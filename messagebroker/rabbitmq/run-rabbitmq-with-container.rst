Run RabbitMQ with container
===========================

ref: https://hub.docker.com/_/rabbitmq

.. code-block:: bash

    docker run -d -p 5672:5672 --hostname my-rabbit --name some-rabbit rabbitmq:3

