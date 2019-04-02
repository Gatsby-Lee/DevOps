iptables
========

Insert rule in specific line
---------------------------

First, figure out line number

.. code-block:: bash

  iptables -L -n --line-numbers


-I is for insertion, 23 is line number. Existing one will be pushed down.

.. code-block:: bash

  iptables -I INPUT 23 -p tcp --dport 5222 -j ACCEPT
