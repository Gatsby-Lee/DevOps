Local pySpark
=============

.. code-block:: bash

  $ pyspark
  
  Python 3.7.9 (default, Sep 17 2021, 16:53:38) 
  [Clang 12.0.5 (clang-1205.0.22.11)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  Setting default log level to "WARN".
  To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
  22/08/31 11:41:02 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
  Welcome to
        ____              __
       / __/__  ___ _____/ /__
      _\ \/ _ \/ _ `/ __/  '_/
     /__ / .__/\_,_/_/ /_/\_\   version 3.3.0
        /_/
  
  Using Python version 3.7.9 (default, Sep 17 2021 16:53:38)
  Spark context Web UI available at http://ip-10-0-0-6.us-west-2.compute.internal:4040
  Spark context available as 'sc' (master = local[*], app id = local-1661971263791).
  SparkSession available as 'spark'.
  >>> df = spark.createDataFrame([[11,"moon","lee"]])
  >>> df.printSchema()
  root
   |-- _1: long (nullable = true)
   |-- _2: string (nullable = true)
   |-- _3: string (nullable = true)
