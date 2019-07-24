Google Kubernetes - Setup Jenkins
=================================

ref: https://github.com/GoogleCloudPlatform/continuous-deployment-on-kubernetes


Start Cloud Shell Terminal
--------------------------

.. code-block:: bash

    $ gcloud auth list

    # define default timezone.
    $ gcloud config set compute/zone us-central1-a


Create Kubernetes Cluster
-------------------------

The extra scopes enable Jenkins to access Cloud Source Repositories and Google Container Registry.

.. code-block:: bash

    gcloud container clusters create jenkins-cd \
        --num-nodes 2 \
        --machine-type n1-standard-2 \
        --scopes "https://www.googleapis.com/auth/projecthosting,cloud-platform"


Once that operation completes download the credentials for your cluster

.. code-block:: bash

    $ gcloud container clusters get-credentials jenkins-cd
    Fetching cluster endpoint and auth data.
    kubeconfig entry generated for jenkins-cd.


Prepare Sample Code
-------------------

.. code-block:: bash

    git clone https://github.com/GoogleCloudPlatform/continuous-deployment-on-kubernetes.git
    cd continuous-deployment-on-kubernetes


Install Helm
------------

Use Helm to install Jenkins from the Charts repository.
Helm is a package manager that makes it easy to configure and deploy Kubernetes applications.

Step 1: Download and install the helm binary

.. code-block:: bash

    # There are multiple versions.
    wget https://storage.googleapis.com/kubernetes-helm/helm-v2.14.1-linux-amd64.tar.gz
    tar zxfv helm-v2.14.1-linux-amd64.tar.gz
    cp linux-amd64/helm .


Step 2: Add yourself as a cluster administrator in the cluster's RBAC so that you can give Jenkins permissions in the cluster

.. code-block:: bash

    $ kubectl create clusterrolebinding cluster-admin-binding \
        --clusterrole=cluster-admin \
        --user=$(gcloud config get-value account)
    Your active configuration is: [cloudshell-11957]
    clusterrolebinding.rbac.authorization.k8s.io/cluster-admin-binding created


Step 3: Grant Tiller the server side of Helm, the cluster-admin role in your cluster:

.. code-block:: bash

    kubectl create serviceaccount tiller --namespace kube-system
    kubectl create clusterrolebinding tiller-admin-binding --clusterrole=cluster-admin --serviceaccount=kube-system:tiller


Step 4: Initialize Helm. This ensures that the server side of Helm (Tiller) is properly installed in your cluster.

.. code-block:: bash

    $ ./helm init --service-account=tiller
    Creating /home/ops/.helm
    Creating /home/ops/.helm/repository
    Creating /home/ops/.helm/repository/cache
    Creating /home/ops/.helm/repository/local
    Creating /home/ops/.helm/plugins
    Creating /home/ops/.helm/starters
    Creating /home/ops/.helm/cache/archive
    Creating /home/ops/.helm/repository/repositories.yaml
    Adding stable repo with URL: https://kubernetes-charts.storage.googleapis.com
    Adding local repo with URL: http://127.0.0.1:8879/charts
    $HELM_HOME has been configured at /home/ops/.helm.

    Tiller (the Helm server-side component) has been installed into your Kubernetes Cluster.

    Please note: by default, Tiller is deployed with an insecure 'allow unauthenticated users' policy.
    To prevent this, run `helm init` with the --tiller-tls-verify flag.
    For more information on securing your installation see: https://docs.helm.sh/using_helm/#securing-your-helm-installation

    $ ./helm repo update
    Hang tight while we grab the latest from your chart repositories...
    ...Skip local chart repository
    ...Successfully got an update from the "stable" chart repository
    Update Complete.


Step 5: Ensure Helm is properly installed by running the following command.
You should see versions appear for both the server and the client of v2.14.1:

.. code-block:: bash

    ./helm version
    Client: &version.Version{SemVer:"v2.14.1", GitCommit:"5270352a09c7e8b6e8c9593002a73535276507c0", GitTreeState:"clean"}
    Server: &version.Version{SemVer:"v2.14.1", GitCommit:"5270352a09c7e8b6e8c9593002a73535276507c0", GitTreeState:"clean"}


Configure and Install Jenkins
-----------------------------

You will use a custom values file to add the GCP specific plugin necessary to use service account credentials to reach your Cloud Source Repository.

Step 1: Use the Helm CLI to deploy the chart with your configuration set.

.. code-block:: bash

    $ ./helm install -n cd stable/jenkins -f jenkins/values.yaml --version 1.2.2 --wait
    NAME:   cd
    LAST DEPLOYED: Sun Jul 21 22:53:46 2019
    NAMESPACE: default
    STATUS: DEPLOYED

    RESOURCES:
    ==> v1/ConfigMap
    NAME              DATA  AGE
    cd-jenkins        5     109s
    cd-jenkins-tests  1     109s

    ==> v1/Deployment
    NAME        READY  UP-TO-DATE  AVAILABLE  AGE
    cd-jenkins  1/1    1           1          109s

    ==> v1/PersistentVolumeClaim
    NAME        STATUS  VOLUME                                    CAPACITY  ACCESS MODES  STORAGECLASS  AGE
    cd-jenkins  Bound   pvc-120865ad-ac45-11e9-8966-42010a80013e  100Gi     RWO           standard      109s

    ==> v1/Pod(related)
    NAME                         READY  STATUS   RESTARTS  AGE
    cd-jenkins-546f5559b4-hbgq7  1/1    Running  0         109s

    ==> v1/Role
    NAME                        AGE
    cd-jenkins-schedule-agents  109s

    ==> v1/RoleBinding
    NAME                        AGE
    cd-jenkins-schedule-agents  109s

    ==> v1/Secret
    NAME        TYPE    DATA  AGE
    cd-jenkins  Opaque  2     109s

    ==> v1/Service
    NAME              TYPE       CLUSTER-IP  EXTERNAL-IP  PORT(S)    AGE
    cd-jenkins        ClusterIP  10.0.0.75   <none>       8080/TCP   109s
    cd-jenkins-agent  ClusterIP  10.0.4.134  <none>       50000/TCP  109s

    ==> v1/ServiceAccount
    NAME        SECRETS  AGE
    cd-jenkins  1        109s

    NOTES:
    1. Get your 'admin' user password by running:
    printf $(kubectl get secret --namespace default cd-jenkins -o jsonpath="{.data.jenkins-admin-password}" | base64 --decode);echo
    2. Get the Jenkins URL to visit by running these commands in the same shell:
    export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/component=jenkins-master" -l "app.kubernetes.io/instance=cd" -o jsonpath="{.items[0].metadata.name}")
    echo http://127.0.0.1:8080
    kubectl --namespace default port-forward $POD_NAME 8080:8080

    3. Login with the password from step 1 and the username: admin


    For more information on running Jenkins on Kubernetes, visit:
    https://cloud.google.com/solutions/jenkins-on-container-engine


Step 2: Check deployment / service / pods

.. code-block:: bash

    $ kubectl get pods --show-labels
    NAME                          READY   STATUS    RESTARTS   AGE   LABELS
    cd-jenkins-546f5559b4-hbgq7   1/1     Running   0          17m   app.kubernetes.io/component=jenkins-master,app.kubernetes.io/instance=cd,app.kubernetes.io/managed-by=Tiller,app.kubernetes.io/name=jenkins,helm.sh/chart=jenkins-1.2.2,pod-template-hash=546f5559b4

    $ kubectl get service
    NAME               TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)     AGE
    cd-jenkins         ClusterIP   10.0.0.75    <none>        8080/TCP    4m40s
    cd-jenkins-agent   ClusterIP   10.0.4.134   <none>        50000/TCP   4m40s
    kubernetes         ClusterIP   10.0.0.1     <none>        443/TCP     83m

    $ kubectl get deployment
    NAME         DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
    cd-jenkins   1         1         1            1           4m48s


Step 3: Configure the Jenkins service account to be able to deploy to the cluster.

.. code-block:: bash

    $ kubectl create clusterrolebinding jenkins-deploy --clusterrole=cluster-admin --serviceaccount=default:cd-jenkins
    clusterrolebinding.rbac.authorization.k8s.io/jenkins-deploy created


Step 4: Run the following command to setup port forwarding to the Jenkins UI from the Cloud Shell

.. code-block:: bash

    export POD_NAME=$(kubectl get pod --selector="app.kubernetes.io/component=jenkins-master,app.kubernetes.io/instance=cd" --output jsonpath='{.items[0].metadata.name}')
    kubectl port-forward $POD_NAME 8080:8080 >> /dev/null &


We are using the Kubernetes Plugin so that our builder nodes will be automatically launched as necessary when the Jenkins master requests them.
Upon completion of their work they will automatically be turned down and their resources added back to the clusters resource pool.

Notice that this service exposes ports 8080 and 50000 for any pods that match the selector.
This will expose the Jenkins web UI and builder/agent registration ports within the Kubernetes cluster.
Additionally the jenkins-ui services is exposed using a ClusterIP so that it is not accessible from outside the cluster.

Kubernetes Plugin : https://wiki.jenkins-ci.org/display/JENKINS/Kubernetes+Plugin


Connect to Jenkins
------------------

Step 1: The Jenkins chart will automatically create an admin password for you. To retrieve it, run:

.. code-block:: bash

    $ printf $(kubectl get secret cd-jenkins -o jsonpath="{.data.jenkins-admin-password}" | base64 --decode);echo
    0AwcOxAQDJ


Step 2: To get to the Jenkins user interface, click on the Web Preview button in cloud shell, then click Preview on port 8080.

