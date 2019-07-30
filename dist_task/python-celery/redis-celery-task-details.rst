Redis Celery - Task details
===========================

Let's check what we have in Redis when there is no running workers

Calling Task
------------

.. code-block:: bash

    $ ~/DevOps/dist_task/python-celery/samples]$ python
    Python 3.7.4 (default, Jul  9 2019, 18:13:23)
    [Clang 10.0.1 (clang-1001.0.46.4)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from redis_celery_task import add
    >>> r = add.delay(1,1)


Check What we have in Redis
---------------------------

.. code-block:: bash

    127.0.0.1:6379> keys *
    1) "celery"
    2) "_kombu.binding.celery"
    127.0.0.1:6379> type "celery"
    list
    127.0.0.1:6379> type "_kombu.binding.celery"
    set
    127.0.0.1:6379> smembers "_kombu.binding.celery"
    1) "celery\x06\x16\x06\x16celery"
    127.0.0.1:6379> lindex "celery" 0


Task details in `celery` queue
------------------------------

.. code-block::

    {
        "body":"W1sxLCAxXSwge30sIHsiY2FsbGJhY2tzIjogbnVsbCwgImVycmJhY2tzIjogbnVsbCwgImNoYWluIjogbnVsbCwgImNob3JkIjogbnVsbH1d",
        "content-encoding":"utf-8",
        "content-type":"application/json",
        "headers":{
            "lang":"py",
            "task":"redis_celery_task.add",
            "id":"68924929-27cd-4651-aff2-bdfee02f9dd1",
            "shadow":null,
            "eta":null,
            "expires":null,
            "group":null,
            "retries":0,
            "timelimit":[
                null,
                null
            ],
            "root_id":"68924929-27cd-4651-aff2-bdfee02f9dd1",
            "parent_id":null,
            "argsrepr":"(1, 1)",
            "kwargsrepr":"{}",
            "origin":"gen53578@mac11102.local"
        },
        "properties":{
            "correlation_id":"68924929-27cd-4651-aff2-bdfee02f9dd1",
            "reply_to":"907185b1-1f59-3fc5-a9b2-573ccdfb6d5c",
            "delivery_mode":2,
            "delivery_info":{
                "exchange":"",
                "routing_key":"celery"
            },
            "priority":0,
            "body_encoding":"base64",
            "delivery_tag":"25fd33d3-6ea0-43e1-b75a-aafa860c12e1"
        }
    }


Decoded Body in Task with base64
--------------------------------

.. code-block:: python

    >>> import base64
    >>> base64.b64decode('W1sxLCAxXSwge30sIHsiY2FsbGJhY2tzIjogbnVsbCwgImVycmJhY2tzIjogbnVsbCwgImNoYWluIjogbnVsbCwgImNob3JkIjogbnVsbH1d') 
    b'[[1, 1], {}, {"callbacks": null, "errbacks": null, "chain": null, "chord": null}]'
