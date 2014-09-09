





#Setting Database Configuration Parameters
USER_NAME = 'root'
PASSWORD = '123asd123'

#Table names
SENSOR_DATA_TABLE = 'sensordata'
RESULTS_TABLE_FULL = 'results_full'
RESULTS_TABLE_SUMMARY = 'results_summary'
VIRTUAL_SENSOR_DATA_TABLE = 'virtualsensordata'





#Table IDs
USER_REQUEST_DATA_TABLE_ID = "urid"
SENSOR_DATA_TABLE_ID = "sid"
RESULTS_ID_FULL = "rfid"
RESULTS_ID_SUMMARY = "rsid"

#Database names
DATA_DB_NAME = 'TESTDATA'
RESULTS_DB_NAME = 'RESULTS'
TEMP_DB_NAME = 'TEMP'


#Setting Evaluation Parameters
TOTAL_NUMBER_OF_CONTEXT_PROPERTIES = 11
TOTAL_NUMBER_OF_SIMULATED_REQUESTS = 1000
WEIGHTED_SCALES_LIST = [1, 5, 10, 50, 100, 500, 1000]
TOTAL_NUMBER_OF_SENSORS_LIST = [100,
                                500,
                                1000,
                                5000,
                                10000,
                                50000,
                                100000,
                                500000,
                                1000000,
                                5000000,
                                10000000,
                                50000000,
                                100000000,
                                500000000,
                                1000000000]





# import statements
import logging

#Setting up logging level
LOGGING_LEVEL = logging.DEBUG


#Setting Logging Configuration
logging.basicConfig(level=LOGGING_LEVEL)

from core import util

USER_REQUEST_DATA_TABLES = util.user_request_data_table_name_generator()
