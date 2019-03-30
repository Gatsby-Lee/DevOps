Working with Neo4j Enterprise from Graphstack.io
================================================

Download
------------
* https://graphstack.io/

Installation
------------
* Uncompress ``tar.gz`` 

.. code-block:: bash

  tar -xvzf neo4j-enterprise-3.3.5-unix.tar.gz

Configuration
-------------
* Update ``conf/neo4j.conf``

Run neo4j server
----------------

**Possible commands:**

.. code-block:: bash

  ./bin/neo4j 
  Usage: neo4j { console | start | stop | restart | status | version }

**Console mode:**

.. code-block:: bash

  ./bin/neo4j console
  
**Daemon mode:**

.. code-block:: bash

  ./bin/neo4j start
