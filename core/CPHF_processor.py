import mysql.connector
from core.config import *
from core import util
from core import db_manager
import numpy
import time
import logging

#looging
logging.basicConfig(level=LOGGING_LEVEL)

db_connection = mysql.connector.connect(user=USER_NAME, password=PASSWORD, autocommit=True)
cursor = db_connection.cursor()


def similiarity_index_calculation(ideal, current, user_requested):
    q = ideal - current
    return numpy.sqrt((user_requested * q * q).sum())


def prepare_CPHF_sql(selection_list, table_name, number_of_sensors_to_remove, total_number_of_sensors):
    logging.debug("prepare_CPHF_sql")
    pos = 1
    list = []
    for selection_list_item in selection_list:
        list.append((selection_list_item, pos))
        pos += 1
    list.sort()
    popped_item = list.pop()
    to_remove = popped_item[0]
    to_remove_CP = util.sensor_data_table_column_name_generator(popped_item[1])
    total_number_of_sensors -= to_remove
    middle_content = "SELECT * FROM " + db_manager.DATA_DB_NAME + '.' + db_manager.SENSOR_DATA_TABLE + " AS " + \
                     util.VIRTUAL_SENSOR_DATA_TABLE + " ORDER BY " + to_remove_CP + " LIMIT " + str(
        total_number_of_sensors)
    while len(list) > 0:
        popped_item = list.pop()
        to_remove = popped_item[0]
        to_remove_CP = util.sensor_data_table_column_name_generator(popped_item[1])
        total_number_of_sensors -= to_remove
        wrap_begin = "SELECT * FROM ("

        wrap_end = ") AS " + util.VIRTUAL_SENSOR_DATA_TABLE + " ORDER BY " + to_remove_CP + " LIMIT " \
                   + str(total_number_of_sensors)
        middle_content = wrap_begin + middle_content + wrap_end
    sql_cphf = middle_content
    return sql_cphf


def do(simulated_requests_data, table, number_of_sensors_to_remove, total_number_of_sensors):
    time_start = time.clock()
    logging.debug("CPHF processor do")
    selection_list = []
    pos = 0
    for simulated_requests_data_item in simulated_requests_data[1:]:
        selection_list.insert(pos, round((simulated_requests_data_item / sum(simulated_requests_data[1:])) *
                                         number_of_sensors_to_remove))
        pos += 1
    logging.debug(selection_list)
    sql_cphf = prepare_CPHF_sql(selection_list, util.user_request_data_table_name_generator()[table],
                                number_of_sensors_to_remove, total_number_of_sensors)
    cursor.execute(sql_cphf)
    results = cursor.fetchall()
    for row in results:
        sensor_id = row[0]
        current_sensor_context_data = numpy.asarray(list(row[1:]))
        ideal_sensor_context_data = util.get_ideal_sensor_context_data(current_sensor_context_data)
        user_preferences = numpy.asarray(simulated_requests_data[1:])
        similiarity_index = similiarity_index_calculation(ideal_sensor_context_data, current_sensor_context_data,
                                                          user_preferences)
        logging.debug(type(similiarity_index))
        db_manager.store_data(sensor_id, [similiarity_index], util.temp_data_table_name_generator(dcphf=True)[table])
        # logging.debug(sensor_id, similiarity_index)
        # add a dummy procedure to order the table
    time_end = time.clock()
    time_total = time_end - time_start
    logging.debug(time_total)
    return time_total