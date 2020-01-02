Troubleshooting: Kudu Disk issue
################################

Case 1: Take out a removed disk from kudu pool
==========================================

* remove disk from kudu-tserver config
* update kudu-tserver pool

.. code-block:: bash

    # the user has to be kudu
    $ su kudu
    $ kudu fs update_dirs --force -fs_wal_dir=/data0/kudu/tserver \
    --fs_data_dirs=/data0/kudu/tserver,/data1/kudu/tserver,/data2/kudu/tserver,/data3/kudu/tserver,/data4/kudu/tserver,/data5/kudu/tserver,/data6/kudu/tserver,/data7/kudu/tserver,/data8/kudu/tserver,/data9/kudu/tserver

* restart kudu-tserver


Case 2: Re-build (bad) directory
==============================

* re-create dir

.. code-block:: bash

    rm -rf /data6/kudu/;mkdir /data6/kudu;chown kudu:kudu /data6/kudu;ls -al /data6;ls -al /data6/kudu/


* re-create kudu filesystem(FS)

.. code-block:: bash

    # the user has to be kudu
    $ su kudu
    $ kudu fs update_dirs --force -fs_wal_dir=/data0/kudu/tserver \
    --fs_data_dirs=/data0/kudu/tserver,/data1/kudu/tserver,/data2/kudu/tserver,/data3/kudu/tserver,/data4/kudu/tserver,/data5/kudu/tserver,/data6/kudu/tserver,/data7/kudu/tserver,/data8/kudu/tserver,/data9/kudu/tserver


* restart kudu-tserver
