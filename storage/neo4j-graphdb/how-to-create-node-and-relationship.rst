Neo4j: How to create node and relationship
==========================================


Cypher
------

**Create Node**

* Create Node with labled with *Keyword* without any property

.. code-block:: sql

  CREATE (:Keyword)


**Create Node with property**

* Keyword is *Label*
* name is a propety of Keyword

.. code-block:: sql

  CREATE (:Keyword { name: 'apple ipad' }),(:Keyword { name: 'ipad' })

**Create Relationship**

.. code-block:: sql

  MATCH (a:Keyword {name:'apple ipad'}),(b:Keyword {name:'ipad'})
  CREATE (a)-[:RELATED]->(b);


Python Driver and Cypher
------------------------

* Transaction and ContextManager are recommended.


.. code-block:: python

  from neo4j.v1 import GraphDatabase
  
  def get_connection():
      return GraphDatabase.driver('bolt://<hostname>:7687', auth=('<username>', '<password>'))
  
  def _op_kw(func_run, *args):
      conn = None
      try:
          conn = get_connection()
          with conn.session() as session:
              session.write_transaction(func_run, *args)
      finally:
          conn.close()
   
  def _func_create_kw(tx, name):
      return tx.run("MERGE (n:Keyword {name:$name}) "
                    "RETURN id(n);", name=name).single().value()

  def _func_create_kw_related_edge(tx, kw1, kw2):
      return tx.run("MATCH (a:Keyword {name:$kw1}),(b:Keyword {name:$kw2}) "
                    "MERGE (a)-[:RELATED]->(b);", kw1=kw1, kw2=kw2)

  def create_kw(kw):
      _op_kw(_func_create_kw, kw)

  def create_kw_related_edge(kw1, kw2):
      _op_kw(_func_create_kw_related_edge, kw1, kw2)
