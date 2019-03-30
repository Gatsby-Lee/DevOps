How to Configure Network Connector
==================================

Configuration file
------------------
* neo4j.conf

Enable connection from all remotes
----------------------------------

Uncomment or Set ``dbms.connectors.default_listen_address=0.0.0.0``

.. code-block:: cfg

  dbms.connectors.default_listen_address=0.0.0.0

External References
-------------------
* https://neo4j.com/docs/operations-manual/current/configuration/connectors/
