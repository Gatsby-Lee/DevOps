Setup 6TB Disk
##############

References
----------

* https://www.cyberciti.biz/tips/fdisk-unable-to-create-partition-greater-2tb.html

* new 6TB Toshiba disk
* has to use parted
* has to change label

.. code-block:: bash

    # /dev/sdb is new one
    [root@test:~/]$ lsblk
    NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
    sda      8:0    0  477G  0 disk
    ├─sda1   8:1    0    1G  0 part /boot
    ├─sda2   8:2    0    8G  0 part [SWAP]
    └─sda3   8:3    0  468G  0 part /
    sdb      8:16   0  5.5T  0 disk

    [root@test:~/]$ parted /dev/sdb
    GNU Parted 2.1
    Using /dev/sdb
    Welcome to GNU Parted! Type 'help' to view a list of commands.
    (parted) mklabel gpt
    (parted) mkpart primary ext4 1 -1
    (parted) print
    Model: ATA TOSHIBA HDWE160 (scsi)
    Disk /dev/sdb: 6001GB
    Sector size (logical/physical): 512B/4096B
    Partition Table: gpt

    Number  Start   End     Size    File system  Name     Flags
    1      1049kB  6001GB  6001GB               primary

    (parted) quit
    Information: You may need to update /etc/fstab.

    [root@test:~/]$ lsblk
    NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
    sda      8:0    0  477G  0 disk
    ├─sda1   8:1    0    1G  0 part /boot
    ├─sda2   8:2    0    8G  0 part [SWAP]
    └─sda3   8:3    0  468G  0 part /
    sdb      8:16   0  5.5T  0 disk
    └─sdb1   8:17   0  5.5T  0 part

    [root@test:~/]$ mkfs.ext4 /dev/sdb1
    mke2fs 1.41.12 (17-May-2010)
    Filesystem label=
    OS type: Linux
    Block size=4096 (log=2)
    Fragment size=4096 (log=2)
    Stride=1 blocks, Stripe width=0 blocks
    366288896 inodes, 1465130240 blocks
    73256512 blocks (5.00%) reserved for the super user
    First data block=0
    Maximum filesystem blocks=4294967296
    44713 block groups
    32768 blocks per group, 32768 fragments per group
    8192 inodes per group
    Superblock backups stored on blocks:
        32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
        4096000, 7962624, 11239424, 20480000, 23887872, 71663616, 78675968,
        102400000, 214990848, 512000000, 550731776, 644972544

    Writing inode tables: done
    Creating journal (32768 blocks): done
    Writing superblocks and filesystem accounting information: done

    This filesystem will be automatically checked every 27 mounts or
    180 days, whichever comes first.  Use tune2fs -c or -i to override.
