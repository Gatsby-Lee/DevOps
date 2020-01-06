Networking
##########

netstat
=======

* `-n` : disable reverse DNS lookup
* `-t` : TCP
* `-u` : UDP
* `-l` : LISTEN
* `-p` : show process name/pid and user id

All TCP/UDP connections
-----------------------

.. code-block:: bash

    # List all TCP/UDP connections
    netstat -a

    # List all TCP connections
    netstat -at

    # List all UDP connections
    netstat -au


Only LISTEN TCP/UDP connections
-------------------------------

.. code-block:: bash

    # List LISTEN TCP/UDP connections
    netstat -l

    # List LISTEN TCP connections
    netstat -tl

    # List LISTEN UDP connections
    netstat -ul
