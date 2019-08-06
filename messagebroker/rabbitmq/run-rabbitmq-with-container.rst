Run RabbitMQ with container
===========================

ref: https://hub.docker.com/_/rabbitmq


.. code-block:: bash

    # without WEB UI
    $ docker run -d -p 5672:5672 -p --hostname my-rabbit --name some-rabbit rabbitmq:3
    # with WEB UI - http://localhost:15672/ ( username/paswd : guest )
    $ docker run -d -p 5672:5672 -p 15672:15672 --hostname my-rabbit --name some-rabbit rabbitmq:management
