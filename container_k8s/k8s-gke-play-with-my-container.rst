Google Kubernetes - My Container
================================

Start Cloud Shell Terminal
--------------------------

.. code-block:: bash

    $ gcloud auth list

    # define default timezone.
    $ gcloud config set compute/zone us-central1-a


Create Kubernetes Cluster
-------------------------

The scopes argument provides access to project hosting and Google Cloud Storage APIs that you'll use later.

.. code-block:: bash

    gcloud container clusters create hello-world --num-nodes 2


https://kubernetes.io/docs/reference/kubectl/overview/

.. code-block:: bash

    kubectl cluster-info
    kubectl config view
    kubectl get events
    kubectl logs <pod-name>


Create pod
----------

A Kubernetes pod is a group of containers tied together for administration and networking purposes.

It can contain single or multiple containers.

.. code-block:: bash

    # project_id can be found from `gcloud config list`
    # export PROJECT_ID=<project_id>
    $ kubectl run hello-world --image=gcr.io/$PROJECT_ID/py-web-server:v1 --port=5000
    deployment.apps/hello-world created

    $ kubectl get deployments
    NAME          DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
    hello-world   1         1         1            1           2m1s

    $ kubectl get pods
    NAME                           READY   STATUS    RESTARTS   AGE
    hello-world-85b5d848d9-wjj72   1/1     Running   0          98s

    $ kubectl get service
    NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
    kubernetes   ClusterIP   10.0.0.1     <none>        443/TCP   10m

    $ kubectl describe deployment hello-world
    Name:                   hello-world
    Namespace:              default
    CreationTimestamp:      Sat, 20 Jul 2019 21:49:38 -0700
    Labels:                 run=hello-world
    Annotations:            deployment.kubernetes.io/revision: 1
    Selector:               run=hello-world
    Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
    StrategyType:           RollingUpdate
    MinReadySeconds:        0
    RollingUpdateStrategy:  25% max unavailable, 25% max surge
    Pod Template:
    Labels:  run=hello-world
    Containers:
    hello-world:
        Image:        gcr.io/hello-world-project/py-web-server:v1
        Port:         5000/TCP
        Host Port:    0/TCP
        Environment:  <none>
        Mounts:       <none>
    Volumes:        <none>
    Conditions:
    Type           Status  Reason
    ----           ------  ------
    Available      True    MinimumReplicasAvailable
    Progressing    True    NewReplicaSetAvailable
    OldReplicaSets:  <none>
    NewReplicaSet:   hello-world-85b5d848d9 (1/1 replicas created)
    Events:
    Type    Reason             Age   From                   Message
    ----    ------             ----  ----                   -------
    Normal  ScalingReplicaSet  26s   deployment-controller  Scaled up replica set hello-world-85b5d848d9 to 1


Interact with pod without exposing to public
--------------------------------------------

port-forward / curl request

.. code-block:: bash

    $ kubectl get pods
    NAME                           READY   STATUS    RESTARTS   AGE
    hello-world-85b5d848d9-wjj72   1/1     Running   0          6m34s

    $ kubectl port-forward hello-world-85b5d848d9-wjj72 5000:5000
    Forwarding from 127.0.0.1:5000 -> 5000

    $ curl http://127.0.0.1:5000
    Flask Dockerize


Allow external traffic
----------------------

By default, the pod is only accessible by its internal IP within the cluster.
In order to make the hello-world container accessible from outside the Kubernetes virtual network,
you have to expose the pod as a Kubernetes service.

Expose the pod to the public internet with the `kubectl expose `command combined with the --type="LoadBalancer" flag.
This flag is required for the creation of an externally accessible IP:

The flag used in this command specifies that are using the load-balancer provided by
the underlying infrastructure (in this case the Compute Engine load balancer).

Note that you expose the deployment, and not the pod, directly.
This will cause the resulting service to load balance traffic across all pods managed by the deployment

The Kubernetes master creates the load balancer and related Compute Engine forwarding rules,
target pools, and firewall rules to make the service fully accessible from outside of Google Cloud Platform.

.. code-block:: bash

    # expose deployment not pod directly.
    $ kubectl expose deployment hello-world --type="LoadBalancer"
    service/hello-world exposed

    # CLUSTER-IP is the internal IP that is only visible inside your cloud virtual network
    # the EXTERNAL-IP is the external load-balanced IP.
    $ $ kubectl get service
    NAME          TYPE           CLUSTER-IP    EXTERNAL-IP    PORT(S)          AGE
    hello-world   LoadBalancer   10.0.14.121   34.68.48.111   5000:31355/TCP   8m47s
    kubernetes    ClusterIP      10.0.0.1      <none>         443/TCP          18m


Scale up service
----------------

.. code-block:: bash

    $ kubectl get deployment
    NAME          DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
    hello-world   1         1         1            1           17m

    $ kubectl scale deployment hello-world --replicas=3
    deployment.extensions/hello-world scaled

    $ kubectl get deployment
    NAME          DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
    hello-world   3         3         3            3           18m

    $ kubectl get pods
    NAME                           READY   STATUS    RESTARTS   AGE
    hello-world-85b5d848d9-kjl92   1/1     Running   0          67s
    hello-world-85b5d848d9-wjj72   1/1     Running   0          19m
    hello-world-85b5d848d9-x7759   1/1     Running   0          67s
