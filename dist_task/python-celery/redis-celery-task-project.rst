Redis Celery Task Project
=========================

Define Celery App and Task separately
-------------------------------------

.. code-block:: bash

    $ tree celery_project/
    celery_project/
    |-- __init__.py
    |-- celery_tasks.py
    `-- celery_worker.py

    0 directories, 3 files


celery_worker.py

.. code-block:: python

    from celery import Celery

    celery_app = Celery('celery_project',
                        backend='redis://localhost',
                        broker='redis://localhost',
                        include=['celery_project.celery_tasks'])

    # Optional configuration, see the application user guide.
    celery_app.conf.update(
        result_expires=3600,
    )

    if __name__ == '__main__':
        celery_app.start()


celery_Tasks.py

.. code-block:: python

    from .celery_worker import celery_app

    @celery_app.task
    def add(x, y):
        return x + y


    @celery_app.task
    def mul(x, y):
        return x * y


Running the Celery worker server
--------------------------------

.. code-block:: bash

    $ ~/DevOps/dist_task/python-celery/samples]$ celery -A celery_project.celery_worker worker --loglevel=info

    -------------- celery@mac11102.local v4.3.0 (rhubarb)
    ---- **** -----
    --- * ***  * -- Darwin-18.7.0-x86_64-i386-64bit 2019-07-29 21:05:49
    -- * - **** ---
    - ** ---------- [config]
    - ** ---------- .> app:         celery_project:0x10c50e6d0
    - ** ---------- .> transport:   redis://localhost:6379//
    - ** ---------- .> results:     redis://localhost/
    - *** --- * --- .> concurrency: 8 (prefork)
    -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
    --- ***** -----
    -------------- [queues]
                    .> celery           exchange=celery(direct) key=celery


    [tasks]
    . celery_project.celery_tasks.add
    . celery_project.celery_tasks.mul
    . celery_project.celery_tasks.xsum

    [2019-07-29 21:05:49,486: INFO/MainProcess] Connected to redis://localhost:6379//
    [2019-07-29 21:05:49,497: INFO/MainProcess] mingle: searching for neighbors
    [2019-07-29 21:05:50,522: INFO/MainProcess] mingle: all alone
    [2019-07-29 21:05:50,539: INFO/MainProcess] celery@mac11102.local ready.


Calling the `add` task
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> from celery_project.celery_tasks import add
    >>> r = add.delay(2,2)
    >>> r.ready()
    True
    >>> r.get()
    4
    >>> r.forget()
