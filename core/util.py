from core.config import *
import logging

#looging
logging.basicConfig(level=LOGGING_LEVEL)

def sensor_data_table_column_name_generator(pos):
    return VIRTUAL_SENSOR_DATA_TABLE + ".CP"+str(pos)


def temp_data_table_name_generator(dcphf = False):
    pos = 0
    tables = []
    for weight in WEIGHTED_SCALES_LIST:
        if dcphf is True:
            tables.insert(pos, "dcphf_"+str(weight))
        else:
            tables.insert(pos, "brute_force_"+str(weight))
        pos += 1
    return tables


def user_request_data_table_name_generator():
    pos = 0
    tables = []
    for weight in WEIGHTED_SCALES_LIST:
        tables.insert(pos, "user_requests_"+str(weight))
        pos += 1
    return tables


def get_ideal_sensor_context_data(current_sensor_context_data):
    i = len(current_sensor_context_data)
    return [0.0] * i
