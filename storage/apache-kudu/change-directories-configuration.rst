Changing Directory Configurations
================================

Background
----------

KUDU tablet server can be configured to store data in multiple directories on different devices.


Issuse 1: One of device is BAD
------------------------------

A disk failure occurs that does not lead to a crash. (Based `documetation <https://kudu.apache.org/docs/administration.html#disk_failure_recovery>`_)
As long as the disk(device) doesn't have WAL or Metadata directory.

NOTE: When a disk failure occurs that does not lead to a crash, Kudu will stop using the affected directory, shut down tablets with blocks on the affected directories, and automatically re-replicate the affected tablets to other tablet servers. The affected server will remain alive and print messages to the log indicating the disk failure, for example:

.. code-block::

  E1205 19:06:24.163748 27115 data_dirs.cc:1011] Directory /data/8/kudu/data marked as failed
  E1205 19:06:30.324795 27064 log_block_manager.cc:1822] Not using report from /data/8/kudu/data: IO error: Could not open container 0a6283cab82d4e75848f49772d2638fe: /data/8/kudu/data/0a6283cab82d4e75848f49772d2638fe.metadata: Read-only file system (error 30)
  E1205 19:06:33.564638 27220 ts_tablet_manager.cc:946] T 4957808439314e0d97795c1394348d80 P 70f7ee61ead54b1885d819f354eb3405: aborting tablet bootstrap: tablet has data in a failed directory


Note that existing tablets will not stripe to the restored disk, but any new tablets will stripe to the restored disk.

My case was
* device is already unmounted
* KUDU Tablet Server has unmounted device in --fs_data_dirs
* KUDU Tablet Server fails to start since it can't find the unmounted device.

Action:

1. Removed the umounted device from --fs_data_dirs
2. By using `kudu fs update_dirs` command, updated --fs_data_dirs like below

.. code-block:: bash

  kudu fs update_dirs --force -fs_wal_dir=/data0/kudu/tserver --fs_data_dirs=/data0/kudu/tserver,/data1/kudu/tserver,/data2/kudu/tserver,/data3/kudu/tserver,/data4/kudu/tserver,/data6/kudu/tserver,/data7/kudu/tserver,/data8/kudu/tserver,/data9/kudu/tserver

3. service kudu-tserver restart


Directory Configurations
------------------------

* --fs_wal_dir
* --fs_metadata_dir
* --fs_data_dirs


References
----------

* https://kudu.apache.org/docs/administration.html#change_dir_config
* https://kudu.apache.org/docs/configuration.html#directory_configuration
* https://kudu.apache.org/docs/administration.html#disk_failure_recovery
