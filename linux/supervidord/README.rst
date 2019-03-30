supervisord
===========


Installation
------------

Installation by pip
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

  pip install supervisor
  mkdir /etc/supervisord.conf.d
  echo_supervisord_conf > /etc/supervisord.conf
  # uncomment [include] section
  # nodaemon mode ( -n )
  supervisord -c /etc/supervisord.conf -n
  # able to use supervisor
  supervisorctl -c /etc/supervisord.conf


Setup init
----------

For CentOS6: ( not completed )
^^^^^^^^^^^^

src: https://github.com/Supervisor/initscripts

.. code-block:: bash

  chmod 755 /etc/init.d/supervidord
  chkconfig --add supervidord


Base setting supervisord.conf
-----------------------------

.. code-block:: conf

    [supervisord]
    nodaemon=true

    [supervisorctl]

    [inet_http_server]
    port = 127.0.0.1:9001

    [rpcinterface:supervisor]
    supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

