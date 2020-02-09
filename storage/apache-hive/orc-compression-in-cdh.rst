ORC compression in CDH
######################

ORC Compression in CDH 5.16.2
=============================

.. code-block: bash

    # Original
    hive> dfs -du -s -h /user/hive/external_warehouse/sample_rcfile_0/yearmonth=201912;
    130.1 G  390.4 G  /user/hive/external_warehouse/sample_rcfile_0/yearmonth=201912

    # no compression ( default )
    hive> dfs -du -s -h /user/hive/warehouse/sample_201912_orc_0;
    70.8 G  212.4 G  /user/hive/warehouse/sample_201912_orc_0

    # zlib
    SET hive.exec.compress.output=true;
    SET orc.compress=ZLIB;
    hive> dfs -du -s -h /user/hive/external_warehouse/sample_201912_orc_0;
    70.9 G  212.6 G  /user/hive/external_warehouse/sample_201912_orc_0

    # snappy
    SET hive.exec.compress.output=true;
    SET orc.compress=SNAPPY;
    hive> dfs -du -s -h /user/hive/external_warehouse/sample_201912_orc_0;
    99.3 G  297.9 G  /user/hive/external_warehouse/sample_201912_orc_0


ORC File Format
===============

* https://cwiki.apache.org/confluence/display/Hive/LanguageManual+ORC
* https://towardsdatascience.com/new-in-hadoop-you-should-know-the-various-file-format-in-hadoop-4fcdfa25d42b
