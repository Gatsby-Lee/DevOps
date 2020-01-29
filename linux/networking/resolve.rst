DNS resolver
############

How to prevent /etc/resolve.cfg to be updated
=============================================

* CentOS6.10

There can be multiple things that can update /etc/resolve.cfg.

1. NetworkManager ( disable service )
2. set `no` for NM_CONTROLLED in /etc/sysconfig/network-scripts/ifcfg-eth*
2. set `no` for PEERDNS in /etc/sysconfig/network-scripts/ifcfg-eth*
