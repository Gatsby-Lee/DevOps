
Google Kubernetes with Config YAML - Coursera
==============================================


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


Step 2: Explore the monolith pod's configuration file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The pod is made up of one container (called monolith). You pass a few arguments to the container when it starts up and open port 80 for HTTP traffic.


.. code-block:: bash

    $ cat orchestrate-with-kubernetes/kubernetes/pods/monolith.yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: monolith
      labels:
        app: monolith
    spec:
      containers:
        - name: monolith
          image: kelseyhightower/monolith:1.0.0
          args:
            - "-http=0.0.0.0:80"
            - "-health=0.0.0.0:81"
            - "-secret=secret"
          ports:
            - name: http
              containerPort: 80
            - name: health
              containerPort: 81
          resources:
            limits:
              cpu: 0.2
              memory: "10Mi"


Step 3: Explore the built-in documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ kubectl explain pods
    $ kubectl explain pods.spec.containers



Create monolith pods
--------------------

Create pod
^^^^^^^^^^

.. code-block:: bash

    $ kubectl create -f orchestrate-with-kubernetes/kubernetes/pods/monolith.yaml
    pod/monolith created


Explore pod
^^^^^^^^^^^

.. code-block:: bash

    # Use the kubectl get pods command to list all pods running in the default namespace.
    $ kubectl get pods
    NAME       READY   STATUS    RESTARTS   AGE
    monolith   1/1     Running   0          48s

    $ kubectl describe pods monolith
    Name:               monolith
    Namespace:          default
    Priority:           0
    PriorityClassName:  <none>
    Node:               gke-bootcamp-default-pool-d6f7288a-ws9z/10.128.0.4
    Start Time:         Sat, 13 Jul 2019 14:23:43 -0700
    Labels:             app=monolith
    Annotations:        <none>
    Status:             Running
    IP:                 10.48.2.6

    Containers:
      monolith:
        Container ID:  docker://d855832f16f1fa50aacb5ed7d4da1f4d4da84d2831e65e70685681aac844574d
        Image:         kelseyhightower/monolith:1.0.0
        Image ID:      docker-pullable://kelseyhightower/monolith@sha256:72c3f41b6b01c21d9fdd2f45a89c6e5d59b8299b52d7dd0c9491745e73db3a35
        Ports:         80/TCP, 81/TCP
        Host Ports:    0/TCP, 0/TCP
        Args:
          -http=0.0.0.0:80
          -health=0.0.0.0:81
          -secret=secret
        State:          Running
          Started:      Sat, 13 Jul 2019 14:23:45 -0700
        Ready:          True
        Restart Count:  0
        Limits:
          cpu:     200m
          memory:  10Mi
        Requests:
          cpu:        200m
          memory:     10Mi
        Environment:  <none>
        Mounts:
          /var/run/secrets/kubernetes.io/serviceaccount from default-token-vw6s6 (ro)
    Conditions:
      Type              Status
      Initialized       True
      Ready             True
      ContainersReady   True
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
      Type    Reason     Age   From                                              Message
      ----    ------     ----  ----                                              -------
      Normal  Scheduled  63s   default-scheduler                                 Successfully assigned default/monolith to gke-bootcamp-default-pool-de34df5c-rsw3
      Normal  Pulling    62s   kubelet, gke-bootcamp-default-pool-de34df5c-rsw3  pulling image "kelseyhightower/monolith:1.0.0"
      Normal  Pulled     60s   kubelet, gke-bootcamp-default-pool-de34df5c-rsw3  Successfully pulled image "kelseyhightower/monolith:1.0.0"
      Normal  Created    60s   kubelet, gke-bootcamp-default-pool-de34df5c-rsw3  Created container
      Normal  Started    60s   kubelet, gke-bootcamp-default-pool-de34df5c-rsw3  Started container



Interacting with pods
---------------------

Pods are allocated a private IP address by default that cannot be reached outside of the cluster.

Use the `kubectl port-forward` command to map a local port to a port inside the monolith pod.

Use two terminals: one to run the kubectl port-forward command, and the other to issue curl commands.


Forward port
^^^^^^^^^^^^

.. code-block:: bash

    # On console 2
    # Run the following command to set up port-forwarding from a local port, 10080, to a pod port, 80 (where your container is listening).
    $ kubectl port-forward monolith 10080:80
    Forwarding from 127.0.0.1:10080 -> 80


Request to secure and non-secure endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    # On console 1
    $ curl http://127.0.0.1:10080
    {"message":"Hello"}

    # On console 1
    # Failed to request to secure endpoint due to auth token is not included
    $ curl http://127.0.0.1:10080/secure
    authorization failed

    # Logging in causes a JWT token to be printed out. You'll use it to test your secure endpoint with curl.
    # type in 'password'
    $ curl -u user http://127.0.0.1:10080/login
    Enter host password for user 'user':
    {"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InVzZXJAZXhhbXBsZS5jb20iLCJleHAiOjE1NjMzMTI3NTksImlhdCI6MTU2MzA1MzU1OSwiaXNzIjoiYXV0aC5zZXJ2aWNlIiwic3ViIjoidXNlciJ9.bYPMx8hOlyRBt-aVnx6KYTwjj0FHkNC8WZMYTI-JvTg"}

    # Cloud Shell doesn't handle copying long strings well, so copy the token into an environment variable.
    $ TOKEN=$(curl http://127.0.0.1:10080/login -u user|jq -r '.token')

    $ curl -H "Authorization: Bearer $TOKEN" http://127.0.0.1:10080/secure
    {"message":"Hello"}


View log for pod
^^^^^^^^^^^^^^^^

.. code-block:: bash

    # On console 3
    $ kubectl logs -f monolith
    2019/07/13 21:23:45 Starting server...
    2019/07/13 21:23:45 Health service listening on 0.0.0.0:81
    2019/07/13 21:23:45 HTTP service listening on 0.0.0.0:80
    127.0.0.1:40010 - - [Sat, 13 Jul 2019 21:30:01 UTC] "GET / HTTP/1.1" curl/7.52.1
    127.0.0.1:40054 - - [Sat, 13 Jul 2019 21:31:09 UTC] "GET /secure HTTP/1.1" curl/7.52.1
    127.0.0.1:40096 - - [Sat, 13 Jul 2019 21:32:39 UTC] "GET /login HTTP/1.1" curl/7.52.1


Interactive shell inside in pod
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    kubectl exec monolith --stdin --tty -c monolith /bin/sh
    # to exit
    / # exit

Clean up
^^^^^^^^

.. code-block:: bash

    kubectl delete pod monolith


Delete cluster
--------------

.. code-block:: bash

    gcloud container clusters delete bootcamp
