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


Interface config file
---------------------

* ref: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/s1-networkscripts-interfaces
* /etc/sysconfig/network-scripts
* BOOTPROTO: none (for static) | bootp | dhcp
* ONBOOT: no | yes ( boot-time activaction )
* PEERDNS: no | yes ( modify /etc/resolv.conf
* NM_CONTROLLED: no | yes ( NetworkManager is permitted to configure this device )
