SELECT  COUNT(idBruteForceList)
FROM `iotdata3`.`BruteForceList`, `iotdata3`.`AppxList`
WHERE idBruteForceList = idAppxList;









# SELECT COUNT(*) FROM temp.dcphf_1 AS my2, (

# SELECT temp.brute_force_1.sid AS mytable FROM temp.brute_force_1 ORDER BY temp.brute_force_1.results ASC LIMIT 100

# ) AS mytable WHERE mytable = my2.sid;


    sql_accuracy = "SELECT  COUNT(" + util.temp_data_table_name_generator()[table] + "." + \
                   db_manager.SENSOR_DATA_TABLE_ID + ") FROM " + db_manager.TEMP_DB_NAME + "." + \
                   util.temp_data_table_name_generator()[table] + " , " + db_manager.TEMP_DB_NAME + "." + \
                   util.temp_data_table_name_generator(dcphf=True)[table] + " WHERE " + \
                   util.temp_data_table_name_generator()[table] + "." + db_manager.SENSOR_DATA_TABLE_ID + " = " +\
                   util.temp_data_table_name_generator(dcphf=True)[table] + "." + db_manager.SENSOR_DATA_TABLE_ID