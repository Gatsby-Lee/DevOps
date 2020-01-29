DNS resolver
############

How to prevent /etc/resolv.cfg to be updated
=============================================

* CentOS6.10

There can be multiple things that can update /etc/resolv.cfg

Actions
-------

1. NetworkManager ( disable service )
2. set `no` for NM_CONTROLLED in /etc/sysconfig/network-scripts/ifcfg-eth*
2. set `no` for PEERDNS in /etc/sysconfig/network-scripts/ifcfg-eth*

.. code-block:: bash

    [root@test:~/]$ grep BOOT /etc/sysconfig/network-scripts/ifcfg-eth*
    /etc/sysconfig/network-scripts/ifcfg-eth0:BOOTPROTO=none
    /etc/sysconfig/network-scripts/ifcfg-eth0:ONBOOT=yes
    /etc/sysconfig/network-scripts/ifcfg-eth1:BOOTPROTO=none
    /etc/sysconfig/network-scripts/ifcfg-eth1:ONBOOT=yes
    /etc/sysconfig/network-scripts/ifcfg-eth2:BOOTPROTO=dhcp
    /etc/sysconfig/network-scripts/ifcfg-eth2:ONBOOT=no
    /etc/sysconfig/network-scripts/ifcfg-eth3:BOOTPROTO=dhcp
    /etc/sysconfig/network-scripts/ifcfg-eth3:ONBOOT=no
    [root@test:~/]$ grep PEER /etc/sysconfig/network-scripts/ifcfg-eth*
    /etc/sysconfig/network-scripts/ifcfg-eth0:PEERDNS=no
    /etc/sysconfig/network-scripts/ifcfg-eth1:PEERDNS=no
    /etc/sysconfig/network-scripts/ifcfg-eth2:PEERDNS=yes
    /etc/sysconfig/network-scripts/ifcfg-eth3:PEERDNS=yes
    [root@test:~/]$ grep NM /etc/sysconfig/network-scripts/ifcfg-eth*
    /etc/sysconfig/network-scripts/ifcfg-eth0:NM_CONTROLLED=no
    /etc/sysconfig/network-scripts/ifcfg-eth1:NM_CONTROLLED=no
    /etc/sysconfig/network-scripts/ifcfg-eth2:NM_CONTROLLED=yes
    /etc/sysconfig/network-scripts/ifcfg-eth3:NM_CONTROLLED=yes


Interface config file
---------------------

* ref: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/s1-networkscripts-interfaces
* /etc/sysconfig/network-scripts
* BOOTPROTO: none (for static) | bootp | dhcp
* ONBOOT: no | yes ( boot-time activaction )
* PEERDNS: no | yes ( modify /etc/resolv.conf
* NM_CONTROLLED: no | yes ( NetworkManager is permitted to configure this device )
