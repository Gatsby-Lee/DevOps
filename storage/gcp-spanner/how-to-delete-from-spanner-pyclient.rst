How to Delete from Spanner with Python Client
=============================================

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

Delete by PrimaryKey
--------------------

.. code-block:: python

    from google.cloud import spanner
    from google.cloud.spanner import KeySet

    def delete_by_pk(instance_id, database_id):
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id)

        to_delete = KeySet(keys=[
            (1,),
            (2,)
        ])

        with database.batch() as batch:
            batch.delete('Singers', to_delete)


Changes
-------
* 2018-06-17: tested with python==3.6, google-cloud-spanner==1.4.0
