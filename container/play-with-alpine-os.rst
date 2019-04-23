Play with Alpine OS
===================

Pull alpine image
-----------------

.. code-block:: bash

    # Pull latest alpine image
    $ docker pull alpine:latest

    # Check images
    $ docker images
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    alpine              latest              cdf98d1859c1        13 days ago         5.53MB


Stop / Remove container
-----------------------

.. code-block:: bash

    # Stop container
    $ docker stop alpine_bash

    # Remove container
    $ docker rm alpine_bash
    alpine_bash
    $ docker ps --all
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES


Play with alpine container
--------------------------

.. code-block:: bash

    # Run container with interactive Shell
    # -i: interactive, -t: tty, --name: name of container
    # /bin/sh will be executed.
    $ docker run -i -t --name alpine_bash alpine /bin/sh
    / # date
    Tue Apr 23 04:19:39 UTC 2019
    / # exit

    # After exit, container is not running.
    $ docker ps --all
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                      PORTS               NAMES
    74dda54a3542        alpine              "/bin/sh"           46 seconds ago      Exited (0) 20 seconds ago                       alpine_bash

    # `attach` command connects your terminal’s standard input, output and error to a running container
    # Unable to attach to "not running container
    $ docker attach alpine_bash
    You cannot attach to a stopped container, start it first
    # Restart container / Attach
    $ docker restart alpine_bash
    alpine_bash
    $ docker ps --all
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
    74dda54a3542        alpine              "/bin/sh"           4 minutes ago       Up 4 seconds                            alpine_bash
    $ docker attach alpine_bash
    / # date
    Tue Apr 23 04:24:58 UTC 2019
    / # exit
    $ docker ps --all
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                    PORTS               NAMES
    74dda54a3542        alpine              "/bin/sh"           5 minutes ago       Exited (0) 1 second ago                       alpine_bash



Play with alpine container ( daemon )
-------------------------------------

.. code-block:: bash

    # Run container with deamon mode.
    # -d: --detach
    $ docker run -d -t --name alpine_bash alpine /bin/sh
    6248960b49a74db83fc4df87127510e1be847dd82e52048616485e9ef2051e30
    $ docker ps --all
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
    6248960b49a7        alpine              "/bin/sh"           5 seconds ago       Up 4 seconds                            alpine_bash

    # Run command(exec)
    # -i: interactive ( keep stdin open )
    # -t: allocate terminal
    $ docker exec -i -t alpine_bash /bin/sh
    / # date
    Tue Apr 23 04:34:53 UTC 2019
    / # exit
    $ docker ps --all
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
    6248960b49a7        alpine              "/bin/sh"           6 minutes ago       Up 6 minutes                            alpine_bash

