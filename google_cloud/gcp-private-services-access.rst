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

    # show IP range used for VPC peering
    $ gcloud compute addresses list --global --filter="purpose=VPC_PEERING"
    NAME                                               ADDRESS/RANGE  TYPE      PURPOSE      NETWORK       REGION  SUBNET  STATUS
    vpcn-prod-central-peering-private-services-access  10.2.0.0/18   INTERNAL  VPC_PEERING  vpcn-central                  RESERVED

    # show all peering.
    $ gcloud compute networks peerings list
    NAME                                                          NETWORK         PEER_PROJECT                  PEER_NETWORK       AUTO_CREATE_ROUTES  STATE   STATE_DETAILS
    redis-peer-88258322706                                        vpcn-central    b93fa6acd2c17ef5f-tp          vpcn-central       True                ACTIVE  [2020-02-21T13:43:30.435-08:00]: Connected.
    servicenetworking-googleapis-com                              vpcn-central    y2bac6ad8d92c64b8-tp          servicenetworking  True                ACTIVE  [2020-03-05T14:06:43.315-08:00]: Connected.


References
==========

* https://cloud.google.com/vpc/docs/configure-private-services-access
