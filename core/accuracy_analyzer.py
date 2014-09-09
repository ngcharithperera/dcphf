from core.config import *
import mysql.connector
from core import util
from core import db_manager
import logging

#looging
logging.basicConfig(level=LOGGING_LEVEL)

db_connection = mysql.connector.connect(user=USER_NAME, password=PASSWORD, autocommit=True)
cursor = db_connection.cursor()


def measure(table, number_of_sensors_requested):
    logging.debug("measure")
    sql_inner = " SELECT " + db_manager.TEMP_DB_NAME + "." + util.temp_data_table_name_generator()[table] + "." +\
                db_manager.SENSOR_DATA_TABLE_ID + " AS brute_force_table FROM " + db_manager.TEMP_DB_NAME + "." + \
                util.temp_data_table_name_generator()[table] + " ORDER BY " + db_manager.TEMP_DB_NAME + "." + \
                util.temp_data_table_name_generator()[table] + ".results ASC LIMIT " + str(number_of_sensors_requested)

    sql_accuracy = " SELECT COUNT(*) FROM " + db_manager.TEMP_DB_NAME + "." + \
                util.temp_data_table_name_generator(dcphf=True)[table] + " AS dcphf_table, ( " + sql_inner + \
                ") AS brute_force_table  WHERE brute_force_table = dcphf_table." + db_manager.SENSOR_DATA_TABLE_ID
    cursor.execute(sql_accuracy)
    results = cursor.fetchall()
    logging.debug(results[0][0] / number_of_sensors_requested * 100.0000)
    return results[0][0] / number_of_sensors_requested