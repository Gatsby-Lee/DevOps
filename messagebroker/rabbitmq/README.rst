RabbitMQ
========

Run with Docker Container
-------------------------

.. code-block::  bash

    # without WEB UI
    $ docker run -d -p 5672:5672 -p --hostname my-rabbit --name some-rabbit rabbitmq:3
    # with WEB UI - http://localhost:15672/ ( username/paswd : guest )
    $ docker run -d -p 5672:5672 -p 15672:15672 --hostname my-rabbit --name some-rabbit rabbitmq:management


Recommended Reads before deploying to Prod
------------------------------------------

* https://www.rabbitmq.com/tutorials/tutorial-one-python.html
* https://www.rabbitmq.com/documentation.html
* https://www.rabbitmq.com/confirms.html
* https://www.rabbitmq.com/production-checklist.html
* https://www.rabbitmq.com/monitoring.html
