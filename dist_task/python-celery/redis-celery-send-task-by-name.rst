Redis Celery - Send Task by Name
================================

Use Cases
---------

* Different languages between Task producer and consumers
* Different code bases between Task producer and consumers


IMPORTANT
---------

Make sure that backend, broker configuration is matched to worker.


Define Celery APP
-----------------

Task has to have `name`

.. code-block:: python

    from celery import Celery

    celery_app = Celery('redis_celery_task',
                        backend='redis://localhost',
                        broker='redis://localhost',
                        )


    @celery_app.task(name='mytask.add')
    def add(x, y):
        return x + y



Running the Celery worker server
--------------------------------

Check registered Tasks with `mytask.add`

.. code-block:: bash

    # -A: application
    (.venv) $ ~/DevOps/dist_task/python-celery/samples]$ celery -A redis_celery_task_with_name worker --loglevel=info

    -------------- celery@mac11102.local v4.3.0 (rhubarb)
    ---- **** -----
    --- * ***  * -- Darwin-18.7.0-x86_64-i386-64bit 2019-07-29 22:04:00
    -- * - **** ---
    - ** ---------- [config]
    - ** ---------- .> app:         redis_celery_task:0x1016f97d0
    - ** ---------- .> transport:   redis://localhost:6379//
    - ** ---------- .> results:     redis://localhost/
    - *** --- * --- .> concurrency: 8 (prefork)
    -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
    --- ***** -----
    -------------- [queues]
                    .> celery           exchange=celery(direct) key=celery


    [tasks]
    . mytask.add

    [2019-07-29 22:04:00,302: INFO/MainProcess] Connected to redis://localhost:6379//
    [2019-07-29 22:04:00,313: INFO/MainProcess] mingle: searching for neighbors
    [2019-07-29 22:04:01,334: INFO/MainProcess] mingle: all alone
    [2019-07-29 22:04:01,349: INFO/MainProcess] celery@mac11102.local ready.
    [2019-07-29 22:04:30,425: INFO/MainProcess] Received task: mytask.add[628709cd-8d6f-409d-861e-d0a437234648]
    [2019-07-29 22:04:30,435: INFO/ForkPoolWorker-6] Task mytask.add[628709cd-8d6f-409d-861e-d0a437234648] succeeded in 0.007305294999998324s: 3


Calling the `add` task by name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create Celery Instance and send_task with name `mytask.add`

.. code-block:: python

    from celery import Celery

    celery_app = Celery('redis_celery_task',
                        backend='redis://localhost',
                        broker='redis://localhost',
                        )


    r = celery_app.send_task('mytask.add', args=[1, 2])
    print(r.get())
    r.forget()
