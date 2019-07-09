Increase TCP backlog limit
==========================


502 bad gateway Error from Nginx + uWSGI
----------------------------------------

.. code-block:: text

    $ cat /var/log/nginx/error.log

    2019/07/09 09:53:54 [error] 10491#0: *36884857 connect() to unix:/tmp/uwsgi.sock failed
    (11: Resource temporarily unavailable) while connecting to upstream, ...


uWSGI options
-------------

.. code-block:: bash

    $ uwsgi --help | grep "\-\-listen"
    -l|--listen                             set the socket listen queue size
    --listen-queue-alarm                    raise the specified alarm when the socket backlog queue is full


Increase kernel level limit
---------------------------

By default, uWSGI has default limit 100 for socket listen backlog.

Also, there is system level limit on Linux socket and TCP connection listen queue, the deault is 128.

.. code-block:: bash

    # system level limit
    $ cat /proc/sys/net/core/somaxconn
    128


uWSGI's one can't be greater than kernel's, so limit in kernel has to be increased first.

.. code-block:: bash

    # This config will be reset to default if machine reboots

    $ echo 4096 > /proc/sys/net/core/somaxconn
    $ cat /proc/sys/net/core/somaxconn
    4096

    OR

    sysctl -w net.core.somaxconn=4096


In order to make it as permant change, `net.core.somaxconn=4096` has to be added into `/etc/sysctl.conf`


Increase uWSGI level limit
--------------------------

Add into `listsen=1000` into uwsgi.ini or set on command line like `uwsgi --listen=1000`
