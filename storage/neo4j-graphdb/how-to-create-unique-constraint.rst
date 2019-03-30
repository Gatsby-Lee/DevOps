Neo4j: How to use Unique Constraint
===================================

List of indexes
---------------

.. code-block:: sql

  CALL db.indexes;

Create / Drop Unique Constraint
-------------------------------

.. code-block:: sql

  CREATE CONSTRAINT ON (k:Keyword) ASSERT k.name IS UNIQUE;
  DROP CONSTRAINT ON (k:Keyword) ASSERT k.name IS UNIQUE;
