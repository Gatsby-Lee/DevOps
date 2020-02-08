ORC compression in CDH
######################

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
