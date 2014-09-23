import mysql.connector
from core.config import *
from core import util
import numpy
import time
from core import db_manager
import logging


#looging
logging.basicConfig(level=LOGGING_LEVEL)
#establish database connections
db_connection = mysql.connector.connect(user=USER_NAME, password=PASSWORD)
cursor = db_connection.cursor()


def similiarity_index_calculation(ideal, current, user_requested):
    q = ideal-current
    return numpy.sqrt((user_requested * q * q).sum())


def do(simulated_requests_data, table):
    time_start = time.clock()
    weigeted_Tables = []
    logging.debug("default processor do")
    cursor.execute("SELECT * FROM testdata.sensordata")
    results = cursor.fetchall()
    for row in results:
        sensor_id = row[0]
        current_sensor_context_data = numpy.asarray(list(row[1:]))
        ideal_sensor_context_data = util.get_ideal_sensor_context_data(current_sensor_context_data)
        user_preferences = numpy.asarray(simulated_requests_data[1:])
        similiarity_index = similiarity_index_calculation(ideal_sensor_context_data, current_sensor_context_data,
                                                          user_preferences)
        logging.debug(type(similiarity_index))
        db_manager.store_data(sensor_id, [similiarity_index], util.temp_data_table_name_generator()[table])
        # logging.debug(str(sensor_id), str(similiarity_index))
        # add a dummy procedure to order the table
    time_end = time.clock()
    time_total = time_end - time_start
    logging.debug(time_total)
    return time_total