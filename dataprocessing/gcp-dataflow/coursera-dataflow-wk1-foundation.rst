What is Apache Beam?
====================

* A open source unified programming model to define
    these data-processing pipelines.
    - batch
    - streaming
* "Beam SDKs" is used to create pipelines in the programming language.
* Pipelines can be run "locally" or other "backend services"
* A "Runner" is used to execute pipelines on a backend services
* "Dataflow" is one of the runners available in Beam.


The Google Cloud runner: Dataflow
=================================

It includs "Resource Autoscaler" and "Dynamic Work Rebalancer"


Beam Portability
================

Apache Beam's vision
--------------------

Providing "comprehensive protability framework" for data processing pipelines.

* write once
* run it on the "execution engines" with minimal effort


Portability framework
---------------------

* "Language-agnostic" way to represent pipelines
* a set of "protocols" for executing pipelines
* interoperability layer = "Portability API"
* "Docker containerization" to customize your execution environment.


Benefits of portability
-----------------------

* "Every runner" works with "every language" ( Running pipelines authored in any SDK on any runner )
* Configurable, hermetic "worker environment"
* "Multi-language" pipelines
* "Cross-language" transforms
* Faster delivery of "new features"


Dataflow Runner v2
------------------

V2 has to be used to utilize Beam's portability

* More efficient and proable worker architecture
* Based on Aapache Beam portability framework
* Support for multi-language pipelines and custom containers


Container Environments
----------------------

* Containerized with Docker
* Per-operation execution environment
* Default environemnt per SDK
* Ahead-of-time installation
* Arbitrary dependencies
* Arbitrary customization


Custom container
----------------

* Apache Beam SDK version 2.25.0 or later is required.


Cross-language transforms
-------------------------

* Transforms can be "shared" among SDKs
* A "rich set of IOs" from Java is available everywhere.
* More libraries are available in the "language of your choice"


Separating Compute and Storage with Dataflow
============================================

Dataflow
--------

1. fully managed and auto-configured
2. Dataflow optimizes the graph execution
3. autoscaling in the middle of a pipeline job


Dataflow Shuffle Service
------------------------

* A "Shuffle" is a Dataflow base operation.
* A "Shuffle" is behind transforms such as GroupByKey, COGroupByKey, and Combine.
* Dataflow uses a "Shuffle" implementation that runs entirely on worker VM and consumers worker's resources like CPU, Memory, Persistent Disk Storage.
* Service-based Dataflow Shuffle feature is only available for batch pipelines. This moves the "Shuffle" operations out of the worker VMs.
    * Faster execution time of batch pipelines for most cases
    * Reduced resource consumtion in workers
    * Better "autoscaling" because workers don't need to hold suffled data and can therefore be sclaed down eariler.


Dataflow Streaming Engine
-------------------------

* Streaming Engine offloads the window state storage from the persistent disks attched to worker VMs, to backend service.
* Streaming Engine works best with smaller worker machine types like n1-standard-2 and doesn't require Persistent Disk beyond a smaller worker boot disk


Flexible Resources Scheduling ( FlexRS )
----------------------------------------

* Reduced batch processing costs because of:
    * Advanced "scheduling"
    * Dataflow Shuffle Service
    * Mix of preemptible and standard VMs
* Execution within 6 hours from job creation
* Suitable for workloads that are not time-critical
* Early validation run at job submission


IAM, Quotas, and Permissions
============================

* when a pipeline is submitted, it goes to
    * GCS bucket
    * Dataflow
        * validates and optmizes the submitted pipeline.
        * Provision VMs in your project to run the pipeline.
        * Deploy the pipeline code to VMs
        * Gather monitoring information for display


Three credentials
-----------------

* User roles
    * Dataflow Viewer
    * Dataflow Developer ( not able to submit a job )
    * Dataflow Admin

* Dataflow service account ( The Orchestrator )
    * Interacts between resource in project and Dataflow
    * Used for worker creation and monitoring
    * service-<project-id>@dataflow-service-producer-prod.iam.gserviceaccount.com
    * Assgned the Dataflow Service Agent role

* Controller service account
    * assigned to the compute engine VMs
    * by default, Compute Engine default service will be used. ( <project-id>-compute@developer.gserviceaccount.com )


Quotas
------

Persistent Disks - Batch Pipeline
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

* VM to PD ratio is 1:1 for Batch
* Size if Shuffle on VM: 250GB
* Size if Shuffle Service: 25GB


Persistent Disks - Streaming Pipeline
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

* a Fixed pool of PDs
* Each worker must have at least 1 persistent disk attached to it.
* The max PDs per VM is 15.
* Default size if shuffle on VM: 400GB
* Default size if Streaming Engine: 30GB
* Amount of disk allocated == Max number of workers
* max-num-workers flag is required for streaming with shuffle on VMs
* Max num of workers is 1000


Securtiy
========

Data locality
-------------

Ensuring all data and metadata stays in one region.


What is a regional endpoint?
>>>>>>>>>>>>>>>>>>>>>>>>>>>>

* Backend that deploys and controls your Dataflow workers
* Talks with the Dataflow service account in your project
* Stores and handles metadata about your Dataflow jobs


Why specify a regional endpoint?
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

* Securty and compliance ( like Bank )
* Minimize network latency and network transport costs


How to specify a regional endpoint?
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

* if no zone preference: --region=$REGION
* to specify zone: --region=$REGION --worker_zone=$ZONE
* run worker in a region with no regional endpoint: --region=$REGION --worker_region=$WORKER_REGION

    * This can create Network latency.
    * only metadata will be transferred.
    * application data will stay in the region.


Shared VPC
----------

Hosts and services

* Dataflow jobs can run in either VPC or Shared VPC
* Works for both default and custom VPC networks
* Number of VMs is constrained by subnet IP block size
* Dataflow service account needs Compute Network User role in host project.
* --network / --subnetwork


Private IPs
-----------

No external IPs

* Secure your data processing infrastructure
* Pipeline can't access the internet and other Cloud networks
* either --network or --subnetwork AND --no_use_public_ips


CMEK
----

it stands for "Customer manged encryption Key"

What is it?
>>>>>>>>>>>

* Where data is stored:

    * Persistent Disk
    * Storage buckets
    * Dataflow Shuffle backend
    * Streaming Engine backend

* Data keys in grouping operations are decrypted using CMEK key.
* Job Metadata is protected by Google-mananged key encryption.
* Add Cloud KMS CryptoKey Encrypter/Decrypter role to Dataflow service account and Controller Agent service account
* --temp_location and --dataflow_kms_key
    * global / multi-regional KMS key won't work.



Experiment
==========


.. code-block:: bash

    gcloud projects get-iam-policy $PROJECT  --format='table(bindings.role)' --flatten="bindings[].members" --filter="bindings.members:$USER_EMAIL"
    ROLE
    roles/dataflow.viewer
    roles/resourcemanager.projectIamAdmin
    roles/storage.admin
    roles/viewer

    gcloud projects add-iam-policy-binding $PROJECT --member=user:$USER_EMAIL --role=roles/dataflow.admin

    # in the virtualenv
    python3 -m pip install -q --upgrade pip setuptools wheel
    python3 -m pip install apache-beam[gcp]

    python3 -m apache_beam.examples.wordcount \
    --input gs://dataflow-samples/shakespeare/kinglear.txt \
    --output gs://$PROJECT/results/outputs --runner DataflowRunner  \
    --project $PROJECT --temp_location gs://$PROJECT/tmp/  \
    --region $REGION
