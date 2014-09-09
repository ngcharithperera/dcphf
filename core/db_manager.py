# import statements
from core.config import *
from core import logger_manager
from mysql import connector
from scipy.lib.six import xrange
import logging





#Establish Database Connections
db_connection = connector.connect(user=USER_NAME, password=PASSWORD, autocommit=True)
cursor = db_connection.cursor()


def create_table(db_name, table_name, sql):
    logging.debug("create_table")
    try:
        cursor.execute(sql)
        logging.debug("Table: {0} successfully created in database {1}".format(table_name, db_name))
    except connector.Error as err:
        logging.debug("Failed creating table: {}".format(err))


def prepare_create_table_sql(number_of_context_properties, database_name, table_name, id_column):
    start = id_column + " BIGINT NOT NULL ,"
    end = "PRIMARY KEY (" + id_column + ")"
    mid = ""
    for ithCP in xrange(1, number_of_context_properties + 1):
        mid = mid + "CP" + str(ithCP) + " DOUBLE NULL , "
    table_definition = start + mid + end
    sql_create_table_main = "CREATE  TABLE IF NOT EXISTS " + database_name + "." + table_name + \
                            " ( " + table_definition + " )"
    full_sql = sql_create_table_main
    return full_sql


def create_tables_for_simulated_user_requests(number_of_context_properties):
    logging.debug("create_tables_for_simulated_user_requests")
    for USER_REQUEST_DATA_TABLE in USER_REQUEST_DATA_TABLES:
        full_sql = prepare_create_table_sql(number_of_context_properties, DATA_DB_NAME, USER_REQUEST_DATA_TABLE,
                                            USER_REQUEST_DATA_TABLE_ID)
        create_table(DATA_DB_NAME, USER_REQUEST_DATA_TABLE, full_sql)


def create_tables_for_simulated_sensor_data(number_of_context_properties):
    logging.debug("create_tables_for_simulated_sensor_data")
    full_sql = prepare_create_table_sql(number_of_context_properties, DATA_DB_NAME, SENSOR_DATA_TABLE,
                                        SENSOR_DATA_TABLE_ID)
    create_table(DATA_DB_NAME, SENSOR_DATA_TABLE, full_sql)


def setup_data_tables(number_of_context_properties):
    logging.debug("setup_tables")
    create_tables_for_simulated_sensor_data(number_of_context_properties)
    create_tables_for_simulated_user_requests(number_of_context_properties)


def setup_temp_db():
    logging.debug("setup_temp_db")
    create_database(TEMP_DB_NAME)


def setup_data_db():
    logging.debug("setup_db")
    create_database(DATA_DB_NAME)
    create_database(RESULTS_DB_NAME)


def reset_temp_db():
    logging.debug("reset_temp_db")
    delete_database(TEMP_DB_NAME)


def reset_data_db():
    logging.debug("reset_db")
    delete_database(DATA_DB_NAME)


def create_database(db_name):
    try:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
        logging.debug("Database: {} successfully created".format(db_name))
    except connector.Error as err:
        logging.debug("Failed creating database: {}".format(err))


def delete_database(db_name):
    logging.debug("delete_database")
    try:
        cursor.execute("DROP DATABASE IF EXISTS {}".format(db_name))
        logging.debug("Database: {} successfully deleted if existed".format(db_name))
    except Exception as err:
        logging.debug("Failed: Deleting database: {}".format(err))


def insert_data_to_db(id, data, db_name, table_name):
    # logging.debug("insert_data_to_db")
    values = ''
    # if type(data) is not 'float':
    for ith_data_item in data:
        values = values + ", " + str(ith_data_item)
    # else:
    #     values = values + ", " + str(data)
    sql = "INSERT INTO " + db_name + "." + table_name + " VALUES(" + str(id) + values + ")"
    cursor.execute(sql)
    db_connection.commit()


def store_data(row_id, data, table_type):
    # logging.debug("store_data")
    if table_type is 'sensor_data':
        insert_data_to_db(row_id, data, DATA_DB_NAME, SENSOR_DATA_TABLE)
    elif 'user_requests_' in table_type:
        insert_data_to_db(row_id, data, DATA_DB_NAME, table_type)
    elif 'brute_force_' in table_type:
        insert_data_to_db(row_id, data, TEMP_DB_NAME,  table_type)
    elif 'dcphf_' in table_type:
        insert_data_to_db(row_id, data, TEMP_DB_NAME,  table_type)
    elif 'results_' in table_type:
        insert_data_to_db(row_id, data, RESULTS_DB_NAME,  table_type)
    else:
        logging.debug("something wrong..")


def prepare_create_temp_table_sql(database_name, table_name, id_column):
    logging.debug("prepare_create_temp_table_sql")
    start = id_column + " BIGINT NOT NULL ,"
    end = "PRIMARY KEY (" + id_column + ")"
    mid = " results DOUBLE NULL , "
    table_definition = start + mid + end
    sql_create_table_main = "CREATE  TABLE IF NOT EXISTS " + database_name + "." + table_name + \
                            " ( " + table_definition + " )"
    full_sql = sql_create_table_main
    return full_sql


def create_tables_for_temp_data(table_name):
    logging.debug("create_tables_for_temp_data")
    full_sql = prepare_create_temp_table_sql(TEMP_DB_NAME, table_name, SENSOR_DATA_TABLE_ID)
    create_table(TEMP_DB_NAME, table_name, full_sql)


def setup_temp_tables(weights):
    logging.debug("setup_temp_tables")
    for weight in weights:
        table_name = "brute_force_" + str(weight)
        create_tables_for_temp_data(table_name)
        table_name = "dcphf_" + str(weight)
        create_tables_for_temp_data(table_name)


def prepare_create_results_table_sql(database_name, table_name, id_column):
    logging.debug("prepare_create_temp_table_sql")
    start = id_column + " BIGINT NOT NULL ,"
    end = "PRIMARY KEY (" + id_column + ")"
    if table_name is RESULTS_TABLE_FULL:
        mid = " numberofcp                      BIGINT NULL ," \
              " numberoftotalsensors            BIGINT NULL ," \
              " numberofsensorsrequested        BIGINT NULL ," \
              " percentageofsensorsrequested    DOUBLE(7,4) NULL , " \
              " marginoferror                   BIGINT NULL ," \
              " marginoferrorpercent            DOUBLE(7,4) NULL , " \
              " urid                            BIGINT NULL , " \
              " timedefault                     BIGINT NULL ," \
              " timecphf                        BIGINT NULL , " \
              " accuracy                        DOUBLE(7,4) NULL , " \
              " weight                          BIGINT NULL ,"
    elif table_name is RESULTS_TABLE_SUMMARY :
        mid = " numberofcp                      BIGINT NULL ," \
              " numberoftotalsensors            BIGINT NULL ," \
              " numberofsensorsrequested        BIGINT NULL ," \
              " percentageofsensorsrequested    DOUBLE(7,4) NULL , " \
              " marginoferror                   BIGINT NULL ," \
              " marginoferrorpercent            DOUBLE(7,4) NULL , " \
              " timedefault                     BIGINT NULL ," \
              " timecphf                        BIGINT NULL , " \
              " accuracy                        DOUBLE(7,4) NULL , " \
              " weight                          BIGINT NULL ,"
    else:
        logging.debug("Error")
    table_definition = start + mid + end
    sql_create_table_main = "CREATE  TABLE IF NOT EXISTS " + database_name + "." + table_name + \
                            " ( " + table_definition + " )"
    full_sql = sql_create_table_main
    return full_sql


def create_tables_for_results_data(table_name):
    logging.debug("create_tables_for_temp_data")
    full_sql = prepare_create_results_table_sql(RESULTS_DB_NAME, table_name, RESULTS_ID_FULL)
    create_table(RESULTS_DB_NAME, table_name, full_sql)


def reset_result_db():
    logging.debug("reset_result_db")
    delete_database(RESULTS_DB_NAME)


def setup_result_db():
    logging.debug("setup_result_db")
    create_database(RESULTS_DB_NAME)


def setup_result_tables():
    logging.debug("setup_result_tables")
    create_tables_for_results_data(RESULTS_TABLE_FULL)
    create_tables_for_results_data(RESULTS_TABLE_SUMMARY)


def get_user_requests(ith_user_request):
    logging.debug("get_user_requests")
    simulated_requests_data = []
    pos = 0
    tables = util.user_request_data_table_name_generator();
    for table in tables:
        cursor.execute("SELECT * FROM testdata." + table + " WHERE urid=" + str(ith_user_request))
        results = cursor.fetchall()
        for row in results:
            simulated_requests_data.insert(pos, list(row))
            pos += 1
    # logging.debug(simulated_requests_data)
    # logging.debug(simulated_requests_data)
    return simulated_requests_data