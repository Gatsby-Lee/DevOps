Compression config from Hive to MapReduce
=========================================

Related Topic
-------------
* `How to Generate Parquet in Hive <https://github.com/Gatsby-Lee/StorageResearch/blob/master/apache-hive/how-to-generate-parquet-in-hive.rst>`_
      
      

Context
-------
* Hive uses MapReduce as execution engine.

  * hive.execution.engin=mr

* Hive forces(requests) execution engine ( it's kind of overriding what MR engine config )

  * to compress intermediate and output with the speicfied compression codec.
  * to use the speicfied compression codec for intermediate and output.


Hive config related to compression
----------------------------------
 
* hive.exec.compress.intermediate=true|false
* hive.exec.compress.output=true|false
* hive.intermediate.compression.codec=
* hive.intermediate.compression.type=BLOCK|RECORD|NONE

  * https://issues.apache.org/jira/browse/HIVE-759


MapReduce config related to compression ( MR2 - YARN )
------------------------------------------------------

**To enable MapReduce intermediate compression:**

* mapreduce.map.output.compress=true|false
* mapreduce.map.output.compress.codec=org.apache.hadoop.io.compress.SnappyCodec

**To compress the final output of a MapReduce job:**

* mapreduce.output.fileoutputformat.compress=true
* mapreduce.output.fileoutputformat.compress.type=BLOCK
* mapreduce.output.fileoutputformat.compress.codec=org.apache.hadoop.io.compress.GzipCodec


How to list available compression codecs
----------------------------------------


.. code-block::

  hive> set io.compression.codecs;
  io.compression.codecs=
  org.apache.hadoop.io.compress.DefaultCodec,
  org.apache.hadoop.io.compress.GzipCodec,
  org.apache.hadoop.io.compress.BZip2Codec,
  org.apache.hadoop.io.compress.DeflateCodec,
  org.apache.hadoop.io.compress.SnappyCodec,
  com.hadoop.compression.lzo.LzopCodec



External Rerferences
--------------------
* https://www.slideshare.net/Hadoop_Summit/kamat-singh-june27425pmroom210cv2
* https://www.slideshare.net/oom65/optimize-hivequeriespptx
* https://datameer.zendesk.com/hc/en-us/articles/204258750-How-to-Use-Intermediate-and-Final-Output-Compression-MR1-YARN-
