from core import db_manager
from core.db_manager import store_data
from scipy.lib.six import xrange
import numpy as np
import logging
from core.config import *

#looging
logging.basicConfig(level=LOGGING_LEVEL)


def sensor_data_generator():
    sensor_data_record = 0
    logging.debug("sensor_data_generator")
    return sensor_data_record


def user_request_data_generator():
    user_request_dataa_record = 0
    logging.debug("user_request_data_generator")
    return user_request_dataa_record


def prepare_simulated_sensor_data_set(number_of_context_properties, total_number_of_sensors):
    logging.debug("prepare_simulated_sensor_data_set")
    for sensor_id in xrange(total_number_of_sensors):
        sensor_data_record = np.random.sample(number_of_context_properties)
        store_data(sensor_id, sensor_data_record, 'sensor_data')


def create_test_data(number_of_context_properties, total_number_of_sensors):
    logging.debug("create_test_data")
    prepare_simulated_sensor_data_set(number_of_context_properties, total_number_of_sensors)