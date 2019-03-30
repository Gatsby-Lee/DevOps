How to load data into neo4j
===========================

* ``neo4j-admin import`` has replaced ``neo4j-import``

Using Cypher's ``Load CSV``
---------------------------
* CSV format: https://neo4j.com/docs/developer-manual/3.3/cypher/clauses/load-csv/#csv-file-format
* Related setting in neo4j.conf::
  
    dbms.security.allow_csv_import_from_file_urls=true
    dbms.directories.import=import

    # minimum 4G if data size is big
    dbms.memory.heap.initial_size=4g
    dbms.memory.heap.max_size=4g

    # ( 50% of physical memory )- ( heap memory ) = recommended mememory size ( for neo4j dedicated machine )
    dbms.memory.pagecache.size=30g

* Notes

  * ``Neo.ClientError.Schema.ConstraintValidationFailed`` ERROR can happen.
  * ``WITH row WHERE row[0] IS NOT NULL`` can be used to skip null value.
  * ``USE PERIODIC COMMIT=1000`` can be used to speed up. It can reduce number of hitting disk to commit changes by grouping multiple operations into transactions. ( default: 1000 )


Use of Cypher's ``Load CSV``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

content in CSV

.. code-block:: text

  printer wireless adapter,3
  shopping london,2
  how do independent insurance agents get paid,7
  ...

Cypher

.. code-block:: sql

  # option 1: using `create` - ( not recommend, if unique constraint exists and is violated, it will fail. )
  USING PERIODIC COMMIT 1000000
  LOAD CSV FROM 'file:///keywords.txt' AS row
  WITH row WHERE row[0] IS NOT NULL
  CREATE (:Keyword { name: row[0], tct: row[1] });

  # option 2: using `merge` to prevent creating duplicated node ( recommended )
  USING PERIODIC COMMIT 1000000
  LOAD CSV FROM "file:///keywords.txt" AS row
  WITH row WHERE row[0] IS NOT NULL
  MERGE (:Keyword { name: row[0], tct: row[1] });




Using ``neo4j-admin import``
----------------------------
* coming

some commands might need to be used
------------------------------------

.. code-block:: sql

  # check list of indexes
  CALL db.indexes;

  # If necessary, set unique constraint first. ( e.g. CREATE / DROP )
  CREATE CONSTRAINT ON (k:Keyword) ASSERT k.name IS UNIQUE;
  DROP CONSTRAINT ON (k:Keyword) ASSERT k.name IS UNIQUE;

  # If necessary, clean up all existing Nodes
  MATCH (n) DETACH DELETE n;
  # if need to re-build entire database, stop neo4j/rename database dir/start neo4j
  https://neo4j.com/developer/kb/large-delete-transaction-best-practices-in-neo4j/

  # If necessary, create/drop index
  CREATE INDEX ON :Keyword(name);
  DROP INDEX ON :Keyword(name);
  
  # Return count of nodes
  MATCH (n) RETURN count(*)

  # Test loading CSV without creating Node
  LOAD CSV FROM "file:///keywords.txt" AS row
  WITH row
  RETURN row
  LIMIT 10;

  # list queries
  CALL dbms.listQueries()
  # kill query
  CALL dbms.killQuery(queryId) 
  :queries

External References
-------------------
* https://neo4j.com/blog/bulk-data-import-neo4j-3-0/
* https://neo4j.com/blog/importing-data-neo4j-via-csv/
* https://neo4j.com/docs/operations-manual/current/tutorial/import-tool/
* https://neo4j.com/docs/developer-manual/3.3/cypher/clauses/load-csv/
* http://blog.comperiosearch.com/blog/2015/02/04/csv-import-tricks-neo4j/
* https://neo4j.com/blog/import-10m-stack-overflow-questions/
* https://neo4j.com/blog/bulk-data-import-neo4j-3-0/
* https://dzone.com/articles/load-csv-neo4j-quickly-and
* https://neo4j.com/developer/guide-import-csv/
