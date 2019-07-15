Start Cloud Shell Terminal
--------------------------

.. code-block:: bash

    gcloud auth list
    # define default timezone.
    gcloud config set compute/zone us-central1-a


Launch Kubernetes Cluster
-------------------------

Launch cluster
^^^^^^^^^^^^^^

The scopes argument provides access to project hosting and Google Cloud Storage APIs that you'll use later.

.. code-block:: bash
    $ gcloud container clusters create bootcamp --num-nodes 1 --scopes "https://www.googleapis.com/auth/projecthosting,storage-rw"


Check Kubernetes version and cluster-info
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After the cluster is created, check your installed version of Kubernetes and cluster info.

The `gcloud container clusters create` command automatically authenticated kubectl for you.

Launched VM can be found both `Comput Engines > VM Instances` and `Kubernete Engine > Cluster`

.. code-block:: bash

    # this prints the version of Client and Server.
    $ kubectl version
    Client Version: version.Info{Major:"1", Minor:"12+", GitVersion:"v1.12.9-gke.7", GitCommit:"b6001a5d99c235723fc19342d347eee4394f2005", GitTreeState:"clean", BuildDate:"2019-06-24T19:27:39Z", GoVersion:"go1.10.8b4", Compiler:"gc", Platform:"linux/amd64"}
    Server Version: version.Info{Major:"1", Minor:"12+", GitVersion:"v1.12.8-gke.10", GitCommit:"f53039cc1e5295eed20969a4f10fb6ad99461e37", GitTreeState:"clean", BuildDate:"2019-06-19T20:48:40Z", GoVersion:"go1.10.8b4", Compiler:"gc", Platform:"linux/amd64"}

    $ kubectl cluster-info
    Kubernetes master is running at https://35.238.248.203
    GLBCDefaultBackend is running at https://35.238.248.203/api/v1/namespaces/kube-system/services/default-http-backend:http/proxy
    Heapster is running at https://35.238.248.203/api/v1/namespaces/kube-system/services/heapster/proxy
    KubeDNS is running at https://35.238.248.203/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
    Metrics-server is running at https://35.238.248.203/api/v1/namespaces/kube-system/services/https:metrics-server:/proxy

    To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.



Run and deploy a container (Nginx)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Step 1: Launch Nginx container
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Kubernetes, all containers run in pods. And in this command, Kubernetes created what is called a deployment behind the scenes, and runs a single pod with the nginx container in it. A deployment keeps a given number of pods up and running even when the nodes they run on fail. In this case, you run the default number of pods, which is 1.


.. code-block:: bash

    $ kubectl run nginx --image=nginx:1.10.0
    kubectl run --generator=deployment/apps.v1beta1 is DEPRECATED and will be removed in a future version. Use kubectl create instead.
    deployment.apps/nginx created


Step 2: View the pod running the nginx container
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ kubectl get pods
    NAME                     READY   STATUS    RESTARTS   AGE
    nginx-5fc69dfb5d-q5x2t   1/1     Running   0          2m38s

    $ kubectl get services
    NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
    kubernetes   ClusterIP   10.113.0.1   <none>        443/TCP   26m


Step 3: Expose the nginx container outside Kubernetes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Kubernetes created a service and an external load balancer with a public IP address attached to it. The IP address remains the same for the life of the service. Any client who hits that public IP address (for example an end user or another container) is routed to pods behind the service. In this case, that would be the nginx pod.

.. code-block:: bash

    $ kubectl expose deployment nginx --port 80 --type LoadBalancer
    service/nginx exposed

    # You'll see an external IP that you can use to test and contact the nginx container remotely.
    # It may take a few seconds before the ExternalIP field is populated for your service.
    $ kubectl get services
    NAME         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
    kubernetes   ClusterIP      10.113.0.1     <none>        443/TCP        27m
    nginx        LoadBalancer   10.113.0.162   <pending>     80:31286/TCP   3s

    $ kubectl get services
    NAME         TYPE           CLUSTER-IP     EXTERNAL-IP      PORT(S)        AGE
    kubernetes   ClusterIP      10.113.0.1     <none>           443/TCP        29m
    nginx        LoadBalancer   10.113.0.162   35.239.227.252   80:31286/TCP   112s


Step 4: Test with external IP address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ curl http://35.239.227.252


Step 5: Scale out Nginx
^^^^^^^^^^^^^^^^^^^^^^^^

Increase the number of backend applications (pods) running on your service using.

.. code-block:: bash

    $ kubectl scale deployment nginx --replicas 3
    deployment.extensions/nginx scaled


Check number of pods

.. code-block:: bash

    $ kubectl get pods
    NAME                     READY   STATUS    RESTARTS   AGE
    nginx-5fc69dfb5d-d2dh4   1/1     Running   0          14m
    nginx-5fc69dfb5d-q5x2t   1/1     Running   0          28m
    nginx-5fc69dfb5d-qpdch   1/1     Running   0          14m


Confirm Nginx service external IP address has not changed

.. code-block:: bash

    $ kubectl get services
    NAME         TYPE           CLUSTER-IP     EXTERNAL-IP      PORT(S)        AGE
    kubernetes   ClusterIP      10.113.0.1     <none>           443/TCP        51m
    nginx        LoadBalancer   10.113.0.162   35.239.227.252   80:31286/TCP   24m


Step 6: Clean up pod and service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ kubectl delete deployment nginx
    $ kubectl delete service nginx

    $ kubectl delete deployment nginx
    deployment.extensions "nginx" deleted
    $ kubectl delete service nginx
    service "nginx" deleted
    $ kubectl get pods
    No resources found.
    $ kubectl get service
    NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
    kubernetes   ClusterIP   10.113.0.1   <none>        443/TCP   57m


Step 7: Delete cluster

.. code-block:: bash

    $ gcloud container clusters delete bootcamp
