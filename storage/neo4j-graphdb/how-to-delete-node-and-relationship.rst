Neo4j: How to delete node and relationship
==========================================

Cypher
------

**Delete node by id**

.. code-block:: sql

  MATCH (n) where id(n) = 40
  DETACH DELETE n;


**Delete relationship**

.. code-block:: sql

  MATCH (:Keyword {name:'ipad'})-[r:RELATED]-(:Keyword {name:'ipad pro price'})
  DELETE r

**Delete all nodes**

.. code-block:: sql

  MATCH (n)
  DETACH DELETE n;

  # if need to re-build entire database, stop neo4j/rename database dir/start neo4j
  https://neo4j.com/developer/kb/large-delete-transaction-best-practices-in-neo4j/

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
   
  def _func_delete_kw(tx, name):
      return tx.run('MATCH (n:Keyword {name:$name}) '
                     'DELETE n;', name=name)

  def _func_delete_all_kw(tx):
      return tx.run('MATCH (n:Keyword) '
                     'DETACH DELETE n;')

  def _func_delete_kw_related_edge(tx, kw1, kw2):
      return tx.run('MATCH (:Keyword {name:$kw1})-[r:RELATED]-(:Keyword {name:$kw2}) '
                    'DELETE r', kw1=kw1, kw2=kw2)

  def delete_kw_by_name(name):
      return _op_kw(_func_delete_kw, name)     
       
  def delete_all_kw():
      return _op_kw(_func_delete_all_kw)

  def delete_kw_related_edge(kw1, kw2):
      return tx.run(_func_delete_kw_related_edge, kw1, kw2)
