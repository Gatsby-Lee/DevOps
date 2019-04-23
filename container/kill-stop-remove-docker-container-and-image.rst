Stop / Kill / Remove Docker Container and Image
================================================

Stop Container ( Gracefully )
-----------------------------

.. code-block:: bash

    docker stop <container_id|container_name> 
    # stop all running containers
    docker stop $(docker ps -a -q)


Kill Container
--------------

.. code-block:: bash

    docker kill <container_id|container_name> 
    # kill all running containers
    docker kill $(docker ps -a -q)


Remove Container
-----------------

.. code-block:: bash

    # Remove one or more containers.
    docker rm <container_id|container_name>
    # Remove all containers
    docker rm $(docker ps -a -q)


Remove Image
-------------

.. code-block:: bash

    # Remove one or more images.
    docker rmi <image_id|repository:tag>
    # Remove all containers
    docker rmi $(docker images -q)

