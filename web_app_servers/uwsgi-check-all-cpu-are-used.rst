Check All CPUs Are Used
=======================

Some people say that enabling `threads` and `enable-threads` is necessary

in order to distribute ( or utilize ) CPU Affinity to all available CPUs.

But, I don't think it is necessary to set if Application doesn't use thread at all.

ref: https://blog.codeship.com/getting-every-microsecond-out-of-uwsgi/


uWSGI Starting Log
------------------

.. code-block:: text

    *** Starting uWSGI 2.0.18 (64bit) on [Tue Jul  9 11:36:01 2019] ***
    compiled with version: 4.4.7 20120313 (Red Hat 4.4.7-23) on 06 June 2019 18:09:19
    os: Linux-2.6.32-754.14.2.el6.x86_64 #1 SMP Tue May 14 19:35:42 UTC 2019
    nodename: hello-world.test.com
    machine: x86_64
    clock source: unix
    detected number of CPU cores: 8
    current working directory: /mnt/repo/hello_world
    detected binary path: /mnt/repo/hello_world/.venv/bin/uwsgi
    !!! no internal routing support, rebuild with pcre support !!!
    setuid() to 498
    your processes number limit is 31388
    your memory page size is 4096 bytes
    detected max file descriptor number: 96000
    lock engine: pthread robust mutexes
    thunder lock: enabled
    uwsgi socket 0 bound to UNIX address /mnt/logs/hello_world/uwsgi.sock fd 3
    Python version: 3.6.8 (default, May  2 2019, 19:37:42)  [GCC 4.4.7 20120313 (Red Hat 4.4.7-23)]
    PEP 405 virtualenv detected: /var/www/html/hello_world/.venv
    Set PythonHome to /var/www/html/hello_world/.venv
    *** Python threads support is disabled. You can enable it with --enable-threads ***
    Python main interpreter initialized at 0x186ed20
    your server socket listen backlog is limited to 1000 connections
    your mercy for graceful operations on workers is 60 seconds
    mapped 947752 bytes (925 KB) for 12 cores
    *** Operational MODE: preforking ***
    WSGI app 0 (mountpoint='') ready in 0 seconds on interpreter 0x186ed20 pid: 19667 (default app)
    *** uWSGI is running in multiple interpreter mode ***
    spawned uWSGI master process (pid: 19667)
    spawned uWSGI worker 1 (pid: 19669, cores: 1)
    spawned uWSGI worker 2 (pid: 19670, cores: 1)
    spawned uWSGI worker 3 (pid: 19671, cores: 1)
    spawned uWSGI worker 4 (pid: 19672, cores: 1)
    spawned uWSGI worker 5 (pid: 19673, cores: 1)
    spawned uWSGI worker 6 (pid: 19674, cores: 1)
    spawned uWSGI worker 7 (pid: 19675, cores: 1)
    spawned uWSGI worker 8 (pid: 19676, cores: 1)
    spawned uWSGI worker 9 (pid: 19677, cores: 1)
    spawned uWSGI worker 10 (pid: 19678, cores: 1)
    spawned uWSGI worker 11 (pid: 19679, cores: 1)
    spawned uWSGI worker 12 (pid: 19680, cores: 1)
    *** Stats server enabled on 127.0.0.1:1717 fd: 33 ***


Check cpuid where application running
-------------------------------------

.. code-block:: bash

    $ ps -eTo cmd,cpuid,pid,ppid | grep hello_world
    grep hello_world              0 11965  8784
    /var/www/html/hello_world     2 19667  2312
    /var/www/html/hello_world     0 19914 19667
    /var/www/html/hello_world     5 19915 19667
    /var/www/html/hello_world     7 19916 19667
    /var/www/html/hello_world     3 19917 19667
    /var/www/html/hello_world     6 19918 19667
    /var/www/html/hello_world     4 19919 19667
    /var/www/html/hello_world     2 19920 19667
    /var/www/html/hello_world     1 19921 19667
    /var/www/html/hello_world     3 19922 19667
    /var/www/html/hello_world     7 19923 19667
    /var/www/html/hello_world     0 19924 19667
    /var/www/html/hello_world     6 19925 19667
