k8s connect to pods without exposing
####################################

* https://github.com/Gatsby-Lee/DevOps/blob/master/container_k8s/k8s-gke-play-with-my-container.rst#interact-with-pod-without-exposing-to-public

.. code-block:: bash

    $ kubectl get pods
    NAME                           READY   STATUS    RESTARTS   AGE
    hello-world-85b5d848d9-wjj72   1/1     Running   0          6m34s

    $ kubectl port-forward hello-world-85b5d848d9-wjj72 5000:5000
    Forwarding from 127.0.0.1:5000 -> 5000

    $ curl http://127.0.0.1:5000
    Flask Dockerize
