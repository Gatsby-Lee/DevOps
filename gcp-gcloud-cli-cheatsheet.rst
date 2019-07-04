GCP gcloud cli cheatsheet
=========================

ref: https://cloud.google.com/sdk/gcloud/reference/


gcloud config
--------------

.. code-block:: bash

  $ gcloud config list
  [core]
  account = hello@test.com
  disable_usage_reporting = True
  project = hello-test-development1

  $ gcloud config set project hello-test-development2
  Updated property [core/project].

  $ gcloud config set compute/zone us-central1-c
  Updated property [compute/zone].
  $ gcloud config list
  [compute]
  zone = us-central1-c
  [core]
  account = hello@test.com
  disable_usage_reporting = True
  project = hello-test-development2


Compute Engines - Images
------------------------

.. code-block:: bash

  $ gcloud compute images list --filter="centos"
  NAME                PROJECT       FAMILY    DEPRECATED  STATUS
  centos-6-v20190619  centos-cloud  centos-6              READY
  centos-7-v20190619  centos-cloud  centos-7              READY

Compute Engines - Firewall-rules
--------------------------------

.. code-block:: bash

  $ gcloud compute firewall-rules list
  NAME                    NETWORK  DIRECTION  PRIORITY  ALLOW                         DENY  DISABLED
  default-allow-icmp      default  INGRESS    65534     icmp                                False
  default-allow-internal  default  INGRESS    65534     tcp:0-65535,udp:0-65535,icmp        False
  default-allow-rdp       default  INGRESS    65534     tcp:3389                            False
  default-allow-ssh       default  INGRESS    65534     tcp:22                              False

  $ gcloud compute firewall-rules delete default-allow-ssh

  $ gcloud compute firewall-rules create default-allow-ssh \
  --network=default --allow tcp:22 --priority 65534


Compute Engines - VM
--------------------

.. code-block:: bash

  $ gcloud compute instances create "my-vm1" \
  --machine-type="n1-standard-1" \
  --image-project="centos-cloud" \
  --image="centos-7-v20190619"
  Created [https://www.googleapis.com/compute/v1/projects/hello-test-development2/zones/us-central1-c/instances/my-vm1].
  NAME    ZONE           MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP     STATUS
  my-vm1  us-central1-c  n1-standard-1               10.128.0.2   35.232.238.124  RUNNING

  $

.. code-block:: bash

  $ gcloud compute zones list
  
  $ gcloud compute networks list
  NAME            SUBNET_MODE  BGP_ROUTING_MODE  IPV4_RANGE  GATEWAY_IPV4
  default         AUTO         REGIONAL
  vpcn-central    CUSTOM       REGIONAL
  
  

Memorystore
-----------

.. code-block:: bash

  $ gcloud redis instances list --region us-central1
  INSTANCE_NAME       VERSION    REGION       TIER   SIZE_GB  HOST      PORT  NETWORK       RESERVED_IP  STATUS    CREATE_TIME
  test-memstore-1  REDIS_3_2  us-central1  BASIC  16       10.0.0.3  6379  vpcn-central  10.0.0.0/29  UPDATING  2019-02-05T21:09:37

  $ gcloud redis instances describe test-memstore-1 --region us-central1
  authorizedNetwork: projects/hello-test-development1/global/networks/vpcn-central
  createTime: '2019-02-05T21:09:37.527642370Z'
  currentLocationId: us-central1-f
  host: 10.0.0.3
  locationId: us-central1-f
  memorySizeGb: 16
  name: projects/hello-test-development1/locations/us-central1/instances/toolbox-memstore-1
  persistenceIamIdentity: serviceAccount:791848431720-compute@developer.gserviceaccount.com
  port: 6379
  redisVersion: REDIS_3_2
  reservedIpRange: 10.0.0.0/29
  state: UPDATING
  tier: BASIC
