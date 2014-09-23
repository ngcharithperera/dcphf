# import statements
from core.config import *
from core import accuracy_analyzer
from core import CPHF_processor
from core import db_manager
from core import default_processor
from core import logger_manager
from core import sensor_data_manager
from core import results_summarizer
from core import user_request_manager
from core import visualization_manager
from core import util
from scipy.lib.six import xrange
import logging


#Setting Logging Configuration
logging.basicConfig(level=LOGGING_LEVEL)


def main():
    full_record_id = 0
    db_manager.reset_result_db()
    db_manager.setup_result_db()
    db_manager.setup_result_tables()
    for number_of_context_properties in xrange(2, TOTAL_NUMBER_OF_CONTEXT_PROPERTIES):
        for total_number_of_sensors in TOTAL_NUMBER_OF_SENSORS_LIST:
            db_manager.reset_data_db()
            db_manager.setup_data_db()
            db_manager.setup_data_tables(number_of_context_properties)
            sensor_data_manager.create_test_data(number_of_context_properties, total_number_of_sensors)
            user_request_manager.create_test_data(number_of_context_properties, TOTAL_NUMBER_OF_SIMULATED_REQUESTS,
                                                  WEIGHTED_SCALES_LIST)
            for number_of_sensors_requested in xrange(1, total_number_of_sensors):
                percentage_of_sensors_requested = (number_of_sensors_requested / total_number_of_sensors) * 100.00
                confidence_counter = 0
                for margin_of_error in xrange(1, total_number_of_sensors - number_of_sensors_requested):
                    if confidence_counter > confidence:
                        break
                    margin_of_error_percent = (margin_of_error /
                                               (total_number_of_sensors - number_of_sensors_requested)) * 100.00
                    for ith_user_request in xrange(1, TOTAL_NUMBER_OF_SIMULATED_REQUESTS):
                        db_manager.reset_temp_db()
                        db_manager.setup_temp_db()
                        db_manager.setup_temp_tables(WEIGHTED_SCALES_LIST)
                        simulated_requests_data_list = db_manager.get_user_requests(ith_user_request)
                        logging.debug(simulated_requests_data_list)
                        table = 0
                        for simulated_requests_data in simulated_requests_data_list:
                            full_record_id += 1
                            total_time_brute_force = default_processor.do(simulated_requests_data, table)
                            total_time_cphf = CPHF_processor.do(simulated_requests_data, table, total_number_of_sensors -
                                                                number_of_sensors_requested - margin_of_error,
                                                                total_number_of_sensors)
                            accuracy = accuracy_analyzer.measure(table, number_of_sensors_requested)
                            if accuracy >= 100:
                                confidence_counter += 1
                            else:
                                confidence_counter = 0
                            logging.debug("confidence_counter" + str(confidence_counter))
                            data_row_full = [number_of_context_properties, total_number_of_sensors,
                                             number_of_sensors_requested, percentage_of_sensors_requested, margin_of_error, margin_of_error_percent,
                                             ith_user_request, total_time_brute_force, total_time_cphf, accuracy,
                                             util.WEIGHTED_SCALES_LIST[table]]
                            logging.debug(data_row_full)
                            db_manager.store_data(full_record_id, data_row_full, db_manager.RESULTS_TABLE_FULL)
                            data_row_summary = results_summarizer.update(number_of_context_properties,
                                                                         total_number_of_sensors,
                                                                         number_of_sensors_requested,
                                                                         percentage_of_sensors_requested,
                                                                         margin_of_error,
                                                                         margin_of_error_percent, ith_user_request,
                                                                         total_time_brute_force, total_time_cphf,
                                                                         accuracy,
                                                                         util.WEIGHTED_SCALES_LIST[table])
                            logging.debug(data_row_summary)
                            table += 1
                    # db_manager.store_data(data_row_summary[0], data_row_summary[1:], db_manager.RESULTS_TABLE_SUMMARY)
            #                     logger_manager.log_full_record(full_record)
            #                     logging.debug(total_number_of_sensors)
            # visualization_manager.prepare_data()
            # visualization_manager.plot_charts()

#This is the beginning of the program
main()

