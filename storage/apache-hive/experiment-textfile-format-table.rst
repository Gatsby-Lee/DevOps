Experiment TEXTFILE format table
================================

Hadoop Version ( CDH 5.15 )
---------------------------
* Hadoop2 2.6.0
* Hive 1.1.0

About TEXTFILE
---------------
* Default Hive file format
* Stored as plain text files
* Not splittable!! ( regardless using Snappy codec or not )

  * Hadoop will not be able to split your file into chunks/blocks and run multiple maps in parallel. This can cause underutilization of your cluster's 'mapping' power.

* refer:

  * https://cwiki.apache.org/confluence/display/Hive/CompressedStorage
  * https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL#LanguageManualDDL-StorageFormatsStorageFormatsRowFormat,StorageFormat,andSerDe


Experiment 1
------------
* Using managed table
* no delimeter in **create table**

**CREATE TABLE ( managed | warehouse )**

.. code-block:: sql

  # TEXTFILE is used as default.
  CREATE TABLE zzz_google_serp_text (
    `domain` string,
    `subdomain` string,
    `url` string,
    `searches` int,
    `raw_rank` int,
    `keyword` string);

  CREATE TABLE zzz_google_serp_text (
    `domain` string,
    `subdomain` string,
    `url` string,
    `searches` int,
    `raw_rank` int,
    `keyword` string)
  STORED AS TEXTFILE;

  INSERT INTO TABLE zzz_google_serp_text values
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 10, 1, 'aaa iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 10, 2, 'aaa iphone'),
  ('ccc.com', 'www.ccc.com', 'www.ccc.com/world', 10, 3, 'aaa iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 20, 1, 'bbb iphone'),
  ('ccc.com', 'www.ccc.com', 'www.ccc.com/world', 20, 2, 'bbb iphone'),
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 20, 3, 'bbb iphone'),
  ('ccc.com', 'www.ccc.com', 'www.ccc.com/world', 30, 1, 'ccc iphone'),
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 30, 2, 'ccc iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 30, 3, 'ccc iphone');


**Data in HDFS**

* default: **field-delimited by ctrl-A** ( '\001' ) and **row-delimited by newline**

.. code-block:: bash

  $ hdfs dfs -ls /user/hive/warehouse/zzz_google_serp_text
  Found 1 items
  -rwxrwxrwx   3 root supergroup        486 2018-08-04 16:43 /user/hive/warehouse/zzz_google_serp_text/000000_0

  $ hdfs dfs -cat /user/hive/warehouse/zzz_google_serp_text/000000_0
  aaa.comwww.aaa.comwww.aaa.com/world101aaa iphone
  bbb.comwww.bbb.comwww.bbb.com/world102aaa iphone
  ccc.comwww.ccc.comwww.ccc.com/world103aaa iphone
  bbb.comwww.bbb.comwww.bbb.com/world201bbb iphone
  ccc.comwww.ccc.comwww.ccc.com/world202bbb iphone
  aaa.comwww.aaa.comwww.aaa.com/world203bbb iphone
  ccc.comwww.ccc.comwww.ccc.com/world301ccc iphone
  aaa.comwww.aaa.comwww.aaa.com/world302ccc iphone
  bbb.comwww.bbb.comwww.bbb.com/world303ccc iphone

**Clean up data in Table by TRUNCATE**

.. code-block:: sql

  hive> truncate table zzz_google_serp_text;

**Drop Table**

* Once table is dropped, directory is also removed.

.. code-block:: sql

  hive> drop table zzz_google_serp_text;

  $ hdfs dfs -ls /user/hive/warehouse/zzz_google_serp_text
  ls: `/user/hive/warehouse/zzz_google_serp_text': No such file or directory


Experiment 2
------------
* Using managed table
* comma delimeter for field in **create table**

**CREATE TABLE ( managed | warehouse )**

.. code-block:: sql

  CREATE TABLE zzz_google_serp_text (
    `domain` string,
    `subdomain` string,
    `url` string,
    `searches` int,
    `raw_rank` int,
    `keyword` string)
  ROW FORMAT DELIMITED
    FIELDS TERMINATED BY ','
  STORED AS TEXTFILE;

  INSERT INTO TABLE zzz_google_serp_text values
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 10, 1, 'aaa iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 10, 2, 'aaa iphone'),
  ('ccc.com', 'www.ccc.com', 'www.ccc.com/world', 10, 3, 'aaa iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 20, 1, 'bbb iphone'),
  ('ccc.com', 'www.ccc.com', 'www.ccc.com/world', 20, 2, 'bbb iphone'),
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 20, 3, 'bbb iphone'),
  ('ccc.com', 'www.ccc.com', 'www.ccc.com/world', 30, 1, 'ccc iphone'),
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 30, 2, 'ccc iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 30, 3, 'ccc iphone');


**Data in HDFS**

* **field-delimited by comma** and **row-delimited by newline**
* File size is not different from prev. one which use `\001` as field delimeter.

.. code-block:: bash

  $ hdfs dfs -ls /user/hive/warehouse/zzz_google_serp_text
  Found 1 items
  -rwxrwxrwx   3 root supergroup        486 2018-08-04 17:01 /user/hive/warehouse/zzz_google_serp_text/000000_0

  $ hdfs dfs -cat /user/hive/warehouse/zzz_google_serp_text/000000_0
  aaa.com,www.aaa.com,www.aaa.com/world,10,1,aaa iphone
  bbb.com,www.bbb.com,www.bbb.com/world,10,2,aaa iphone
  ccc.com,www.ccc.com,www.ccc.com/world,10,3,aaa iphone
  bbb.com,www.bbb.com,www.bbb.com/world,20,1,bbb iphone
  ccc.com,www.ccc.com,www.ccc.com/world,20,2,bbb iphone
  aaa.com,www.aaa.com,www.aaa.com/world,20,3,bbb iphone
  ccc.com,www.ccc.com,www.ccc.com/world,30,1,ccc iphone
  aaa.com,www.aaa.com,www.aaa.com/world,30,2,ccc iphone
  bbb.com,www.bbb.com,www.bbb.com/world,30,3,ccc iphone

Experiment 3: Table details
---------------------------

.. code-block:: sql

  hive> describe formatted zzz_google_serp_text;
  OK
  # col_name              data_type               comment

  domain                  string
  subdomain               string
  url                     string
  searches                int
  raw_rank                int
  keyword                 string

  # Detailed Table Information
  Database:               default
  Owner:                  root
  CreateTime:             Sat Aug 04 17:30:04 PDT 2018
  LastAccessTime:         UNKNOWN
  Protect Mode:           None
  Retention:              0
  Location:               hdfs://hadoop1-nn.test.com:8020/user/hive/warehouse/zzz_google_serp_text
  Table Type:             MANAGED_TABLE
  Table Parameters:
          transient_lastDdlTime   1533429004

  # Storage Information
  SerDe Library:          org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe
  InputFormat:            org.apache.hadoop.mapred.TextInputFormat
  OutputFormat:           org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat
  Compressed:             No
  Num Buckets:            -1
  Bucket Columns:         []
  Sort Columns:           []
  Storage Desc Params:
          serialization.format    1
  Time taken: 0.146 seconds, Fetched: 31 row(s)


  hive> describe extended zzz_google_serp_text;
  OK
  domain                  string
  subdomain               string
  url                     string
  searches                int
  raw_rank                int
  keyword                 string

  Detailed Table Information      Table(tableName:zzz_google_serp_text, dbName:default, owner:root, createTime:1533429004, lastAccessTime:0, retention:0, sd:StorageDescriptor(cols:[FieldSchema(name:domain, type:string, comment:null), FieldSchema(name:subdomain, type:string, comment:null), FieldSchema(name:url, type:string, comment:null), FieldSchema(name:searches, type:int, comment:null), FieldSchema(name:raw_rank, type:int, comment:null), FieldSchema(name:keyword, type:string, comment:null)], location:hdfs://hadoop1-nn.staging.test.com:8020/user/hive/warehouse/zzz_google_serp_text, inputFormat:org.apache.hadoop.mapred.TextInputFormat, outputFormat:org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat, compressed:false, numBuckets:-1, serdeInfo:SerDeInfo(name:null, serializationLib:org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe, parameters:{serialization.format=1}), bucketCols:[], sortCols:[], parameters:{}, skewedInfo:SkewedInfo(skewedColNames:[], skewedColValues:[], skewedColValueLocationMaps:{}), storedAsSubDirectories:false), partitionKeys:[], parameters:{transient_lastDdlTime=1533429004}, viewOriginalText:null, viewExpandedText:null, tableType:MANAGED_TABLE)
  Time taken: 0.119 seconds, Fetched: 8 row(s)


Experiment 4
------------
* Using managed table
* testing if each insertion generate new files.

.. code-block:: sql

  CREATE TABLE zzz_google_serp_text (
    `domain` string,
    `subdomain` string,
    `url` string,
    `searches` int,
    `raw_rank` int,
    `keyword` string)
  STORED AS TEXTFILE;

  # data insertion query
  INSERT INTO TABLE zzz_google_serp_text values
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 10, 1, 'aaa iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 10, 2, 'aaa iphone'),
  ('ccc.com', 'www.ccc.com', 'www.ccc.com/world', 10, 3, 'aaa iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 20, 1, 'bbb iphone'),
  ('ccc.com', 'www.ccc.com', 'www.ccc.com/world', 20, 2, 'bbb iphone'),
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 20, 3, 'bbb iphone'),
  ('ccc.com', 'www.ccc.com', 'www.ccc.com/world', 30, 1, 'ccc iphone'),
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 30, 2, 'ccc iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 30, 3, 'ccc iphone');

**Data in HDFS**

* Each insertion generates a file in HDFS

.. code-block:: bash

  # After running insertion statements twice
  $ hdfs dfs -ls /user/hive/warehouse/zzz_google_serp_text
  Found 2 items
  -rwxrwxrwx   3 root supergroup        486 2018-08-04 17:51 /user/hive/warehouse/zzz_google_serp_text/000000_0
  -rwxrwxrwx   3 root supergroup        486 2018-08-04 17:53 /user/hive/warehouse/zzz_google_serp_text/000000_0_copy_1

  $ hdfs dfs -cat /user/hive/warehouse/zzz_google_serp_text/000000_0
  aaa.comwww.aaa.comwww.aaa.com/world101aaa iphone
  bbb.comwww.bbb.comwww.bbb.com/world102aaa iphone
  ccc.comwww.ccc.comwww.ccc.com/world103aaa iphone
  bbb.comwww.bbb.comwww.bbb.com/world201bbb iphone
  ccc.comwww.ccc.comwww.ccc.com/world202bbb iphone
  aaa.comwww.aaa.comwww.aaa.com/world203bbb iphone
  ccc.comwww.ccc.comwww.ccc.com/world301ccc iphone
  aaa.comwww.aaa.comwww.aaa.com/world302ccc iphone
  bbb.comwww.bbb.comwww.bbb.com/world303ccc iphone

  $ hdfs dfs -cat /user/hive/warehouse/zzz_google_serp_text/000000_0_copy_1
  aaa.comwww.aaa.comwww.aaa.com/world101aaa iphone
  bbb.comwww.bbb.comwww.bbb.com/world102aaa iphone
  ccc.comwww.ccc.comwww.ccc.com/world103aaa iphone
  bbb.comwww.bbb.comwww.bbb.com/world201bbb iphone
  ccc.comwww.ccc.comwww.ccc.com/world202bbb iphone
  aaa.comwww.aaa.comwww.aaa.com/world203bbb iphone
  ccc.comwww.ccc.comwww.ccc.com/world301ccc iphone
  aaa.comwww.aaa.comwww.aaa.com/world302ccc iphone
  bbb.comwww.bbb.comwww.bbb.com/world303ccc iphone

  # After running insertion statements three times
  $ hdfs dfs -ls /user/hive/warehouse/zzz_google_serp_text
  Found 3 items
  -rwxrwxrwx   3 root supergroup        486 2018-08-04 17:51 /user/hive/warehouse/zzz_google_serp_text/000000_0
  -rwxrwxrwx   3 root supergroup        486 2018-08-04 17:53 /user/hive/warehouse/zzz_google_serp_text/000000_0_copy_1
  -rwxrwxrwx   3 root supergroup        486 2018-08-04 17:58 /user/hive/warehouse/zzz_google_serp_text/000000_0_copy_2

  # Used differet insertion
  INSERT INTO TABLE zzz_google_serp_text values
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 10, 1, 'aaa iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 30, 3, 'ccc iphone');

  # I thought Hive could detect same query and put `copy` suffix, but it wasn't.
  # Even the different query genereates `000000_0_copy_3`
  $ hdfs dfs -ls /user/hive/warehouse/zzz_google_serp_text
  Found 4 items
  -rwxrwxrwx   3 root supergroup        486 2018-08-04 17:51 /user/hive/warehouse/zzz_google_serp_text/000000_0
  -rwxrwxrwx   3 root supergroup        486 2018-08-04 17:53 /user/hive/warehouse/zzz_google_serp_text/000000_0_copy_1
  -rwxrwxrwx   3 root supergroup        486 2018-08-04 17:58 /user/hive/warehouse/zzz_google_serp_text/000000_0_copy_2
  -rwxrwxrwx   3 root supergroup        108 2018-08-04 18:00 /user/hive/warehouse/zzz_google_serp_text/000000_0_copy_3


Experiment 5
------------
* Using managed table
* Check if `TBLPROPERTIES('textfile.compress'='snappy')` affects. ( NO!! )

.. code-block:: sql

  CREATE TABLE zzz_google_serp_text (
    `domain` string,
    `subdomain` string,
    `url` string,
    `searches` int,
    `raw_rank` int,
    `keyword` string)
  TBLPROPERTIES('textfile.compress'='snappy');

  # data insertion query
  INSERT INTO TABLE zzz_google_serp_text values
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 10, 1, 'aaa iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 10, 2, 'aaa iphone'),
  ('ccc.com', 'www.ccc.com', 'www.ccc.com/world', 10, 3, 'aaa iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 20, 1, 'bbb iphone'),
  ('ccc.com', 'www.ccc.com', 'www.ccc.com/world', 20, 2, 'bbb iphone'),
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 20, 3, 'bbb iphone'),
  ('ccc.com', 'www.ccc.com', 'www.ccc.com/world', 30, 1, 'ccc iphone'),
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 30, 2, 'ccc iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 30, 3, 'ccc iphone');

**Data in HDFS**

* Each insertion generates a file in HDFS

.. code-block:: bash

  # After running insertion statements twice
  $ hdfs dfs -ls /user/hive/warehouse/zzz_google_serp_text
  Found 1 items
  -rwxrwxrwx   3 root supergroup        486 2018-08-05 12:59 /user/hive/warehouse/zzz_google_serp_text/000000_0

  $ hdfs dfs -cat /user/hive/warehouse/zzz_google_serp_text/000000_0
  aaa.comwww.aaa.comwww.aaa.com/world101aaa iphone
  bbb.comwww.bbb.comwww.bbb.com/world102aaa iphone
  ccc.comwww.ccc.comwww.ccc.com/world103aaa iphone
  bbb.comwww.bbb.comwww.bbb.com/world201bbb iphone
  ccc.comwww.ccc.comwww.ccc.com/world202bbb iphone
  aaa.comwww.aaa.comwww.aaa.com/world203bbb iphone
  ccc.comwww.ccc.comwww.ccc.com/world301ccc iphone
  aaa.comwww.aaa.comwww.aaa.com/world302ccc iphone
  bbb.comwww.bbb.comwww.bbb.com/world303ccc iphone



Experiment 6: Enable Compression by using Hive setting ( without setting codec )
--------------------------------------------------------------------------------
* Using managed table
* not set `mapreduce.output.fileoutputformat.compress.codec` ( default is used. )

.. code-block:: sql

  hive> DROP TABLE IF EXISTS zzz_google_serp_text;
  hive> CREATE TABLE zzz_google_serp_text (
    `domain` string,
    `subdomain` string,
    `url` string,
    `searches` int,
    `raw_rank` int,
    `keyword` string);

  # Enable Gzip Compression on Final Output
  hive> set hive.exec.compress.output=true;

  # data insertion query
  hive> INSERT INTO TABLE zzz_google_serp_text values
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 10, 1, 'aaa iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 10, 2, 'aaa iphone'),
  ('ccc.com', 'www.ccc.com', 'www.ccc.com/world', 10, 3, 'aaa iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 20, 1, 'bbb iphone'),
  ('ccc.com', 'www.ccc.com', 'www.ccc.com/world', 20, 2, 'bbb iphone'),
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 20, 3, 'bbb iphone'),
  ('ccc.com', 'www.ccc.com', 'www.ccc.com/world', 30, 1, 'ccc iphone'),
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 30, 2, 'ccc iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 30, 3, 'ccc iphone');

  # Files in Dirctory
  hive> dfs -ls /user/hive/warehouse/zzz_google_serp_text/;
  -rwxrwxrwx   3 root supergroup        114 2018-08-05 13:42 /user/hive/warehouse/zzz_google_serp_text/000000_0.deflate

  # content is compressed with zlib/deflate. It is the default data compression format.
  hive> dfs -cat /user/hive/warehouse/zzz_google_serp_text/000000_0.deflate;
  xKLL//d02
  2
   2u%''a#tȅ@!F 1ȅ@!qr!ve>

  hive> dfs -text /user/hive/warehouse/zzz_google_serp_text/000000_0.deflate;
  aaa.comwww.aaa.comwww.aaa.com/world101aaa iphone
  bbb.comwww.bbb.comwww.bbb.com/world102aaa iphone
  ccc.comwww.ccc.comwww.ccc.com/world103aaa iphone
  bbb.comwww.bbb.comwww.bbb.com/world201bbb iphone
  ccc.comwww.ccc.comwww.ccc.com/world202bbb iphone
  aaa.comwww.aaa.comwww.aaa.com/world203bbb iphone
  ccc.comwww.ccc.comwww.ccc.com/world301ccc iphone
  aaa.comwww.aaa.comwww.aaa.com/world302ccc iphone
  bbb.comwww.bbb.comwww.bbb.com/world303ccc iphone


Experiment 7: Enable Compression by using Hive setting
---------------------------------------------------------------
* Using managed table
* Set `mapreduce.output.fileoutputformat.compress.codec` with specfic codecs.

.. code-block:: sql

  hive> DROP TABLE IF EXISTS zzz_google_serp_text;
  hive> CREATE TABLE zzz_google_serp_text (
    `domain` string,
    `subdomain` string,
    `url` string,
    `searches` int,
    `raw_rank` int,
    `keyword` string);

  # Enable Gzip Compression on Final Output
  hive> set hive.exec.compress.output=true;
  hive> set mapreduce.output.fileoutputformat.compress.codec=org.apache.hadoop.io.compress.GzipCodec;

  # data insertion query
  hive> INSERT INTO TABLE zzz_google_serp_text values
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 10, 1, 'aaa iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 10, 2, 'aaa iphone'),
  ('ccc.com', 'www.ccc.com', 'www.ccc.com/world', 10, 3, 'aaa iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 20, 1, 'bbb iphone'),
  ('ccc.com', 'www.ccc.com', 'www.ccc.com/world', 20, 2, 'bbb iphone'),
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 20, 3, 'bbb iphone'),
  ('ccc.com', 'www.ccc.com', 'www.ccc.com/world', 30, 1, 'ccc iphone'),
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 30, 2, 'ccc iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 30, 3, 'ccc iphone');

  hive> dfs -ls /user/hive/warehouse/zzz_google_serp_text;
  Found 1 items
  -rwxrwxrwx   3 root supergroup        126 2018-08-05 13:54 /user/hive/warehouse/zzz_google_serp_text/000000_0.gz

  hive> dfs -text /user/hive/warehouse/zzz_google_serp_text/000000_0.gz;
  aaa.comwww.aaa.comwww.aaa.com/world101aaa iphone
  bbb.comwww.bbb.comwww.bbb.com/world102aaa iphone
  ccc.comwww.ccc.comwww.ccc.com/world103aaa iphone
  bbb.comwww.bbb.comwww.bbb.com/world201bbb iphone
  ccc.comwww.ccc.comwww.ccc.com/world202bbb iphone
  aaa.comwww.aaa.comwww.aaa.com/world203bbb iphone
  ccc.comwww.ccc.comwww.ccc.com/world301ccc iphone
  aaa.comwww.aaa.comwww.aaa.com/world302ccc iphone
  bbb.comwww.bbb.comwww.bbb.com/world303ccc iphone

  # switch to `org.apache.hadoop.io.compress.SnappyCodec`
  hive> set mapreduce.output.fileoutputformat.compress.codec=org.apache.hadoop.io.compress.SnappyCodec;

  # data insertion query
  hive> INSERT INTO TABLE zzz_google_serp_text values
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 10, 1, 'aaa iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 10, 2, 'aaa iphone'),
  ('ccc.com', 'www.ccc.com', 'www.ccc.com/world', 10, 3, 'aaa iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 20, 1, 'bbb iphone'),
  ('ccc.com', 'www.ccc.com', 'www.ccc.com/world', 20, 2, 'bbb iphone'),
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 20, 3, 'bbb iphone'),
  ('ccc.com', 'www.ccc.com', 'www.ccc.com/world', 30, 1, 'ccc iphone'),
  ('aaa.com', 'www.aaa.com', 'www.aaa.com/world', 30, 2, 'ccc iphone'),
  ('bbb.com', 'www.bbb.com', 'www.bbb.com/world', 30, 3, 'ccc iphone');

  hive> dfs -ls /user/hive/warehouse/zzz_google_serp_text;
  Found 2 items
  -rwxrwxrwx   3 root supergroup        126 2018-08-05 13:54 /user/hive/warehouse/zzz_google_serp_text/000000_0.gz
  -rwxrwxrwx   3 root supergroup        190 2018-08-05 13:59 /user/hive/warehouse/zzz_google_serp_text/000000_0.snappy
