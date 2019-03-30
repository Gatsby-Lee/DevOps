How to generate Parquet in Hive
===============================

Related Topic
-------------
* `Compression Config from Hive to MapReduce <https://github.com/Gatsby-Lee/StorageResearch/blob/master/apache-hive/compression-config-from-hive-to-mapreduce.rst>`_

Context
-------
* Hadoop: cdh 5.15
* Hive 2.6

Settings
--------

* supported compression types for **parquet.compression** are UNCOMPRESSED, GZIP, and SNAPPY.
* **dfs.blocksize**

  possible suffix (case insensitive): k(kilo), m(mega), g(giga), t(tera), p(peta), e(exa) to specify the size (such as 128k, 512m, 1g, etc.), Or provide complete size in bytes (such as 134217728 for 128 MB).

* **parquet.block.size**

  use byte format. e.g) 268435456 is for 256MB ( 256 * 1024 * 1024 )
  or use byte format. e.g) 1073741824 is for 1GB ( 1024 * 1024 * 1024 )

.. code-block:: bash

  SET parquet.compression=SNAPPY;
  SET parquet.block.size=268435456;
  SET dfs.blocksize=268435456;


checking block size of files in HDFS
------------------------------------

.. code-block:: bash

  hdfs fsck <hdfs_path> -files -blocks


  $ hdfs fsck /user/hive/external_warehouse/sampledata/yearmonth=201806/domain_prefix=go/000007_0 -files -blocks;
  Connecting to namenode via http://hadoop1-nn.test.com:50070
  FSCK started by root (auth:SIMPLE) from /10.168.101.83 for path /user/hive/external_warehouse/sampledata/yearmonth=201806/domain_prefix=go/000007_0 at Tue Aug 07 21:26:18 PDT 2018
  /user/hive/external_warehouse/sampledata/yearmonth=201806/domain_prefix=go/000007_0 3477236146 bytes, 13 block(s):  OK
  0. BP-996251660-10.168.101.83-1455223418370:blk_1092141470_18402933 len=268435456 Live_repl=3
  1. BP-996251660-10.168.101.83-1455223418370:blk_1092141473_18402936 len=268435456 Live_repl=3
  2. BP-996251660-10.168.101.83-1455223418370:blk_1092141475_18402938 len=268435456 Live_repl=3
  3. BP-996251660-10.168.101.83-1455223418370:blk_1092141478_18402941 len=268435456 Live_repl=3
  4. BP-996251660-10.168.101.83-1455223418370:blk_1092141480_18402943 len=268435456 Live_repl=3
  5. BP-996251660-10.168.101.83-1455223418370:blk_1092141482_18402945 len=268435456 Live_repl=3
  6. BP-996251660-10.168.101.83-1455223418370:blk_1092141485_18402948 len=268435456 Live_repl=3
  7. BP-996251660-10.168.101.83-1455223418370:blk_1092141487_18402950 len=268435456 Live_repl=3
  8. BP-996251660-10.168.101.83-1455223418370:blk_1092141490_18402953 len=268435456 Live_repl=3
  9. BP-996251660-10.168.101.83-1455223418370:blk_1092141491_18402954 len=268435456 Live_repl=3
  10. BP-996251660-10.168.101.83-1455223418370:blk_1092141493_18402956 len=268435456 Live_repl=3
  11. BP-996251660-10.168.101.83-1455223418370:blk_1092141497_18402960 len=268435456 Live_repl=3
  12. BP-996251660-10.168.101.83-1455223418370:blk_1092141500_18402963 len=256010674 Live_repl=3

  Status: HEALTHY
   Total size:    3477236146 B
   Total dirs:    0
   Total files:   1
   Total symlinks:                0
   Total blocks (validated):      13 (avg. block size 267479703 B)
   Minimally replicated blocks:   13 (100.0 %)
   Over-replicated blocks:        0 (0.0 %)
   Under-replicated blocks:       0 (0.0 %)
   Mis-replicated blocks:         0 (0.0 %)
   Default replication factor:    3
   Average block replication:     3.0
   Corrupt blocks:                0
   Missing replicas:              0 (0.0 %)
   Number of data-nodes:          8
   Number of racks:               1
  FSCK ended at Tue Aug 07 21:26:18 PDT 2018 in 1 milliseconds


External Resources
------------------
* https://www.cloudera.com/documentation/enterprise/latest/topics/cdh_ig_parquet.html#parquet_compatibility
* https://parquet.apache.org/documentation/latest/
* https://hadoop.apache.org/docs/r2.6.0/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml
