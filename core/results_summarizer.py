from core.config import *
import logging

#looging
logging.basicConfig(level=LOGGING_LEVEL)

accuracy_min = 0
accuracy_max = 0
accuracy_avg = 0


def update(number_of_context_properties, total_number_of_sensors,
           number_of_sensors_requested, percentage_of_sensors_requested, margin_of_error,margin_of_error_percent,
           ith_user_request,  total_time_brute_force,
           total_time_cphf, accuracy, weights):
    logging.debug("results_summarizer")
    global accuracy_min
    global accuracy_max
    global accuracy_avg
    if accuracy < accuracy_min:
        accuracy_min = accuracy

    if accuracy > accuracy_max:
        accuracy_max = accuracy
    accuracy_avg = ((accuracy_avg * ith_user_request) + accuracy) / (ith_user_request + 1)
    data_row_summary = [number_of_context_properties, total_number_of_sensors, number_of_sensors_requested,
                        percentage_of_sensors_requested, margin_of_error, margin_of_error_percent,
                        total_time_brute_force, total_time_cphf, accuracy_min,
                        accuracy_max, accuracy_avg, weights]
    return data_row_summary
