Google Cloud Kubernetes Workload
================================

kubectl autocomplete
--------------------

https://kubernetes.io/docs/reference/kubectl/cheatsheet/#kubectl-autocomplete

kubectl command
---------------

Summary
>>>>>>>

* kubectl is a utility used by admin to control Kubernetes cluster
* kubectl is composed of serveral parts, such as command, type, name, and optional flags



.. image:: ./images/gcp_k8e_workload/kubectl_cmd.png

.. image:: ./images/gcp_k8e_workload/kubectl_api.png


kubctl config
>>>>>>>>>>>>>

* relies on config file: **$HOME/.kube/config**
* config file contains

  * target cluster name
  * credentials for the cluster
  
* to see current config,

.. code-block:: bash

  kubectl config view
  
  
retrieve credentials for cluster
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block::

  gcloud containers clusters \
  get-credentials [cluster_name] \
  --zone [ZONE_NAME]
  


Introspection
-------------

kubectl get
>>>>>>>>>>>

* Pod phases:

  * Pending
  * Running
  * Successed
  * Failed
  * Unkown
  * CrahLoopBackOff


kubectl describe
>>>>>>>>>>>>>>>>


kubectl exec
>>>>>>>>>>>>

Running a command within a pod

.. code-block:: bash

  # kubectl exec -it [pod_name] -- [command]
  # -i is for std input
  # -t tells std input is TTY
  # -c is to attch to specfic pod
  kubectl exec -it demo -- /bin/bash


kubectl logs
>>>>>>>>>>>>


Cluster
-------

Create cluster
>>>>>>>>>>>>>>

.. code-block:: bash

  # ref: https://cloud.google.com/sdk/gcloud/reference/container/clusters/create
  gcloud container clusters create $my_cluster --num-nodes 3 --zone $my_zone --enable-ip-alias
  

Increase Node in cluster
>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: bash

  gcloud container clusters resize $my_cluster --zone $my_zone --size=4
  

Connect to GKE cluster
>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: bash

  $ gcloud container clusters get-credentials $my_cluster --zone $my_zone
  Fetching cluster endpoint and auth data.
  kubeconfig entry generated for standard-cluster-1.
  
  
Inspect GKE cluster
>>>>>>>>>>>>>>>>>>>

.. code-block:: bash

  # print content of the kubeconfig
  kubectl config view
  # print cluster information
  kubectl cluster-info
  # print out the active context
  kubectl config current-context
  # print out some details for all the cluster contexts in the kubeconfig file
  kubectl config get-contexts
  # change active context
  kubectl config use-context gke_${GOOGLE_CLOUD_PROJECT}_us-central1-a_standard-cluster-1
  

Enable kubectl command hint
>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: bash

  source <(kubectl completion bash)
  

Deploy Pods
>>>>>>>>>>>>

.. code-block:: bash

  $ kubectl run nginx-1 --image nginx:latest
  
  $ kubectl get pods
  NAME                      READY   STATUS    RESTARTS   AGE
  nginx-1-6866cfb98-ckpq8   1/1     Running   0          36s
  
  $ kubectl describe pod nginx-1-6866cfb98-ckpq8


Copy file to container
>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: bash

  kubectl cp ~/test.html $my_nginx_pod:/usr/share/nginx/html/test.html
  

Expose Pod for testing
>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: bash

  $ kubectl expose pod $my_nginx_pod --port 80 --type LoadBalancer
  service/nginx-1-6866cfb98-ckpq8 exposed

  $ kubectl get services
  NAME                      TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
  kubernetes                ClusterIP      10.12.0.1      <none>        443/TCP        21m
  nginx-1-6866cfb98-ckpq8   LoadBalancer   10.12.10.222   <pending>     80:31652/TCP   9s
  

Deploy Pods with config
>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: bash

    $ git clone https://github.com/GoogleCloudPlatformTraining/training-data-analyst
    $ cd ~/training-data-analyst/courses/ak8s/04_GKE_Shell/

    # sample config
    $ cat new-nginx-pod.yaml 
    apiVersion: v1
    kind: Pod
    metadata:
      name: new-nginx
      labels:
        name: new-nginx
    spec:
      containers:
      - name: new-nginx
        image: nginx
        ports:
        - containerPort: 80
        
    # deploy pod
    $ kubectl apply -f ./new-nginx-pod.yaml


Check running pods
>>>>>>>>>>>>>>>>>>

.. code-block:: bash

  $ kubectl get pods
  NAME                      READY   STATUS    RESTARTS   AGE
  new-nginx                 1/1     Running   0          14s
  nginx-1-6866cfb98-ckpq8   1/1     Running   0          15m


Connect to container in pod
>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: bash

  # connecting container in pod
  # if there is more than one container, then -c can be used to connect to specific conatiner.
  $ kubectl exec -it new-nginx /bin/bash


Port-forwarding
>>>>>>>>>>>>>>>

.. code-block:: bash

  # port-forwarding
  $ kubectl port-forward new-nginx 10081:80


View logging
>>>>>>>>>>>>>>>

.. code-block:: bash

  # monitor logging
  $ kubectl port-forward new-nginx 10081:80
  


Deployments
-----------

Deployments defines/describe a desired of state of pods

.. image:: ./images/gcp_k8e_workload/deployment_twoparts_process.png

Once deployment config YAML is submitted Kubernetes master, Kubernetes creates **deployment controller**. Deployment Controller is
responsible for converting the desired state(config) to reality and keeping the desired state over time.


Deployment Usage
>>>>>>>>>>>>>>>>

.. image:: ./images/gcp_k8e_workload/deployment_usage.png


Three ways to create deployment
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

* create a deployment **declaratively** using a manifest file, such as a YAML

.. code-block:: bash

  kubectl apply -f [DEPLOYMENT_FILE]
  
  
* creates a deployment **imperatively**, using a kubectl run command 

.. code-block:: bash

  kubectl run [DEPLOYMENT_NAME] \
  --image [IMAGE]:[TAG]
  --replicas 3 \
  --labels [KEY]=[VALUE] \
  --port 8080 \
  --generator deployment/app.v1 \
  --save-config
  
* using GCP Console


How to inspect Deployment
>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: bash

  kubectl get deployment [DEPLOYMENT_NAME]


How to print/output Deployment config in a YAML format
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-blcok:: bash

  kubectl get deployment [DEPLOYMENT_NAME] -o yaml > this.yaml
  
  
How to get more details about Deployment
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: bash

  kubectl describe deployment [DEPLOYMENT_NAME]
  

Scaling deployments
>>>>>>>>>>>>>>>>>>>

.. image:: ./images/gcp_k8e_workload/service_loadbalancing.png


.. code-block:: bash

  # manual-scaling a deployment
  kubectl scale deployemnt [DEPLOYMENT_NAME] --replicas=5
  
  # autos-caling a deployment
  kubectl autoscale deployemnt [DEPLOYMENT_NAME] --min=5 --max=15 --cpu-percent=75
  

How to udpate Deployment
>>>>>>>>>>>>>>>>>>>>>>>>

* update pod specification ( YAML )

  * automatic update rollout will happen
  * only applicable to the changes in port specifications
  

* use updated deployment YAML ( kubectl apply -f [DEPLOYMENT_FILE] )

  * allowing to update other specification of a deployment, such as number of replicas
  
* use `kubectl set`
  
  * allowing to change pod specifications for the deployment, such as images, resources, or selector values.

* use `kubectl edit` 

  * once exit/saved, kubectl automatically applies the updated file.
  
* use GCP console


Deployment strategy - Rolling updates
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

* **max unavailable:** specific number or percentage

.. image:: ./images/gcp_k8e_workload/deployment_rollout_max_unavailable.png

.. image:: ./images/gcp_k8e_workload/deployment_rollout_max_unavailable_percentage.png


* **max surge:** specifying max number of pods that can be created concurrently in a new replica set

.. image:: ./images/gcp_k8e_workload/deployment_rollout_max_max_surge.png

.. image:: ./images/gcp_k8e_workload/deployment_rollout_max_max_surge_percentage.png


Deployment strategy - Blue/Green
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
