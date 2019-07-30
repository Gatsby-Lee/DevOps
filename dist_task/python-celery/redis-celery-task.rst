Redis Celery Task
=================

Define Celery App and Task in a module.
---------------------------------------

redis_celery_task.py


.. code-block:: python

    from celery import Celery

    # the argument of Celery is name of the current module
    celery_app = Celery('redis_celery_task',
                    backend='redis://localhost',
                    broker='redis://localhost',
                    )

    @celery_app.task
    def add(x, y):
        return x + y


Running the Celery worker server
--------------------------------

.. code-block:: bash

    # -A: application
    (.venv) $ ~/DevOps/dist_task/python-celery/samples]$ celery -A redis_celery_task worker --loglevel=info

    -------------- celery@mac11102.local v4.3.0 (rhubarb)
    ---- **** -----
    --- * ***  * -- Darwin-18.7.0-x86_64-i386-64bit 2019-07-29 20:20:33
    -- * - **** ---
    - ** ---------- [config]
    - ** ---------- .> app:         redis_celery_task:0x1092e2450
    - ** ---------- .> transport:   redis://localhost:6379//
    - ** ---------- .> results:     redis://localhost/
    - *** --- * --- .> concurrency: 8 (prefork)
    -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
    --- ***** -----
    -------------- [queues]
                    .> celery           exchange=celery(direct) key=celery


    [tasks]
    . redis_celery_task.add

    [2019-07-29 19:58:11,468: INFO/MainProcess] Connected to redis://localhost:6379//
    [2019-07-29 19:58:11,477: INFO/MainProcess] mingle: searching for neighbors
    [2019-07-29 19:58:12,501: INFO/MainProcess] mingle: all alone
    [2019-07-29 19:58:12,517: INFO/MainProcess] celery@mac11102.local ready.


Check Redis storage
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    127.0.0.1:6379> keys *
    1) "_kombu.binding.celeryev"
    2) "_kombu.binding.celery"
    3) "_kombu.binding.celery.pidbox"
    4) "unacked_mutex"


Calling the `add` task
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> from redis_celery_task import add
    >>> r = add.delay(1,1)
    >>> r
    <AsyncResult: e66505a8-5411-472d-be51-31e5b1296357>
    >>> r.ready()
    True

Check Redis storage
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    127.0.0.1:6379> keys *
    1) "_kombu.binding.celery"
    2) "_kombu.binding.celeryev"
    3) "_kombu.binding.celery.pidbox"
    4) "celery-task-meta-e66505a8-5411-472d-be51-31e5b1296357"
    5) "unacked_mutex"
    127.0.0.1:6379> type "celery-task-meta-e66505a8-5411-472d-be51-31e5b1296357"
    string
    127.0.0.1:6379> get "celery-task-meta-e66505a8-5411-472d-be51-31e5b1296357"
    "{\"status\": \"SUCCESS\", \"result\": 2, \"traceback\": null, \"children\": [], \"task_id\": \"e66505a8-5411-472d-be51-31e5b1296357\", \"date_done\": \"2019-07-30T03:21:40.995689\"}"


Get/Delete results
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> r.get()
    2
    # multiple calles don't raise error
    >>> r.forget()
    >>> r.forget()
    >>> r.forget()


Results in Redis
^^^^^^^^^^^^^^^^

.. code-block:: bash

    127.0.0.1:6379> keys *
    1) "_kombu.binding.celery"
    2) "_kombu.binding.celeryev"
    3) "_kombu.binding.celery.pidbox"
    4) "unacked_mutex"
