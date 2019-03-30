Hive and Impala UDF
===================

Hive UDF
--------

* show functions
* describe function <function_name>

Hive Built-in UDF
^^^^^^^^^^^^^^^^^

*get_json_object*

.. code-block:: sql

  select get_json_object('{"headers":["name","age"], "values":[1,2]}', '$.values[0]');


Impala UDF
-------------------
* Show built-in functions in Impala
* Add UDF function into Impala
* Drop UDF function in Impala

References
-------------------
* https://impala.apache.org/docs/build/html/topics/impala_udf.html
* https://www.cloudera.com/documentation/enterprise/5-11-x/topics/cm_mc_hive_udf.html
* https://www.qubole.com/resources/hive-function-cheat-sheet/
* https://impala.apache.org/docs/build/
* https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF#LanguageManualUDF-get_json_object
