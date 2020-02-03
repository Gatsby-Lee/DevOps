Diagnose Filesystem
###################

Troubleshooting 1: 2020-02-02
=============================

Story
-----

* CentOS 6.10, Hadoop3.0, Ext4
* While upgrading to Hadoop 3.0 from Hadoop 2.6.x, Hadoop upgraded HDFS blocks.
* In the middle of operration, stopped namenode and datanode.
* after that, one of nodes started logging exceptions like below with three volumes

.. code-block:: bash

    # in datanode log file
    # /data6, /data2, /data3
    du: cannot access /data6/hadoop/hdfs/data/current/BP-2016402303-97.64.80.10-1417763269460/previous.tmp/finalized/subdir78/subdir204/blk_1297009743_223559395.meta': Input/output error
    du: cannot access /data6/hadoop/hdfs/data/current/BP-2016402303-97.64.80.10-1417763269460/previous.tmp/finalized/subdir75/subdir180/blk_1296807082_223356728.meta': Input/output error

    # /var/log/dmesg
    EXT4-fs (sda1): mounted filesystem with ordered data mode. Opts:
    EXT4-fs (dm-2): mounted filesystem with ordered data mode. Opts:
    EXT4-fs (sdc1): recovery complete
    EXT4-fs (sdc1): mounted filesystem with ordered data mode. Opts:
    EXT4-fs (sde1): recovery complete
    EXT4-fs (sde1): mounted filesystem with ordered data mode. Opts:
    EXT4-fs (sdd1): warning: mounting fs with errors, running e2fsck is recommended
    EXT4-fs (sdd1): recovery complete
    EXT4-fs (sdd1): mounted filesystem with ordered data mode. Opts:
    EXT4-fs (sdg1): warning: maximal mount count reached, running e2fsck is recommended
    EXT4-fs (sdg1): recovery complete
    EXT4-fs (sdg1): mounted filesystem with ordered data mode. Opts:
    EXT4-fs (sdf1): mounted filesystem with ordered data mode. Opts:
    EXT4-fs (sdh1): warning: mounting fs with errors, running e2fsck is recommended
    EXT4-fs (sdh1): recovery complete
    EXT4-fs (sdh1): mounted filesystem with ordered data mode. Opts:
    EXT4-fs (sdi1): warning: mounting fs with errors, running e2fsck is recommended
    EXT4-fs (sdi1): recovery complete
    EXT4-fs (sdi1): mounted filesystem with ordered data mode. Opts:
    EXT4-fs (sdj1): recovery complete
    EXT4-fs (sdj1): mounted filesystem with ordered data mode. Opts:
    EXT4-fs (sdk1): recovery complete
    EXT4-fs (sdk1): mounted filesystem with ordered data mode. Opts:
    EXT4-fs (sdb1): recovery complete
    EXT4-fs (sdb1): mounted filesystem with ordered data mode. Opts:

    # Checked device/partition/Filesystem
    $ lsblk -o NAME,FSTYPE,MOUNTPOINT
    NAME                       FSTYPE      MOUNTPOINT
    sdb
    └─sdb1                     ext4        /data9
    sdd
    └─sdd1                     ext4        /data2
    sdc
    └─sdc1                     ext4        /data0
    sde
    └─sde1                     ext4        /data1
    sdf
    └─sdf1                     ext4        /data4
    sdg
    └─sdg1                     ext4        /data3
    sdh
    └─sdh1                     ext4        /data5
    sdi
    └─sdi1                     ext4        /data6
    sdj
    └─sdj1                     ext4        /data7
    sdk
    └─sdk1                     ext4        /data8
    sda
    ├─sda1                     ext4        /boot
    └─sda2                     LVM2_member
    ├─vg_srv7-lv_root (dm-0) ext4        /
    ├─vg_srv7-lv_swap (dm-1) swap        [SWAP]
    └─vg_srv7-lv_home (dm-2) ext4        /home


Actions
-------

.. code-block:: bash

    # checked/fixed filesystem
    # DO NOT run e2fsck or fsck on mounted filesystems,
    unmount /data2
    fsck.ext4 -f -C 0 /dev/sdd1

    # after fixing all three volumes - checked /etc/fstab
    mount -a


References
----------

* https://linux.101hacks.com/unix/e2fsck/
* https://www.tecmint.com/manage-ext2-ext3-and-ext4-health-in-linux/
