#import statements
import logging


LOGGER_STATUS_FLAG = 0
FORMAT = "%(asctime)-15s %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def config_log_file():
    global LOGGER_STATUS_FLAG
    logger = logging.getLogger('DCPHF_Logger')
    if LOGGER_STATUS_FLAG is 0:
        fmt = logging.Formatter(FORMAT, datefmt=DATE_FORMAT)
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler('application.log')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(fmt)
        logger.addHandler(fh)
        LOGGER_STATUS_FLAG = 1
        return logger
    else:
        return logger


def log_to_file(message):
    logger = config_log_file()
    logger.debug(message)


def log_full_record():
    logging.debug("log_full_record")