Google Kubernetes - Create Cluster
==================================

What to consider?
-----------------

* Max number of running pods in Node
* Types of Cluster


Type of Cluster
------------------------------------------------

Cluster type can't changed after created.

Ref:

* https://cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster
* https://cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters


* Zonal Cluster ( one master, single region, can be multiple compute zones )

    * DEFAULT: a single compute zone
    * multi-zone

* Regional Cluster ( three masters, single region, multiple compute zones )

    * https://cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters
    * By default, three masters, three nodes per zone, three compute zones ( can be customized )

.. code-block:: bash

    # default: three zones with three nodes each
    gcloud container clusters create test-regional-cluster --region us-east1

    # three zones with one node each
    gcloud container clusters create test-regional-cluster --region us-east1 \
        --num-nodes 1

    # one zone with one node
    gcloud container clusters create test-regional-cluster --num-nodes 1 \
        --region us-east1 --node-locations us-east1-b


* Private Cluster

