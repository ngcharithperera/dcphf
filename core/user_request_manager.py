from core.config import *
from core.db_manager import store_data
from scipy.lib.six import xrange
import numpy as np
import logging

#looging
logging.basicConfig(level=LOGGING_LEVEL)

def prepare_simulated_user_requests_data_set(number_of_context_properties, total_number_of_simulated_requests, weight):
    logging.debug("prepare_simulated_user_requests_data_set")
    for user_request_id in xrange(total_number_of_simulated_requests):
        x = np.random.sample(number_of_context_properties)
        sums = sum(x)
        if weight is 1:
            user_request_data_record = [(i/sums) + 1 for i in x]
        else:
            user_request_data_record = [(i/sums) * weight for i in x]
        store_data(user_request_id, user_request_data_record, 'user_requests_' + str(weight))


def create_test_data(number_of_context_properties, total_number_of_simulated_requests, weights):
    logging.debug("create_test_data")
    for weight in weights:
        prepare_simulated_user_requests_data_set(number_of_context_properties, total_number_of_simulated_requests,
                                                 weight)