How to insert into Spanner table
================================

Table Schema
------------
* SingerId is **PK**

.. code-block:: sql

  CREATE TABLE Singers (
    SingerId     INT64 NOT NULL,
    FirstName    STRING(1024),
    LastName     STRING(1024),
    SingerInfo   BYTES(MAX)
  ) PRIMARY KEY (SingerId)

Important Note
--------------
* STRING columns uses a text string. ( str in Python 3; unicode in Python 2 )


insert /  insert_or_update / replace
------------------------------------

*insert*
^^^^^^^^

* **FAIL** if any of the records in insertion already exists in table.

*insert_or_update*
^^^^^^^^^^^^^^^^^^
 
* similar to **UPSERT** ( update or insert )
* if row doesn't exist, insert row
* if row exists,

  - update columns with supplied columns and valuses
  - preserve values for not supplied columns.

*replace*
^^^^^^^^^

* similar to **insert_or_update**

* if row exists,

  - update columns with supplied columns and valuses
  - update columns with NULL value for not supplied columns.


.. code-block:: python

  def insert_data(instance_id, database_id):
      spanner_client = spanner.Client()
      instance = spanner_client.instance(instance_id)
      database = instance.database(database_id)

      # when context exits without raising an exception, API call will be made.
      # if context is not used, then batch.commit() need to be executed to make API call.
      with database.batch() as batch:
          # batch.insert
          # batch.insert_or_update
          # batch.replace
          batch.insert(
              table='Singers',
              columns=('SingerId', 'FirstName', 'LastName',),
              values=[
                  (1, u'Marc', u'Richards'),
                  (2, u'Catalina', u'Smith')])
  

Changes
-------
* 2018-06-17: tested with python==3.6, google-cloud-spanner==1.4.0
