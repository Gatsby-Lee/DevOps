Google Private Services Access
##############################

`Private services access` is implemented as a '''VPC peering connection''' between your VPC network and the Google services Network.


Supported Google Managed Services
=================================

* Cloud SQL
* Cloud Memorystore


Connectivities
==============

* `On-prem` can access Google Managed services using Private Services Access through Google Interconnect or VPN.
* GKE-native ( not Route based ) can access it.


References
==========

* https://cloud.google.com/vpc/docs/configure-private-services-access
