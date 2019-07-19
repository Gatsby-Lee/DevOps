
Google Kubernetes - Services - Coursera
=======================================

Create volumes
--------------

Step 1: Create secret store volume
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # check existing secret store
    $ kubectl get secret
    NAME                  TYPE                                  DATA   AGE
    default-token-gh7z2   kubernetes.io/service-account-token   3      80m

    # secret stores TLS cert files for your nginx server
    $ kubectl create secret generic tls-certs --from-file orchestrate-with-kubernetes/kubernetes/tls/
    secret/tls-certs created

    $ kubectl get secret
    NAME                  TYPE                                  DATA   AGE
    default-token-gh7z2   kubernetes.io/service-account-token   3      81m
    tls-certs             Opaque                                4      3s


Step 2: Create ConfigMap volume
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    $ kubectl get configmap
    No resources found.

    # for nginx's configuration file.
    $ kubectl create configmap nginx-proxy-conf --from-file orchestrate-with-kubernetes/kubernetes/nginx/proxy.conf
    configmap/nginx-proxy-conf created

    $ kubectl get configmap
    NAME               DATA   AGE
    nginx-proxy-conf   1      2s

    # check content of nginx-proxy-conf
    $ kubectl describe configmap nginx-proxy-conf
    Name:         nginx-proxy-conf
    Namespace:    default
    Labels:       <none>
    Annotations:  <none>

    Data
    ====
    proxy.conf:
    ----
    server {
      listen 443;
      ssl    on;

      ssl_certificate     /etc/tls/cert.pem;
      ssl_certificate_key /etc/tls/key.pem;

      location / {
        proxy_pass http://127.0.0.1:80;
      }
    }

    Events:  <none>


::

    The file specifies that SSL is ON and specifies the location of cert files in the container file system.
    The files really exist in the secret volume, so you need to mount the volume to the container's file system.


Create pod
----------

.. code-block:: bash

    $ kubectl create -f orchestrate-with-kubernetes/kubernetes/pods/secure-monolith.yaml
    pod/secure-monolith created

    $ kubectl get pods --show-labels
    NAME              READY   STATUS    RESTARTS   AGE   LABELS
    secure-monolith   2/2     Running   0          23m   app=monolith


Explore the secure-monolith pod configuration file. ( nginx, monolith )

.. code-block:: bash

    $ cat orchestrate-with-kubernetes/kubernetes/pods/secure-monolith.yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: "secure-monolith"
      labels:
        app: monolith
    spec:
      containers:
        - name: nginx
          image: "nginx:1.9.14"
          lifecycle:
            preStop:
              exec:
                command: ["/usr/sbin/nginx","-s","quit"]
          volumeMounts:
            - name: "nginx-proxy-conf"
              mountPath: "/etc/nginx/conf.d"
            - name: "tls-certs"
              mountPath: "/etc/tls"
        - name: monolith
          image: "kelseyhightower/monolith:1.0.0"
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
      volumes:
        - name: "tls-certs"
          secret:
            secretName: "tls-certs"
        - name: "nginx-proxy-conf"
          configMap:
            name: "nginx-proxy-conf"
            items:
              - key: "proxy.conf"
                path: "proxy.conf"


::

    Under volumes, the pod attaches the two volumes you created. And under volumeMounts, it mounts the tls-certs volume to the container's file system so nginx can consume the data.


Create service
--------------

.. code-block:: bash

    $ kubectl get service
    NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
    kubernetes   ClusterIP   10.113.0.1   <none>        443/TCP   106m

    $ kubectl create -f orchestrate-with-kubernetes/kubernetes/services/monolith.yaml
    service/monolith created

    $ kubectl get service
    NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)         AGE
    kubernetes   ClusterIP   10.113.0.1      <none>        443/TCP         108m
    monolith     NodePort    10.113.14.131   <none>        443:31000/TCP   25s

    $ kubectl describe services monolith
    Name:                     monolith
    Namespace:                default
    Labels:                   <none>
    Annotations:              <none>
    Selector:                 app=monolith,secure=enabled
    Type:                     NodePort
    IP:                       10.113.14.131
    Port:                     <unset>  443/TCP
    TargetPort:               443/TCP
    NodePort:                 <unset>  31000/TCP
    Endpoints:                <none>
    Session Affinity:         None
    External Traffic Policy:  Cluster
    Events:                   <none>


Explore the monolith service configuration file.

.. code-block:: bash

    # The selector that finds and exposes pods with labels app=monolith and secure=enabled
    # targetPort and nodePort that forward external traffic from port 31000 to nginx on port 443.

    $ cat orchestrate-with-kubernetes/kubernetes/services/monolith.yaml
    kind: Service
    apiVersion: v1
    metadata:
      name: "monolith"
    spec:
      selector:
        app: "monolith"
        secure: "enabled"
      ports:
        - protocol: "TCP"
          port: 443
          targetPort: 443
          nodePort: 31000
      type: NodePort


::

    NodePort in the Service's yaml file means that it uses a port on each cluster node to expose the service.
    This means that it's possible to have "port collisions" if another app tries to bind to port 31000 on one of your servers."""

    Normally, Kubernetes handles this port assignment for you. In this lab, you chose one so that it's easier to configure health checks later.


Create firewall-rules
---------------------

.. code-block:: bash

    # Allow traffic to the monolith service on the exposed nodeport.
    # secure-monolith service is accessble from outside the cluster without using port forwarding

    $ gcloud compute firewall-rules create allow-monolith-nodeport --allow=tcp:31000
    Creating firewall...done.
    NAME                     NETWORK  DIRECTION  PRIORITY  ALLOW      DENY  DISABLED
    allow-monolith-nodeport  default  INGRESS    1000      tcp:31000        False


Open with browser
-----------------

.. code-block::

    # Get an IP address for one of your nodes.
    $ gcloud compute instances list
    NAME                                     ZONE           MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP      STATUS
    gke-bootcamp-default-pool-d6f7288a-89h1  us-central1-a  n1-standard-1               10.128.0.3   104.197.253.227  RUNNING
    gke-bootcamp-default-pool-d6f7288a-9p4k  us-central1-a  n1-standard-1               10.128.0.6   34.68.200.9      RUNNING
    gke-bootcamp-default-pool-d6f7288a-cz3p  us-central1-a  n1-standard-1               10.128.0.5   34.68.212.121    RUNNING
    gke-bootcamp-default-pool-d6f7288a-pxpg  us-central1-a  n1-standard-1               10.128.0.2   35.239.52.151    RUNNING
    gke-bootcamp-default-pool-d6f7288a-ws9z  us-central1-a  n1-standard-1               10.128.0.4   34.68.182.91     RUNNING


    # Try to open the URL in your browser.
    # BUT, That timed out or refused to connect. What's going wrong?
    https://34.68.182.91:31000/


Questions:
^^^^^^^^^^

* Why can't you get a response from the monolith service?
* How many endpoints does the monolith service have?
* What labels must a pod have to be picked up by the monolith service?



Adding Labels to Pods
---------------------


Currently the monolith service does not have any endpoints because there is no matched pod with selector "app=monolith,secure=enabled"


.. code-block:: bash

    # check endpoints
    $ kubectl get endpoints monolith
    NAME       ENDPOINTS   AGE
    monolith   <none>      13m

    # check pods with selector that service uses.
    $ kubectl get pods -l "app=monolith,secure=enabled"
    No resources found.

    $ kubectl get pods --show-labels
    NAME              READY   STATUS    RESTARTS   AGE   LABELS
    secure-monolith   2/2     Running   0          23m   app=monolith

    # Add label
    $ kubectl label pods secure-monolith 'secure=enabled'
    pod/secure-monolith labeled

    $ kubectl get pods secure-monolith --show-labels
    NAME              READY   STATUS    RESTARTS   AGE   LABELS
    secure-monolith   2/2     Running   0          10m   app=monolith,secure=enabled

    $ kubectl get endpoints monolith
    NAME       ENDPOINTS        AGE
    monolith   10.48.0.13:443   17m


the SSL warning because secure-monolith is using a self-signed certificate.
