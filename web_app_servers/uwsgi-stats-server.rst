uWSGI Stats Server
==================

Enable stats server by ini
--------------------------

.. code-block:: ini

    stats=127.0.0.1:1717
    stats-http=true


Access through uwsgitop
-----------------------

Install uwsgitop by PIP and run with stats server address.

.. code-block:: bash

    $ pip install uwsgitop
    $ uwsgitop http://127.0.0.1:1717


Field description: https://github.com/xrmx/uwsgitop#usage


Access through http
-------------------

.. code-block:: bash

    {
        "version":"2.0.18",
        "listen_queue":0,
        "listen_queue_errors":0,
        "signal_queue":0,
        "load":0,
        "pid":19667,
        "uid":498,
        "gid":0,
        "cwd":"/mnt/hello_repo/hello_pingback",
        "locks":[
            {
                "user 0":0
            },
            {
                "signal":0
            },
            {
                "filemon":0
            },
            {
                "timer":0
            },
            {
                "rbtimer":0
            },
            {
                "cron":0
            },
            {
                "thunder":19680
            },
            {
                "rpc":0
            },
            {
                "snmp":0
            }
        ],
        "sockets":[
            {
                "name":"/mnt/hello_logs/hello_pingback/uwsgi.sock",
                "proto":"uwsgi",
                "queue":0,
                "max_queue":0,
                "shared":0,
                "can_offload":0
            }
        ],
        "workers":[
            {
                "id":1,
                "pid":19669,
                "accepting":1,
                "requests":332071,
                "delta_requests":332071,
                "exceptions":0,
                "harakiri_count":0,
                "signals":0,
                "signal_queue":0,
                "status":"idle",
                "rss":0,
                "vsz":0,
                "running_time":579663715,
                "last_spawn":1562697361,
                "respawn_count":1,
                "tx":51254118,
                "avg_rt":1750,
                "apps":[
                    {
                        "id":0,
                        "modifier1":0,
                        "mountpoint":"",
                        "startup_time":0,
                        "requests":332071,
                        "exceptions":0,
                        "chdir":""
                    }
                ],
                "cores":[
                    {
                        "id":0,
                        "requests":332071,
                        "static_requests":0,
                        "routed_requests":0,
                        "offloaded_requests":0,
                        "write_errors":0,
                        "read_errors":0,
                        "in_request":0,
                        "vars":[

                        ],
                        "req_info":                     {

                        }
                    }
                ]
            }
        ]
    }

References
----------

* https://uwsgi-docs.readthedocs.io/en/latest/StatsServer.html
