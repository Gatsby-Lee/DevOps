Google Composer
###############

Create composer environment
===========================

* service-account has to have necessary permissions. ( https://cloud.google.com/composer/docs/how-to/access-control )

.. code-block:: bash

    $ gcloud composer environments create blue-workflow \
        --location=us-east1 \
        --zone=us-east1-c \
        --labels=environment=production,pod=central,component=kwc \
        --python-version=3 \
        --service-account=composer@test-project.iam.gserviceaccount.com \
        --network=vpcn-central \
        --subnetwork=vpcsn-central-gke-nodes-us-east1 \
        --machine-type=n1-standard-1 \
        --disk-size=20 \
        --node-count=3 \
        --async

    $ gcloud composer environments list --locations=us-east1
    ┌───────────────┬──────────┬──────────┬──────────────────────────┐
    │      NAME     │ LOCATION │  STATE   │       CREATE_TIME        │
    ├───────────────┼──────────┼──────────┼──────────────────────────┤
    │ blue-workflow │ us-east1 │ CREATING │ 2020-03-06T16:54:30.953Z │
    └───────────────┴──────────┴──────────┴──────────────────────────┘


Create composer environment - GKE native
========================================

* https://cloud.google.com/composer/docs/how-to/managing/configuring-private-ip


.. code-block:: bash

    $ gcloud beta composer environments create blue-workflow \
        --location=us-east1 \
        --zone=us-east1-c \
        --labels=environment=production,pod=central,component=kwc \
        --airflow-version=1.10.6 \
        --python-version=3 \
        --service-account=composer@test-project.iam.gserviceaccount.com \
        --network=vpcn-central \
        --subnetwork=vpcsn-central-gke-nodes-us-east1 \
        --enable-ip-alias \
        --cluster-secondary-range-name=vpcsn-central-gke-pods-us-east1 \
        --services-secondary-range-name=vpcsn-central-gke-composer-service-us-east1 \
        --machine-type=n1-standard-1 \
        --disk-size=20 \
        --node-count=3 \
        --async


Show details about composer environment
=======================================

.. code-block:: bash

    $ gcloud beta composer environments describe blue-workflow --location=us-east1
    config:
    airflowUri: https://f5d24fa6bb2c4fbe8-tp.appspot.com
    dagGcsPrefix: gs://us-east1-blue-workflow-753f6fc3-bucket/dags
    gkeCluster: projects/test-project/zones/us-east1-c/clusters/us-east1-blue-workflow-753f6fc3-gke
    nodeConfig:
        diskSizeGb: 20
        ipAllocationPolicy:
        clusterSecondaryRangeName: vpcsn-central-gke-pods-us-east1
        servicesSecondaryRangeName: vpcsn-central-gke-composer-service-us-east1
        useIpAliases: true
        location: projects/test-project/zones/us-east1-c
        machineType: projects/test-project/zones/us-east1-c/machineTypes/n1-standard-1
        network: projects/test-project/global/networks/vpcn-central
        oauthScopes:
        - https://www.googleapis.com/auth/cloud-platform
        serviceAccount: composer@test-project.iam.gserviceaccount.com
        subnetwork: projects/test-project/regions/us-east1/subnetworks/vpcsn-central-gke-nodes-us-east1
    nodeCount: 3
    privateEnvironmentConfig:
        privateClusterConfig: {}
    softwareConfig:
        imageVersion: composer-1.9.2-airflow-1.10.2
        pythonVersion: '3'
    webServerNetworkAccessControl:
        allowedIpRanges:
        - description: Allows access from all IPv4 addresses (default value)
        value: 0.0.0.0/0
        - description: Allows access from all IPv6 addresses (default value)
        value: ::0/0
    createTime: '2020-03-12T19:38:18.606Z'
    labels:
    component: kwc
    environment: production
    pod: central
    name: projects/test-project/locations/us-east1/environments/blue-workflow
    state: RUNNING
    updateTime: '2020-03-12T19:55:20.874Z'
    uuid: 1de2cdac-f22b-46f9-a1f0-61d851218d24


Add/Create connections into Airflow by gcloud
=============================================

* https://cloud.google.com/sdk/gcloud/reference/beta/composer/environments/run


Redis Connection
----------------

.. code-block:: bash

    gcloud composer environments run hello-composer \
        --location=us-east1 \
        connections -- --add \
        --conn_type=Redis \
        --conn_id="redis_connection_id" \
        --conn_host="redis.test.com" \
        --conn_password="hello" \
        --conn_port=2222 \
        --conn_extra="{\"db\":10}"


MySQL Connection
----------------

.. code-block:: bash

    gcloud composer environments run hello-composer \
        --location=us-east1 \
        connections -- --add \
        --conn_type=mysql \
        --conn_id="_db_test" \
        --conn_host="mysql.test.com" \
        --conn_port=3306 \
        --conn_login="yo" \
        --conn_password="mypassword" \
        --conn_schema="database-name"


Add/Create variables into Airflow by gcloud
===========================================

* https://airflow.apache.org/docs/stable/cli.html#variables


Add/Create one
--------------

.. code-block:: bash

    gcloud composer environments run hello-composer \
        --location=us-east1 \
        variables -- --set active_pods "[1,2,3]"

    gcloud composer environments run hello-composer \
        --location=us-east1 \
        variables -- --delete active_pods


Import variables in JSON
------------------------

* https://stackoverflow.com/questions/54237270/import-variables-using-json-file-in-google-cloud-composer

.. code-block:: bash

    gcloud composer environments storage data import --source=airflow_variables.json \
        --environment=$(WORKFLOW) --location=$(LOCATION)

    gcloud composer environments run $(WORKFLOW) \
        --location=$(LOCATION) \
        variables -- --import /home/airflow/gcs/data/airflow_variables.json


Add/Create pool into Airflow by gcloud
===========================================

* airflow_pools.json content

.. code-block:: json

{
  "_db1": { "slots": 2, "description": "" },
  "_db2": { "slots": 2, "description": "" }
}


.. code-block:: bash

    gcloud composer environments storage data import --source=airflow_pools.json \
    --environment=$(WORKFLOW) --location=$(LOCATION)

    gcloud composer environments run $(WORKFLOW) \
    --location=$(LOCATION) \
    pool -- --import /home/airflow/gcs/data/airflow_pools.json


References
==========

* https://cloud.google.com/sdk/gcloud/reference/beta/composer/environments/storage
* https://stackoverflow.com/questions/57558319/writing-and-importing-custom-plugins-in-airflow
