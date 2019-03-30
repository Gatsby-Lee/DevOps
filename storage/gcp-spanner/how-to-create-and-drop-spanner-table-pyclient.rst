How to Create/Drop Table in Spanner with Python Client
=============================================================

CREATE table
------------

Data Tyle: https://cloud.google.com/spanner/docs/data-types

.. code-block:: python

    from google.cloud import spanner

    def create_table(instance_id, database_id):
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id)

        operation = database.update_ddl(ddl_statements=[
            """CREATE TABLE Singers (
                SingerId     INT64 NOT NULL,
                FirstName    STRING(1024),
                LastName     STRING(1024),
                SingerInfo   BYTES(MAX)
            ) PRIMARY KEY (SingerId)""",
        ])

        print('Waiting for operation to complete...')
        operation.result()

        print('Created table on database {} on instance {}'.format(
            database_id, instance_id))




DROP table
----------

.. code-block:: python

  from google.cloud import spanner

  def drop_table(instance_id, database_id):
      spanner_client = spanner.Client()
      instance = spanner_client.instance(instance_id)
      database = instance.database(database_id)

      # this executes specified ddl_statements.
      # DROP TABLE DDL returns None
      database.update_ddl(ddl_statements=[
          """DROP TABLE Albums""",
      ])

      print('Dropped table on database {} on instance {}'.format(
          database_id, instance_id))

Changes
-------
* 2018-06-17: tested with python==3.6, google-cloud-spanner==1.4.0
