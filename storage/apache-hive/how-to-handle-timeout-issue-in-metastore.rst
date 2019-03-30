How to Handle Timeout issue When Drop/Alter table
=================================================

Context
-------
* cdh 5.15
* Failed dropping a table having 70k partitions


Noticed Error
-------------

.. code-block:: text

  Logging initialized using configuration in file:/etc/hive/conf.dist/hive-log4j.properties
  FAILED: Execution Error, return code 1 from org.apache.hadoop.hive.ql.exec.DDLTask. MetaException(message:Timeout when executing method: drop_table_with_environment_context; 610758ms exceeds 600000ms)
  

Configuration to set
--------------------

.. code-block:: config

  # default value is 600sec ( 5min )
  SET hive.metastore.client.socket.timeout=1800;
