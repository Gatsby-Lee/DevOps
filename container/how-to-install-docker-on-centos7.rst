how-to-install-docker-on-centos7
================================

refs: https://docs.docker.com/install/linux/docker-ce/centos/


1. Remove any old Docker
------------------------

.. code-block:: bash

    sudo yum remove docker \
        docker-client \
        docker-client-latest \
        docker-common \
        docker-latest \
        docker-latest-logrotate \
        docker-logrotate \
        docker-engine


2. Setup Docker YUM repository
------------------------------

Install necessary RPM packages


.. code-block:: bash

    sudo yum install -y yum-utils \
        device-mapper-persistent-data \
        lvm2



Add YUM repository

.. code-block:: bash

    sudo yum-config-manager \
        --add-repo \
        https://download.docker.com/linux/centos/docker-ce.repo


3. Install Docker
-----------------

.. code-block:: bash

    sudo yum install docker-ce docker-ce-cli containerd.io


4. Start Docker service
-----------------------

.. code-blcok:: bash

    sudo systemctl start docker



5. Setup docker group
---------------------

refs: https://docs.docker.com/install/linux/linux-postinstall/

.. code-blcok:: bash

    sudo groupadd docker
    sudo usermod -aG docker $USER


6. Docker Login
---------------------

.. code-blcok:: bash

    docker login


7. Test Docker
--------------------

.. code-block:: bash

    docker run hello-world

