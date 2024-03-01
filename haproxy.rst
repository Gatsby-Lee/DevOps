HAProxy
#######

Save Current Stata / Reload
===========================

* setting socket ref:

  * https://cbonte.github.io/haproxy-dconv/1.8/management.html#9.3
  * https://cbonte.github.io/haproxy-dconv/1.8/configuration.html#3.1-stats%20socket

* load-server-state-from-file ref: https://cbonte.github.io/haproxy-dconv/1.8/configuration.html#4-load-server-state-from-file
* server-state-file ref: https://cbonte.github.io/haproxy-dconv/1.8/configuration.html#server-state-file

Sample HAProxy Config
---------------------

.. code-block:: cfg

    global
        ...
        # Binds a UNIX socket to <path>
        stats socket /var/run/haproxy.sock
        # Specifies the path to the file containing state of servers.
        server-state-file /etc/haproxy/haproxy.state
        ...

    defaults
        ...
        # This directive points HAProxy to a file where server state from previous
        #  running process has been saved
        load-server-state-from-file global
        ...

Reload HAProxy with previous state
----------------------------------

.. code-block:: bash

    socat /var/run/haproxy.sock - <<< "show servers state" > /etc/haproxy/haproxy.state; service haproxy reload; rm -f /etc/haproxy/haproxy.state
