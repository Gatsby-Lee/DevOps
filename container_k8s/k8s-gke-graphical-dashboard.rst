Google Kubernetes - Graphical Dashboard
=======================================

ref: https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/

grant cluster level permissions
-------------------------------

.. code-block:: bash

    kubectl create clusterrolebinding cluster-admin-binding --clusterrole=cluster-admin --user=$(gcloud config get-value account)


Create Dashboard service
------------------------

.. code-block:: bash

    kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v1.10.1/src/deploy/recommended/kubernetes-dashboard.yaml


Update yaml
-----------

.. code-block:: bash

    # Change type: ClusterIP to type: NodePort
    kubectl -n kube-system edit service kubernetes-dashboard


Get token
---------

To log in to the Kubernetes dashboard you must authenticate using a token.
Use a token allocated to a service account, such as the namespace-controller.

.. code-block:: bash

    kubectl -n kube-system describe $(kubectl -n kube-system \
    get secret -n kube-system -o name | grep namespace) | grep token:


Open connection
---------------

.. code-block:: bash

    kubectl proxy --port 8081


Then use the Cloud Shell Web preview feature to change ports to 8081:

To get to the dashboard, remove /?authuser=0 and append the URL with the following:

::

    /api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/#!/overview?namespace=default

