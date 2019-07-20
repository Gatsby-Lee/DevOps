Google Kubernetes - Deployment - Coursera
=========================================


Start Cloud Shell Terminal
--------------------------

.. code-block:: bash

    $ gcloud auth list

    # define default timezone.
    $ gcloud config set compute/zone us-central1-a


Launch Kubernetes Cluster
-------------------------

The scopes argument provides access to project hosting and Google Cloud Storage APIs that you'll use later.

.. code-block:: bash

    gcloud container clusters create bootcamp --num-nodes 3 --scopes "https://www.googleapis.com/auth/projecthosting,storage-rw"


Prepare Sample Code
-------------------

.. code-block:: bash

    git clone https://github.com/Gatsby-Lee/orchestrate-with-kubernetes
    cd orchestrate-with-kubernetes/kubernetes



Learn About Deployment Objects
------------------------------

.. code-block:: bash

    # about the deployment object.
    $ kubectl explain deployment

    # --recursive option to see all of the fields.
    $ kubectl explain deployment --recursive

    # individual fields
    $ kubectl explain deployment.metadata.name


Create auth deployment / service
--------------------------------

Create auth deployment
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ kubectl create -f deployments/auth.yaml
    $ kubectl get deployments
    NAME   DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
    auth   1         1         1            0           6s

    # Kubernetes creates a ReplicaSet for the deployment like with a name like auth-xxxxxxx
    $ kubectl get replicasets
    NAME              DESIRED   CURRENT   READY   AGE
    auth-697545c8cc   1         1         1       112s

    # view the pods created for your deployment.
    # A single pod was created when the ReplicaSet was created.
    $ kubectl get pods
    NAME                    READY   STATUS    RESTARTS   AGE
    auth-697545c8cc-krkpv   1/1     Running   0          37s


.. code-block:: bash

    # Examine the deployment configuration file.
    $ cat deployments/auth.yaml

    apiVersion: extensions/v1beta1
    kind: Deployment
    metadata:
      name: auth
    spec:
      replicas: 1
      template:
        metadata:
          labels:
            app: auth
            track: stable
        spec:
          containers:
            - name: auth
              image: "kelseyhightower/auth:2.0.0"
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


Create auth service
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ kubectl create -f services/auth.yaml


.. code-block:: bash

    # Examine the service configuration file.
    $ cat services/auth.yaml
    kind: Service
    apiVersion: v1
    metadata:
      name: "auth"
    spec:
      selector:
        app: "auth"
      ports:
        - protocol: "TCP"
          port: 80
          targetPort: 80


Create hello deployment / service
--------------------------------

Create hello deployment
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ kubectl get deployment
    NAME   DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
    auth   1         1         1            1           14m

    $ kubectl create -f deployments/hello.yaml

    $ kubectl get deployment
    NAME    DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
    auth    1         1         1            1           14m
    hello   3         3         3            0           5s

    $ kubectl get replicasets
    NAME               DESIRED   CURRENT   READY   AGE
    auth-697545c8cc    1         1         1       15m
    hello-5cbf94fc49   3         3         3       31s

    $ kubectl get pods
    NAME                     READY   STATUS    RESTARTS   AGE
    auth-697545c8cc-krkpv    1/1     Running   0          15m
    hello-5cbf94fc49-jg7nc   1/1     Running   0          69s
    hello-5cbf94fc49-jrx6q   1/1     Running   0          69s
    hello-5cbf94fc49-mj5cf   1/1     Running   0          69s


.. code-block:: bash

    # Examine the deployment configuration file.
    $ cat deployments/hello.yaml
    apiVersion: extensions/v1beta1
    kind: Deployment
    metadata:
      name: hello
    spec:
      replicas: 3
      template:
        metadata:
          labels:
            app: hello
            track: stable
            version: 1.0.0
        spec:
          containers:
            - name: hello
              image: "kelseyhightower/hello:1.0.0"
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


Create hello service
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ kubectl get service
    NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
    auth         ClusterIP   10.113.2.142   <none>        80/TCP    4m51s
    kubernetes   ClusterIP   10.113.0.1     <none>        443/TCP   28m

    $ kubectl create -f services/hello.yaml

    $ kubectl get service
    NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
    auth         ClusterIP   10.113.2.142   <none>        80/TCP    6m47s
    hello        ClusterIP   10.113.9.103   <none>        80/TCP    3s
    kubernetes   ClusterIP   10.113.0.1     <none>        443/TCP   30m


.. code-block:: bash

    $ cat services/hello.yaml
    kind: Service
    apiVersion: v1
    metadata:
      name: "hello"
    spec:
      selector:
        app: "hello"
      ports:
        - protocol: "TCP"
          port: 80
          targetPort: 80


Create frontend deployment / service
------------------------------------

Create volumes
^^^^^^^^^^^^^^

.. code-block:: bash

    kubectl create configmap nginx-frontend-conf --from-file=nginx/frontend.conf
    kubectl create secret generic tls-certs --from-file tls/


.. code-block:: bash

    $ cat nginx/frontend.conf
    upstream hello {
        server hello.default.svc.cluster.local;
    }

    upstream auth {
        server auth.default.svc.cluster.local;
    }

    server {
        listen 443;
        ssl    on;

        ssl_certificate     /etc/tls/cert.pem;
        ssl_certificate_key /etc/tls/key.pem;

        location / {
            proxy_pass http://hello;
        }

        location /login {
            proxy_pass http://auth;
        }
    }


Create frontend deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ kubectl create -f deployments/frontend.yaml

    $ kubectl get deployments
    NAME       DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
    auth       1         1         1            1           26m
    frontend   1         1         1            0           3s
    hello      3         3         3            3           11m

    $ kubectl get replicaset
    NAME                  DESIRED   CURRENT   READY   AGE
    auth-697545c8cc       1         1         1       33m
    frontend-77f46bf858   1         1         1       7m30s
    hello-5cbf94fc49      3         3         3       19m

    $ kubectl get pods --show-labels
    NAME                        READY   STATUS    RESTARTS   AGE     LABELS
    auth-697545c8cc-krkpv       1/1     Running   0          32m     app=auth,pod-template-hash=697545c8cc,track=stable
    frontend-77f46bf858-mhkld   1/1     Running   0          6m29s   app=frontend,pod-template-hash=77f46bf858,track=stable
    hello-5cbf94fc49-jg7nc      1/1     Running   0          18m     app=hello,pod-template-hash=5cbf94fc49,track=stable,version=1.0.0
    hello-5cbf94fc49-jrx6q      1/1     Running   0          18m     app=hello,pod-template-hash=5cbf94fc49,track=stable,version=1.0.0
    hello-5cbf94fc49-mj5cf      1/1     Running   0          18m     app=hello,pod-template-hash=5cbf94fc49,track=stable,version=1.0.0


.. code-block:: bash

    $ cat deployments/frontend.yaml
    apiVersion: extensions/v1beta1
    kind: Deployment
    metadata:
      name: frontend
    spec:
      replicas: 1
      template:
        metadata:
          labels:
            app: frontend
            track: stable
        spec:
          containers:
            - name: nginx
              image: "nginx:1.9.14"
              lifecycle:
                preStop:
                  exec:
                    command: ["/usr/sbin/nginx","-s","quit"]
              volumeMounts:
                - name: "nginx-frontend-conf"
                  mountPath: "/etc/nginx/conf.d"
                - name: "tls-certs"
                  mountPath: "/etc/tls"
          volumes:
            - name: "tls-certs"
              secret:
                secretName: "tls-certs"
            - name: "nginx-frontend-conf"
              configMap:
                name: "nginx-frontend-conf"
                items:
                  - key: "frontend.conf"
                    path: "frontend.conf"


Create frontend deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ kubectl create -f services/frontend.yaml


.. code-blcok:: bash

    $ cat services/frontend.yaml
    kind: Service
    apiVersion: v1
    metadata:
      name: "frontend"
    spec:
      selector:
        app: "frontend"
      ports:
        - protocol: "TCP"
          port: 443
          targetPort: 443
      type: LoadBalancer


curl service
------------

.. code-block:: bash

    curl -ks https://<EXTERNAL-IP>

    $ curl -ks https://`kubectl get svc frontend -o=jsonpath="{.status.loadBalancer.ingress[0].ip}"`
    {"message":"Hello"}


-----------------------------


Scale a deployment
------------------

    # view about deployment.spec.replicas
    $ kubectl explain deployment.spec.replicas

    # add replicas
    $ kubectl scale deployment hello --replicas=5

    # check running replicas (pod)
    $ kubectl get pods | grep hello- | wc -l

    $ kubectl scale deployment hello --replicas=3



Rolling Updates
---------------

Deployments update images to new versions through rolling updates. When a deployment is updated with a new version, it creates a new ReplicaSet and slowly increases the number of replicas in the new ReplicaSet as it decreases the replicas in the old ReplicaSet.


Trigger a Rolling Update
^^^^^^^^^^^^^^^^^^^^^^^^^

The updated deployment is saved to your cluster and Kubernetes begins a rolling update.

.. code-block:: bash

    $ kubectl edit deployment hello
    # Change the image in containers section to the following, then save and exit.
    # containers:
    # - name: hello
    #   image: kelseyhightower/hello:2.0.0

    # View the new entry in the rollout history.
    $ kubectl rollout history deployment/hello
    deployment.extensions/hello
    REVISION  CHANGE-CAUSE
    1         <none>
    2         <none>

    # new version of container can be found in Events
    $ kubectl describe pod hello-677685c76-q6rdb


Pause Rolling Update
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ kubectl rollout pause deployment/hello

    # Verify the current state of the rollout.
    $ kubectl rollout status deployment/hello

    # Verify this with the pods.
    $ kubectl get pods -o jsonpath --template='{range .items[*]}{.metadata.name}{"\t"}{"\t"}{.spec.containers[0].image}{"\n"}{end}'

    # Resume a Rolling Update
    $ kubectl rollout resume deployment/hello

    # verify the rollout is complete.
    $ kubectl rollout status deployment/hello
    deployment "hello" successfully rolled out


Rollback an Update
^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    # roll back to the previous version
    $ kubectl rollout undo deployment/hello

    # Verify the rollback in the deployment's history.
    $ kubectl rollout history deployment/hello

    # Verify all pods have rolled back to the previous version.
    $ kubectl get pods -o jsonpath --template='{range .items[*]}{.metadata.name}{"\t"}{"\t"}{.spec.containers[0].image}{"\n"}{end}'



Canary Deployments
------------------

Run a canary deployment to test a new deployment in production with a subset of users. This mitigates risk with new releases.

A canary deployment consists of a separate deployment from your stable deployment and a service that targets them both at the same time.


Create hello-canary deployement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The hello service selector uses app: hello, which matches pods in both deployments. However, the canary deployment has fewer pods, and is only used by a subset of users.


.. code-block:: bash

    $ kubectl create -f deployments/hello-canary.yaml

    $ kubectl get deployments
    NAME           DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
    auth           1         1         1            1           66m
    frontend       1         1         1            1           40m
    hello          3         3         3            3           52m
    hello-canary   1         1         1            1           31s

    $ kubectl get pods
    NAME                            READY   STATUS    RESTARTS   AGE
    auth-697545c8cc-krkpv           1/1     Running   0          69m
    frontend-77f46bf858-mhkld       1/1     Running   0          43m
    hello-5cbf94fc49-5j85g          1/1     Running   0          10m
    hello-5cbf94fc49-8vwwx          1/1     Running   0          10m
    hello-5cbf94fc49-m95j5          1/1     Running   0          10m
    hello-canary-5b8c844cb6-lzd2j   1/1     Running   0          3m

.. code-block:: bash

    $ cat deployments/hello-canary.yaml
    apiVersion: extensions/v1beta1
    kind: Deployment
    metadata:
      name: hello-canary
    spec:
      replicas: 1
      template:
        metadata:
          labels:
            app: hello
            track: canary
            version: 2.0.0
        spec:
          containers:
            - name: hello
              image: kelseyhightower/hello:2.0.0
              ports:
                - name: http
                  containerPort: 80
                - name: health
                  containerPort: 81
              resources:
                limits:
                  cpu: 0.2
                  memory: 10Mi
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


Verify the Canary Deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

verify both hello versions being served by requests.


.. code-block:: bash

    # this makes request and print version
    $ curl -ks https://`kubectl get svc frontend -o=jsonpath="{.status.loadBalancer.ingress[0].ip}"`/version


By default, every request has a chance to be served by the canary deployment. If you want users to get all their responses from the same version, enable session affinity in the configuration file as follows:

::

    spec:
        sessionAffinity: ClientIP


Delete Canary Deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    kubectl delete deployment hello-canary



Blue-Green Deployments
----------------------

You can use blue-green deployments if it's more beneficial to modify load balancers to point to a new, fully-tested deployment all at once.

A downside is you need double the resources to host both versions of your application during the switch.

You use two nearly-identical service files (hello-blue and hello-green) to switch between versions. The only difference between these files is their version selector. You could edit the service while it's running and change the version selector, but switching files is easier for labs.

.. code-block:: bash

    $ kubectl get service
    NAME         TYPE           CLUSTER-IP     EXTERNAL-IP    PORT(S)         AGE
    auth         ClusterIP      10.113.2.142   <none>         80/TCP          73m
    frontend     LoadBalancer   10.113.5.195   35.202.89.58   443:32287/TCP   57m
    hello        ClusterIP      10.113.9.103   <none>         80/TCP          66m
    kubernetes   ClusterIP      10.113.0.1     <none>         443/TCP         97m

    # You use the existing hello deployment for the blue version and a new hello-green deployment for the green version.
    # First, update the service to use the blue deployment:
    $ kubectl apply -f services/hello-blue.yaml

    # Create the green deployment.
    $ kubectl create -f deployments/hello-green.yaml

    $ kubectl get deployments
    NAME          DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
    auth          1         1         1            1           89m
    frontend      1         1         1            1           63m
    hello         3         3         3            3           74m
    hello-green   3         3         3            1           9s

    # Verify the blue deployment (1.0.0) is still being used.
    $ curl -ks https://`kubectl get svc frontend -o=jsonpath="{.status.loadBalancer.ingress[0].ip}"`/version
    {"version":"1.0.0"}

    # Run the following command to update the service to use the green deployment.
    $ kubectl apply -f services/hello-green.yaml

    $ kubectl describe service hello
    Name:              hello
    Namespace:         default
    Labels:            <none>
    Annotations:       kubectl.kubernetes.io/last-applied-configuration:
                         {"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"name":"hello","namespace":"default"},"spec":{"ports":[{"port":80,"protoc...
    Selector:          app=hello,version=2.0.0
    Type:              ClusterIP
    IP:                10.113.9.103
    Port:              <unset>  80/TCP
    TargetPort:        80/TCP
    Endpoints:         10.48.1.11:80,10.48.2.13:80
    Session Affinity:  None
    Events:            <none>

    # Verify the green deployment is being used.
    $ curl -ks https://`kubectl get svc frontend -o=jsonpath="{.status.loadBalancer.ingress[0].ip}"`/version
    {"version":"2.0.0"}


.. code-block:: bash

    $ cat services/hello.yaml
    kind: Service
    apiVersion: v1
    metadata:
      name: "hello"
    spec:
      selector:
        app: "hello"
      ports:
        - protocol: "TCP"
          port: 80
          targetPort: 80

    $ cat services/hello-blue.yaml
    kind: Service
    apiVersion: v1
    metadata:
      name: "hello"
    spec:
      selector:
        app: "hello"
        version: 1.0.0
      ports:
        - protocol: "TCP"
          port: 80
          targetPort: 80

    $ cat services/hello-green.yaml
    kind: Service
    apiVersion: v1
    metadata:
      name: hello
    spec:
      selector:
        app: hello
        version: 2.0.0
      ports:
        - protocol: TCP
          port: 80
          targetPort: 80

    $ cat deployments/hello-green.yaml
    apiVersion: extensions/v1beta1
    kind: Deployment
    metadata:
      name: hello-green
    spec:
      replicas: 3
      template:
        metadata:
          labels:
            app: hello
            track: stable
            version: 2.0.0
        spec:
          containers:
            - name: hello
              image: kelseyhightower/hello:2.0.0
              ports:
                - name: http
                  containerPort: 80
                - name: health
                  containerPort: 81
              resources:
                limits:
                  cpu: 0.2
                  memory: 10Mi
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


Rollback a Blue-Green Deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can roll back to the old version.

While the green deployment is still running, simply update the service to the old (blue) deployment.


.. code-block:: bash

    $ kubectl apply -f services/hello-blue.yaml

    $ kubectl describe service hello
    Name:              hello
    Namespace:         default
    Labels:            <none>
    Annotations:       kubectl.kubernetes.io/last-applied-configuration:
                         {"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"name":"hello","namespace":"default"},"spec":{"ports":[{"port":80,"protoc...
    Selector:          app=hello,version=1.0.0
    Type:              ClusterIP
    IP:                10.113.9.103
    Port:              <unset>  80/TCP
    TargetPort:        80/TCP
    Endpoints:         10.48.0.5:80,10.48.1.10:80,10.48.2.11:80
    Session Affinity:  None
    Events:            <none>

    # Verify that the blue deployment is being used.
    $ curl -ks https://`kubectl get svc frontend -o=jsonpath="{.status.loadBalancer.ingress[0].ip}"`/version
    {"version":"1.0.0"}
