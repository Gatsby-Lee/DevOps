Hadoop MR Historyserver
#######################

mapred-site.xml
===============

* yarn.app.mapreduce.am.staging-dir
* mapreduce.jobhistory.intermediate-done-dir
* mapreduce.jobhistory.done-dir
* mapreduce.jobhistory.cleaner.enable
* mapreduce.jobhistory.cleaner.interval-ms
* mapreduce.jobhistory.max-age-ms


.. code-block:: bash

    /etc/init.d # hdfs dfs -ls /tmp/hadoop-yarn/staging/history
    Found 2 items
    drwxrwx--x   - mapred mapred          0 2014-12-16 18:05 /tmp/hadoop-yarn/staging/history/done
    drwxrwxrwt   - mapred mapred          0 2014-12-16 18:02 /tmp/hadoop-yarn/staging/history/done_intermediate


References
==========

* https://hadoop.apache.org/docs/r3.0.0/hadoop-mapreduce-client/hadoop-mapreduce-client-core/mapred-default.xml
