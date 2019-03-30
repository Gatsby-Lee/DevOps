Create Hive Table for CSV files
===============================

.. code-block:: sql

    CREATE EXTERNAL TABLE `users`(
      `first_name` string,
      `age` int)
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
    STORED AS TEXTFILE 
    LOCATION '/user/hive/external_warehouse/users';
