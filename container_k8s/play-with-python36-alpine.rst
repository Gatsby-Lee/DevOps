Play with Python3.6 Alpine
==========================

Pull alpine image
-----------------

.. code-block:: bash

    # Pull latest alpine image
    $ docker pull python:3.7-alpine
    $ docker images
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    python              3.7-alpine          96c5c39abbb6        13 days ago         87MB


Play with python36 container
----------------------------

.. code-block:: bash

    # -i: interactive, -t: tty, --name: name of container
    $ docker run -i -t --name python36 python:3.7-alpine
    Python 3.7.3 (default, Apr 10 2019, 01:29:41)
    [GCC 8.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import sys
    >>> sys.version
    '3.7.3 (default, Apr 10 2019, 01:29:41) \n[GCC 8.3.0]'
