Google Cloud Kubernetes
=======================

Get access to cluster for kubectl
---------------------------------

.. code-block:: bash

  export my_zone=us-central1-a
  export my_cluster=standard-cluster-1
  source <(kubectl completion bash)
  gcloud container clusters get-credentials $my_cluster --zone $my_zone
