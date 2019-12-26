Trouble Shooting
================

Error: No such image
--------------------

.. code-block:: bash

    $ docker images
    REPOSITORY                 TAG                 IMAGE ID            CREATED             SIZE
    hello-world                latest              e38bc07ac18e        12 months ago       1.85kB
    parrotstream/impala-kudu   latest              e1e15b122016        20 months ago       2.03GB
    centos                     6                   89fb9d1ed93b        3 years ago         203MB

    $ docker rmi -f $(docker images -q)
    Error: No such image: e38bc07ac18e
    Error: No such image: e1e15b122016
    Error: No such image: 89fb9d1ed93b

    # clean up / restart
    sudo service docker stop
    sudo rm -rf /var/lib/docker
    sudo service docker start
    
