Redis Celery - Send Task to Queue
=================================

Celery App
----------

.. code-block:: python

    celery_app = Celery('redis_celery_task',
                        backend='redis://localhost',
                        broker='redis://localhost',
                        )

Send Task - sent to default queue, `celery`
-------------------------------------------

.. code-block:: python

    r = celery_app.send_task('mytask.add', args=[1, 2])


.. code-block:: bash

    127.0.0.1:6379> keys *
    1) "celery"
    2) "_kombu.binding.celery"


.. code-block:: json

    {
        "body":"W1sxLCAyXSwge30sIHsiY2FsbGJhY2tzIjogbnVsbCwgImVycmJhY2tzIjogbnVsbCwgImNoYWluIjogbnVsbCwgImNob3JkIjogbnVsbH1d",
        "content-encoding":"utf-8",
        "content-type":"application/json",
        "headers":{
            "lang":"py",
            "task":"mytask.add",
            "id":"7f6c7fff-b582-4bfd-be34-27d0e37f6abc",
            "shadow":null,
            "eta":null,
            "expires":null,
            "group":null,
            "retries":0,
            "timelimit":[
                null,
                null
            ],
            "root_id":"7f6c7fff-b582-4bfd-be34-27d0e37f6abc",
            "parent_id":null,
            "argsrepr":"[1, 2]",
            "kwargsrepr":"{}",
            "origin":"gen81961@mac11102.local"
        },
        "properties":{
            "correlation_id":"7f6c7fff-b582-4bfd-be34-27d0e37f6abc",
            "reply_to":"82e5b6ba-8685-333b-80ce-290f3bcaa957",
            "delivery_mode":2,
            "delivery_info":{
                "exchange":"",
                "routing_key":"celery"
            },
            "priority":0,
            "body_encoding":"base64",
            "delivery_tag":"3a166d96-9562-4387-92e1-f38841ec013b"
        }
    }

Send Task - sent to `fasttrack` queue
-------------------------------------

.. code-block:: python

    r = celery_app.send_task('mytask.add', args=[1, 2],
                             queue='fasttrack')


.. code-block:: bash

    127.0.0.1:6379> keys *
    1) "_kombu.binding.fasttrack"
    2) "fasttrack"


.. code-block:: json

    {
        "body":"W1sxLCAyXSwge30sIHsiY2FsbGJhY2tzIjogbnVsbCwgImVycmJhY2tzIjogbnVsbCwgImNoYWluIjogbnVsbCwgImNob3JkIjogbnVsbH1d",
        "content-encoding":"utf-8",
        "content-type":"application/json",
        "headers":{
            "lang":"py",
            "task":"mytask.add",
            "id":"dbcf505f-a540-4942-ab06-0bc73c9ed2b6",
            "shadow":null,
            "eta":null,
            "expires":null,
            "group":null,
            "retries":0,
            "timelimit":[
                null,
                null
            ],
            "root_id":"dbcf505f-a540-4942-ab06-0bc73c9ed2b6",
            "parent_id":null,
            "argsrepr":"[1, 2]",
            "kwargsrepr":"{}",
            "origin":"gen82074@mac11102.local"
        },
        "properties":{
            "correlation_id":"dbcf505f-a540-4942-ab06-0bc73c9ed2b6",
            "reply_to":"eb7da16d-dff7-3c98-8e59-74ebf2ecb9cf",
            "delivery_mode":2,
            "delivery_info":{
                "exchange":"",
                "routing_key":"fasttrack"
            },
            "priority":0,
            "body_encoding":"base64",
            "delivery_tag":"045d7bbb-f2ea-4405-9a3f-68d2cfee53a0"
        }
    }
