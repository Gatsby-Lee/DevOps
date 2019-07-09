uWSGI config
============

.. code-block:: ini

    [uwsgi]
    project=hello_world
    project-base=/var/www/html/%(project)
    project-log-dir=/mnt/app_logs/%(project)

    ## --- process related
    master=true
    master-fifo=/tmp/%(project)_master_uwsgi.fifo
    # %k is a magic var translated to the number of cpu cores
    processes=%(%k * 3)
    disable-logging=true
    listen=1000
    # the socket ( full path to be safe )
    socket=/tmp/%(project)_uwsgi.sock
    chmod-socket=666
    uid=nginx
    # clear environment on exit
    vacuum=true
    die-on-term=true
    # stats
    stats=127.0.0.1:1717
    stats-http=true

    ## --- application related
    module=flask_web.main:app
    virtualenv=%(project-base)/.venv
