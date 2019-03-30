Neo4j scatch
============

Naming Convention
-----------------
* ref: https://neo4j.com/docs/developer-manual/current/cypher/syntax/naming/
* Node labels: Camel case, beginning with an upper-case character
* Relationship types: UPPER CASE, using underscore to separate words ( e.g. OWNS_VEHICLE )



Concepts
--------
* ref: https://neo4j.com/docs/developer-manual/current/introduction/graphdb-concepts/
Node (representing object) ::
  * Having **properties** key-value-pairs
  * Having **labels** representing their different roles in your domain. 

Relationships::
  * providing directed, named, semantically relevant connections between two node-entities
  * always having a direction, a type, a start node, a end node
  * able to have properties
  * In most cases, relationships have "quantitative properties", such as weights, costs, distances, ratings, time intervals, strengths or etc.

Labels::
  * A label is a named graph construct that is used to group nodes into sets
  * All nodes labeled with the same label belongs to the same set
  * A node may be labeled with any number of labels, including none ( label is optional )

No broken links::
  * Unable to delete a node without also deleting its associated relationships


Data Model Transformation
--------------------------
Node ( each node is row in table )::
  * label: table name
  * properties: column

key / index / unique::
  * Add unique constraints for business primary keys
  * Add indexes for frequent lookup attributes


Bi-directional relationships
--------------
ref : https://graphaware.com/neo4j/2013/10/11/neo4j-bidirectional-relationships.html

* Neo4j can be traversed in both directions with the same speed
* direction can be completely ignored.
* no need to create two different relationships between nodes
* e.g) MATCH (neo)-[:PARTNER]-(partner) same as MATCH (neo)-[:PARTNER]->(partner) and MATCH (neo)<-[:PARTNER]-(partner)


Create syntax
-----------------
* ref: https://neo4j.com/docs/developer-manual/current/cypher/clauses/create/

**Create constraint**

ref: https://www.quackit.com/neo4j/tutorial/neo4j_create_a_constraint_using_cypher.cfm

.. code-block:: sql

  CREATE CONSTRAINT ON (a:Keyword) ASSERT a.name IS UNIQUE;


**Create Keyword**


.. code-block:: sql

  CREATE (:Keyword { name: 'apple ipad', word_ct: 2 }),(:Keyword { name: 'ipad', word_ct: 1 }),(:Keyword { name: 'apple ipad pro', word_ct: 3 }),(:Keyword { name: 'apple ipad pro price', word_ct: 4 });

**Create Word**

.. code-block:: SQL

  CREATE (:Word { name: 'apple' }), (:Word { name: 'ipad' }),(:Word { name: 'pro' }),(:Word { name: 'price' });

**Create Relationship between Keywords**

.. code-block:: SQL

  MATCH (a:Keyword {name:'apple ipad'}),(b:Keyword {name:'ipad'}),(c:Keyword {name:'apple ipad pro'}),(d:Keyword {name:'apple ipad pro price'})
  CREATE (a)-[:RELATED]->(b),(a)-[:RELATED]->(c),(c)-[:RELATED]->(d);

**Create Relationship between Keyword and Word**

.. code-block:: SQL

  MATCH (k:Keyword {name:'apple ipad'}),(w1:Word {name:'apple'}),(w2:Word {name:'ipad'})
  CREATE (k)-[:INCLUDE]->(w1), (k)-[:INCLUDE]->(w2);

  MATCH (k:Keyword {name:'ipad'}),(w1:Word {name:'ipad'})
  CREATE (a)-[:INCLUDE]->(b)

  MATCH (k:Keyword {name:'apple ipad pro'}),(w1:Word {name:'apple'}),(w2:Word {name:'ipad'}),(w3:Word {name:'pro'})
  CREATE (k)-[:INCLUDE]->(w1), (k)-[:INCLUDE]->(w2), (k)-[:INCLUDE]->(w3)

  MATCH (k:Keyword {name:'apple ipad pro price'}),(w1:Word {name:'apple'}),(w2:Word {name:'ipad'}),(w3:Word {name:'pro'}),(w4:Word {name:'price'})
  CREATE (k)-[:INCLUDE]->(w1),(k)-[:INCLUDE]->(w2),(k)-[:INCLUDE]->(w3),(k)-[:INCLUDE]->(w4);
  
Delete
--------------------

**Delete Relationship**

.. code-block::

  MATCH (:Keyword {name:'apple ipad pro price'})-[r:RELATED]-(:Keyword {name:'apple ipad pro price'}) 
  DELETE r

**Delete Node by ID**

.. code-block::

  MATCH (n) where id(n) = 40 DETACH DELETE n


Select
------------------

**Select All**

.. code-block:: sql

  MATCH (n) RETURN n


**Select by Keyword name**

.. code-block:: sql

  MATCH (a:Keyword),(b:Keyword)
  WHERE a.name = 'apple ipad' AND b.name = 'ipad'
  RETURN a,b

.. code-block:: sql

  MATCH (a:Keyword {name:'apple ipad'}),(b:Keyword {name:'ipad'})
  RETURN a,b

**Select Keywords related to A**

.. code-block:: sql

  MATCH (a:Keyword {name:'apple ipad'})-[:RELATED]-(b:Keyword)
  RETURN b

.. code-block:: sql

  MATCH (a:Keyword {name:'apple ipad'})-[:RELATED*0..1]-(b:Keyword)
  RETURN b

**Select Keywords related to A within two hop**

.. code-block:: sql

  MATCH (a:Keyword {name:'apple ipad'})-[:RELATED*0..2]-(b:Keyword)
  RETURN b

