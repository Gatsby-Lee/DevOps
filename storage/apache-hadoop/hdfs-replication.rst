HDFS Replication
################

* https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml
* https://community.cloudera.com/t5/Support-Questions/How-to-fix-under-replicated-blocks-fasly-its-take-long-time/m-p/164417

cmd to save namespace
=====================

.. code-block: bash

    sudo -u hdfs hdfs dfsadmin -safemode enter
    sudo -u hdfs hdfs dfsadmin -safemode get
    sudo -u hdfs hdfs dfsadmin -saveNamespace
    sudo -u hdfs hdfs dfsadmin -safemode leave


hdfs-site.xml
=============

* dfs.namenode.replication.work.multiplier.per.iteration
* dfs.namenode.replication.max-streams
* dfs.namenode.replication.max-streams-hard-limit
