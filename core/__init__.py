# from pip._vendor.requests.packages.urllib3.connectionpool import xrange
# import mysql.connector
#
from numpy import *
from scipy import *



import numpy as np
import logging
# #from core.dbhandle import *
#
#
# DB_NAME = 'iotdata3'
# #
# #
# # def establish_database_server_connection():
# #     config = {
# #         'user': 'root',
# #         'password': '123asd123',
# #         'host': '127.0.0.1',    }
# #     try:
# #         db_connection = mysql.connector.connect(**config)
# #         cursor = db_connection.cursor()
# #         return cursor
# #         print('dummy_create_sensor_table')
# #     except mysql.connector.Error as err:
# #         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
# #             print("Something is wrong with your user name or password")
# #         elif err.errno == errorcode.ER_BAD_DB_ERROR:
# #             print("Database does not exists")
# #         else:
# #             print(err)
# #     else:
# #         db_connection.close()
# #
# #
# # def create_sensor_tables():
# #     cursor = establish_database_server_connection()
# #     print('create_sensor_table')
# #
# #
# # def create_databases():
# #     cnx = mysql.connector.connect(user='root', password='123asd123')
# #     cursor = cnx.cursor()
# #     try:
# #         cursor.execute(
# #             "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
# #         print("Database: {} successfully created".format(DB_NAME))
# #     except mysql.connector.Error as err:
# #         print("Failed creating database: {}".format(err))
# #
# #
# # def create_database_server_connection():
# #     print('dummy_reset_data_source')
# #
# #
# # def reset_data_source():
# #     cnx = mysql.connector.connect(user='root', password='123asd123')
# #     cursor = cnx.cursor()
# #     try:
# #         cursor.execute("DROP DATABASE {}".format(DB_NAME))
# #         print("Database: {} successfully deleted".format(DB_NAME))
# #     except mysql.connector.Error as err:
# #         print("Failed creating database: {}".format(err))
# #
# #
# # def main():
# #     reset_data_source()
# #     create_databases()
#
#
#     #
#     # number_of_context_properties = 101
#     # total_number_of_sensors_list = [10, 20, 30]
#     # number_of_simulated_user_requests = 1000000
#     # for ithCP in xrange(1, number_of_context_properties):
#     #     for total_number_of_sensors in total_number_of_sensors_list:
#     #         reset_data_source()
#     #         create_databases()
#     #         create_sensor_tables()
#     #         print(total_number_of_sensors)
# from scipy.spatial.distance import cdist
#
#
# def insertdata():
#     dbhandler.printing();
#     # db = mysql.connector.connect(user='root', password='123asd123')
#     # cursor = db.cursor()
#     # for x in range(0, 100000):
#     #     sql = "INSERT INTO iotdata3.TestNumbers(one,two,three)VALUES({0},{1},{2})".format(random.random(), random.random(), random.random())
#     #     cursor.execute(sql)
#     #     db.commit()
#     # db.close()
#
#
#
# def fast_wdist(A, B, W):
#     """
#     Compute the weighted euclidean distance between two arrays of points:
#
#     D{i,j} =
#     sqrt( ((A{0,i}-B{0,j})/W{0,i})^2 + ... + ((A{k,i}-B{k,j})/W{k,i})^2 )
#
#     inputs:
#         A is an (k, m) array of coordinates
#         B is an (k, n) array of coordinates
#         W is an (k, m) array of weights
#
#     returns:
#         D is an (m, n) array of weighted euclidean distances
#     """
#
#     # compute the differences and apply the weights in one go using
#     # broadcasting jujitsu. the result is (n, k, m)
#     wdiff = (A[np.newaxis,...] - B[np.newaxis,...].T) / W[np.newaxis,...]
#
#     # square and sum over the second axis, take the sqrt and transpose. the
#     # result is an (m, n) array of weighted euclidean distances
#     D = np.sqrt((wdiff*wdiff).sum(1)).T
#
#     return D
#
#
# def setup(k=2, m=1, n=1):
#     return np.random.randn(k, m), np.random.randn(k, n), np.random.randn(k, m)
#
#


def weightedL2(a,b,w):
    q = a-b
    return np.sqrt((w*q*q).sum())


def main2():
    print("test")
    mylist = [(14, 5), (36, 1), (69, 8), (38, 2), (25, 4), (86, 3)]
    print(mylist)
    mylist.sort()
    print(mylist)

    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    logging.info("test")


    # #a, b, w = setup()
    # #a = array([0.5, 0.3, 0.3])
    # #b = array([0.3, 0.1, 0.3])
    # #w = array([0.2, 0.8, 0.2])
    #
    # a = array([0.3, 0.4])
    # c = array([0.5, 0.3])
    # b = array([0.0, 0.0])
    # w = array([1.0, 30.9])
    #
    #
    # #d1 = fast_wdist(a, b, w)
    # #b = np.zeros(2, 1)
    # #print(a)
    # d2 = weightedL2(a,b,w)
    # print(d2)
    # d2 = weightedL2(c,b,w)
    # print(d2)
    # #print(d1)
    # #Y = cdist(a, b, 'euclidean') #working
    # #print(Y)
#
main2()
#
#
# insertdata()
#
#
#
#
# import mysql.connector
# from scipy.lib.six import xrange
# from core import logger_manager
#
#
# #Database configuration
# USER_NAME = 'root'
# PASSWORD = '123asd123'
#
#
# def main():
#     # x = np.random.sample(3)
#     # sums = sum(x)
#     # norm = [i/sums for i in x]
#     # print(norm)
#
#     db_connection = mysql.connector.connect(user=USER_NAME, password=PASSWORD)
#     cursor = db_connection.cursor()
#     cursor.execute("SELECT * FROM testdata.sensordata")
#     results = cursor.fetchall()
#     for row in results:
#         print(row)
#
#
# main()