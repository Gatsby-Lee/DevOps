Redis
=====

Spec
----
* Single thread ( process one command )
* support collections

Do NOT
------
* use `keys`
* use `flushall`

SCAN / HSCAN
------------

**HSCAN <key>**
**SCAN <key>**

.. code-block:: bash

  hscan "hash:proxy_ip_status" 0 match "*" COUNT 1000

External References
-------------------
* http://joygram.info/wordpress/?p=93

