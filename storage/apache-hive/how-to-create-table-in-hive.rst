How to Create Table in Hive
===========================

Text Format ( default )
-----------------------

.. code-block:: SQL

  hive> CREATE TABLE `keywords`(
      > `name` string);

  hive> CREATE TABLE `keywords`(
      > `name` string)
      > STORED AS TEXTFILE;

  hive> show create table keywords;
  OK
  CREATE TABLE `keywords`(
    `name` string)
  ROW FORMAT SERDE 
    'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe' 
  STORED AS INPUTFORMAT 
    'org.apache.hadoop.mapred.TextInputFormat' 
  OUTPUTFORMAT 
    'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
  LOCATION
    'hdfs://hadoop-nn.test.com:8020/user/hive/warehouse/keywords'
  TBLPROPERTIES (
    'transient_lastDdlTime'='1531756136');
    

RCFile Format
-------------

.. code-block:: SQL

  hive> CREATE TABLE `keywords`(
      > `name` string)
      > STORED AS RCFILE;
      
  hive> show create table keywords;
  CREATE TABLE `keywords`(
    `name` string)
  ROW FORMAT SERDE 
    'org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe' 
  STORED AS INPUTFORMAT 
    'org.apache.hadoop.hive.ql.io.RCFileInputFormat' 
  OUTPUTFORMAT 
    'org.apache.hadoop.hive.ql.io.RCFileOutputFormat'
  LOCATION
    'hdfs://hadoop-nn.test.com:8020/user/hive/warehouse/keywords'
  TBLPROPERTIES (
    'transient_lastDdlTime'='1531756578')

Avro Format
-----------

.. code-block:: SQL

  hive> CREATE TABLE `keywords`(
      > `name` string)
      > STORED AS AVRO;

  hive> show create table keywords;
  CREATE TABLE `keywords`(
    `name` string COMMENT '')
  ROW FORMAT SERDE 
    'org.apache.hadoop.hive.serde2.avro.AvroSerDe' 
  STORED AS INPUTFORMAT 
    'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat' 
  OUTPUTFORMAT 
    'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
  LOCATION
    'hdfs://hadoop-nn.test.com:8020/user/hive/warehouse/keywords'
  TBLPROPERTIES (
    'transient_lastDdlTime'='1532118617')
