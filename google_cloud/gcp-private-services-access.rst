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


Check VPC_PEERING
=================

.. code-block:: bash

    $ gcloud compute addresses list --global --filter="purpose=VPC_PEERING"
    NAME                                               ADDRESS/RANGE  TYPE      PURPOSE      NETWORK       REGION  SUBNET  STATUS
    vpcn-prod-central-peering-private-services-access  10.2.0.0/18   INTERNAL  VPC_PEERING  vpcn-central                  RESERVED

References
==========

* https://cloud.google.com/vpc/docs/configure-private-services-access
