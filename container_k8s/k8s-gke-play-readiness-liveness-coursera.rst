Google Kubernetes - Monitoring and Health Checks - Coursera
===========================================================


Start Cloud Shell Terminal
--------------------------

.. code-block:: bash

    $ gcloud auth list

    # define default timezone.
    $ gcloud config set compute/zone us-central1-a


Launch Kubernetes Cluster
-------------------------

Launch cluster
^^^^^^^^^^^^^^

The scopes argument provides access to project hosting and Google Cloud Storage APIs that you'll use later.

.. code-block:: bash

    gcloud container clusters create bootcamp --num-nodes 1 --scopes "https://www.googleapis.com/auth/projecthosting,storage-rw"



Prepare Sample Code
-------------------

Step 1: Clone Sample Code Repo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    git clone https://github.com/Gatsby-Lee/orchestrate-with-kubernetes


Kubernetes supports monitoring applications in the form of readiness and liveness probes. Health checks can be performed on each container in a pod. Readiness probes indicate when a pod is "ready" to serve traffic. Liveness probes indicate whether a container is "alive." If a liveness probe fails multiple times, the container is restarted. Liveness probes that continue to fail cause a pod to enter a crash loop. If a readiness check fails, the container is marked as not ready and is removed from any load balancers.


Step 2: Explore pod configuration file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ cat orchestrate-with-kubernetes/kubernetes/pods/healthy-monolith.yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: "healthy-monolith"
      labels:
        app: monolith
    spec:
      containers:
        - name: monolith
          image: kelseyhightower/monolith:1.0.0
          ports:
            - name: http
              containerPort: 80
            - name: health
              containerPort: 81
          resources:
            limits:
              cpu: 0.2
              memory: "10Mi"
          livenessProbe:
            httpGet:
              path: /healthz
              port: 81
              scheme: HTTP
            initialDelaySeconds: 5
            periodSeconds: 15
            timeoutSeconds: 5
          readinessProbe:
            httpGet:
              path: /readiness
              port: 81
              scheme: HTTP
            initialDelaySeconds: 5
            timeoutSeconds: 1



Step 3: Create pod with configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ kubectl create -f orchestrate-with-kubernetes/kubernetes/pods/healthy-monolith.yaml

    $ kubectl get pods
    NAME               READY   STATUS    RESTARTS   AGE
    healthy-monolith   1/1     Running   0          58s


Pods are not marked ready until the readiness probe returns an HTTP 200 response. Use the kubectl describe command to view details for the healthy-monolith pod.

.. code-block:: bash

    $ kubectl describe pod healthy-monolith


Readiness Probes
----------------

See how Kubernetes responds to failed readiness probes. The monolith container supports the ability to force failures of its readiness and liveness probes. This enables you to simulate failures for the healthy-monolith pod.


Step 1: forward a local port
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    # On terminal 2, to the health port of the healthy-monolith pod.
    $ kubectl port-forward healthy-monolith 10081:81


Step 2: Force container readiness probe to fail
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    # Use the curl command in terminal 1 to toggle the readiness probe status.
    # Note that this command does not show any output.
    $ curl http://127.0.0.1:10081/readiness/status

    # Get the status of the healthy-monolith pod using the kubectl get pods -w command.
    $ $  kubectl get pods healthy-monolith -w
    NAME               READY   STATUS    RESTARTS   AGE
    healthy-monolith   1/1     Running   0          69s
    healthy-monolith   0/1     Running   0          83s

    # Details about the failing readiness probe.
    # Notice the events history for the healthy-monolith pod report details about failing readiness probes.
    $ kubectl describe pods healthy-monolith
    Name:               healthy-monolith
    Namespace:          default
    Priority:           0
    PriorityClassName:  <none>
    Node:               gke-bootcamp-default-pool-d6f7288a-pxpg/10.128.0.2
    Start Time:         Sat, 13 Jul 2019 14:48:08 -0700
    Labels:             app=monolith
    Annotations:        <none>
    Status:             Running
    IP:                 10.48.0.7
    Containers:
      monolith:
        Container ID:   docker://c357344f4aa69f7a711c1805a0986c0854e0b5e0a2e8d414385a18e2d5f6ab28
        Image:          kelseyhightower/monolith:1.0.0
        Image ID:       docker-pullable://kelseyhightower/monolith@sha256:72c3f41b6b01c21d9fdd2f45a89c6e5d59b8299b52d7dd0c9491745e73db3a35
        Ports:          80/TCP, 81/TCP
        Host Ports:     0/TCP, 0/TCP
        State:          Running
          Started:      Sat, 13 Jul 2019 14:48:10 -0700
        Ready:          False
        Restart Count:  0
        Limits:
          cpu:     200m
          memory:  10Mi
        Requests:
          cpu:        200m
          memory:     10Mi
        Liveness:     http-get http://:81/healthz delay=5s timeout=5s period=15s #success=1 #failure=3
        Readiness:    http-get http://:81/readiness delay=5s timeout=1s period=10s #success=1 #failure=3
        Environment:  <none>
        Mounts:
          /var/run/secrets/kubernetes.io/serviceaccount from default-token-vw6s6 (ro)
    Conditions:
      Type              Status
      Initialized       True
      Ready             False
      ContainersReady   False
      PodScheduled      True
    Volumes:
      default-token-vw6s6:
        Type:        Secret (a volume populated by a Secret)
        SecretName:  default-token-vw6s6
        Optional:    false
    QoS Class:       Guaranteed
    Node-Selectors:  <none>
    Tolerations:     node.kubernetes.io/not-ready:NoExecute for 300s
                     node.kubernetes.io/unreachable:NoExecute for 300s
    Events:
      Type     Reason     Age                 From                                              Message
      ----     ------     ----                ----                                              -------
      Normal   Scheduled  6m47s               default-scheduler                                 Successfully assigned default/healthy-monolith to gke-bootcamp-default-pool-d6f7288a-pxpg
      Normal   Pulling    6m46s               kubelet, gke-bootcamp-default-pool-d6f7288a-pxpg  pulling image "kelseyhightower/monolith:1.0.0"
      Normal   Pulled     6m45s               kubelet, gke-bootcamp-default-pool-d6f7288a-pxpg  Successfully pulled image "kelseyhightower/monolith:1.0.0"
      Normal   Created    6m45s               kubelet, gke-bootcamp-default-pool-d6f7288a-pxpg  Created container
      Normal   Started    6m45s               kubelet, gke-bootcamp-default-pool-d6f7288a-pxpg  Started container
      Warning  Unhealthy  1s (x13 over 2m1s)  kubelet, gke-bootcamp-default-pool-d6f7288a-pxpg  Readiness probe failed: HTTP probe failed with statuscode: 503


Step 3: Force container readiness probe to pass
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    # To force the monolith container readiness probe to pass, toggle the readiness probe status by using the curl command.
    $ curl http://127.0.0.1:10081/readiness/status

    # Wait about 15 seconds and get the status of the healthy-monolith pod using the kubectl get pods command.
    $ kubectl get pods healthy-monolith
    NAME               READY   STATUS    RESTARTS   AGE
    healthy-monolith   1/1     Running   0          9m25s


Liveness Probes
----------------

Observe how Kubernetes responds to failing liveness probes.


Step 1: forward a local port
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    # On terminal 2, to the health port of the healthy-monolith pod.
    $ kubectl port-forward healthy-monolith 10081:81


Step 2: Force container liveness probe to fail
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    # Use the curl command in terminal 1 to toggle the readiness probe status.
    $ curl http://127.0.0.1:10081/healthz/status

    # Get the status of the healthy-monolith pod using the kubectl get pods -w command.
    $ kubectl get pods healthy-monolith -w
    NAME               READY   STATUS    RESTARTS   AGE
    healthy-monolith   0/1     Running   0          12m
    healthy-monolith   0/1   Running   1     12m
    healthy-monolith   1/1   Running   1     12m

    # When a liveness probe fails, the container is restarted.
    # Once restarted, the healthy-monolith pod should return to a healthy state.
    #!!!! Note the restart count
    $ kubectl describe pods healthy-monolith
    Name:               healthy-monolith
    Namespace:          default
    Priority:           0
    PriorityClassName:  <none>
    Node:               gke-bootcamp-default-pool-6b61ac72-x8wp/10.128.0.13
    Start Time:         Thu, 18 Jul 2019 20:15:18 -0700
    Labels:             app=monolith
    Annotations:        <none>
    Status:             Running
    IP:                 10.48.0.12
    Containers:
      monolith:
        Container ID:   docker://4cef4759f952a35da6c58e593468e25ab6823c4bff45370d50131c7b3dd67d0d
        Image:          kelseyhightower/monolith:1.0.0
        Image ID:       docker-pullable://kelseyhightower/monolith@sha256:72c3f41b6b01c21d9fdd2f45a89c6e5d59b8299b52d7dd0c9491745e73db3a35
        Ports:          80/TCP, 81/TCP
        Host Ports:     0/TCP, 0/TCP
        State:          Running
          Started:      Thu, 18 Jul 2019 20:27:55 -0700
        Last State:     Terminated
          Reason:       Completed
          Exit Code:    0
          Started:      Thu, 18 Jul 2019 20:15:19 -0700
          Finished:     Thu, 18 Jul 2019 20:27:54 -0700
        Ready:          True
        Restart Count:  1
        Limits:
          cpu:     200m
          memory:  10Mi
        Requests:
          cpu:        200m
          memory:     10Mi
        Liveness:     http-get http://:81/healthz delay=5s timeout=5s period=15s #success=1 #failure=3
        Readiness:    http-get http://:81/readiness delay=5s timeout=1s period=10s #success=1 #failure=3
        Environment:  <none>
        Mounts:
          /var/run/secrets/kubernetes.io/serviceaccount from default-token-gh7z2 (ro)
    Conditions:
      Type              Status
      Initialized       True
      Ready             True
      ContainersReady   True
      PodScheduled      True
    Volumes:
      default-token-gh7z2:
        Type:        Secret (a volume populated by a Secret)
        SecretName:  default-token-gh7z2
        Optional:    false
    QoS Class:       Guaranteed
    Node-Selectors:  <none>
    Tolerations:     node.kubernetes.io/not-ready:NoExecute for 300s
                     node.kubernetes.io/unreachable:NoExecute for 300s
    Events:
      Type     Reason     Age                   From                                              Message
      ----     ------     ----                  ----                                              -------
      Normal   Scheduled  13m                   default-scheduler                                 Successfully assigned default/healthy-monolith to gke-bootcamp-default-pool-6b61ac72-x8wp
      Normal   Pulled     13m                   kubelet, gke-bootcamp-default-pool-6b61ac72-x8wp  Container image "kelseyhightower/monolith:1.0.0" already present on machine
      Normal   Created    13m                   kubelet, gke-bootcamp-default-pool-6b61ac72-x8wp  Created container
      Normal   Started    13m                   kubelet, gke-bootcamp-default-pool-6b61ac72-x8wp  Started container
      Warning  Unhealthy  3m28s (x55 over 12m)  kubelet, gke-bootcamp-default-pool-6b61ac72-x8wp  Readiness probe failed: HTTP probe failed with statuscode: 503
