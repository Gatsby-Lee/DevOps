GCP gcloud cli cheatsheet
=========================

ref: https://cloud.google.com/sdk/gcloud/reference/

gcloud config

.. code-block:: bash

  $ gcloud config list
  [core]
  account = hello@test.com
  disable_usage_reporting = True
  project = hello-test-development1

gcloud compute

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
