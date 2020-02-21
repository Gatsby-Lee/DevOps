Play with GKE
=============

Create GKE cluster
------------------

.. code-block:: bash

  $ gcloud container clusters create webfrontend --zone "us-central1-f" --num-nodes 2
  Creating cluster webfrontend in us-central1-f... Cluster is being health-checked (master is healthy)...done.
  Created [https://container.googleapis.com/v1/projects/brightedge-gcp-development2/zones/us-central1-f/clusters/webfrontend].
  To inspect the contents of your cluster, go to: https://console.cloud.google.com/kubernetes/workload_/gcloud/us-central1-f/webfrontend?project=brightedge-gcp-development2
  kubeconfig entry generated for webfrontend.
  NAME         LOCATION       MASTER_VERSION  MASTER_IP       MACHINE_TYPE   NODE_VERSION   NUM_NODES  STATUS
  webfrontend  us-central1-f  1.12.8-gke.10   35.224.242.230  n1-standard-1  1.12.8-gke.10  2          RUNNING


In case kubectl doesn't work
----------------------------

It might be related to kubectl credential. https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl

.. code-block:: bash

  gcloud container clusters get-credentials <cluster_name>



Run nginx container
-------------------

.. code-block:: bash

  $ kubectl run nginx --image=nginx:latest

  $ kubectl get pods
  NAME                    READY   STATUS    RESTARTS   AGE
  nginx-cbc48fcd9-sqkvg   1/1     Running   0          120m

Expose nginx to external
------------------------

.. code-block:: bash

  $ kubectl expose deployment nginx --port 80 --type LoadBalancer
  service/nginx exposed

  # we can see that nginx get external ip and bind to port 80
  # you can visit external ip
  $ kubectl get services
  NAME         TYPE           CLUSTER-IP   EXTERNAL-IP     PORT(S)        AGE
  kubernetes   ClusterIP      10.0.0.1     <none>          443/TCP        139m
  nginx        LoadBalancer   10.0.3.144   34.66.254.169   80:32737/TCP   12m


Scale nginx service
-------------------

.. code-block:: bash

  $ kubectl scale deployment nginx --replicas 3
  deployment.extensions/nginx scaled

  # check running nginx service
  $ kubectl get pods
  NAME                    READY   STATUS    RESTARTS   AGE
  nginx-cbc48fcd9-kv4kp   1/1     Running   0          2m17s
  nginx-cbc48fcd9-qcmp5   1/1     Running   0          2m17s
  nginx-cbc48fcd9-sqkvg   1/1     Running   0          140m

  # confirm that nginx external-ip is not changed.
  $ kubectl get services
  NAME         TYPE           CLUSTER-IP   EXTERNAL-IP     PORT(S)        AGE
  kubernetes   ClusterIP      10.0.0.1     <none>          443/TCP        139m
  nginx        LoadBalancer   10.0.3.144   34.66.254.169   80:32737/TCP   12m


Delete GKE cluster
------------------

.. code-block:: bash

  $ gcloud container clusters delete webfrontend --zone "us-central1-f"

