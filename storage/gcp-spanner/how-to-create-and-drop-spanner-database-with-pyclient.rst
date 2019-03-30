How to Create/Drop Spanner Database with Python Client
======================================================

Create Database with tables
---------------------------

* Multiple tables can be created with one command.
* Database and Tables can be created with one command.

.. code-block:: python

    from google.cloud import spanner

    def create_database(instance_id, database_id):
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id, ddl_statements=[
            """CREATE TABLE Singers (
                SingerId     INT64 NOT NULL,
                FirstName    STRING(1024),
                LastName     STRING(1024),
                SingerInfo   BYTES(MAX)
            ) PRIMARY KEY (SingerId)""",
            """CREATE TABLE Albums (
                SingerId     INT64 NOT NULL,
                AlbumId      INT64 NOT NULL,
                AlbumTitle   STRING(MAX)
            ) PRIMARY KEY (SingerId, AlbumId),
            INTERLEAVE IN PARENT Singers ON DELETE CASCADE"""
        ])

        operation = database.create()

        print('Waiting for operation to complete...')
        operation.result()

        print('Created database {} on instance {}'.format(
            database_id, instance_id))


Create Database
---------------

.. code-block:: python

    from google.cloud import spanner

    def create_database(instance_id, database_id):
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id)
        operation = database.create()

        print('Waiting for operation to complete...')
            operation.result()

        print('Created database {} on instance {}'.format(
            database_id, instance_id))

Drop Database
---------------

Database will be dropped although there are tables and data.

.. code-block:: python

    from google.cloud import spanner

    def drop_database(instance_id, database_id):
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id)
        database.drop()

        print('Dropped database {} on instance {}'.format(
            database_id, instance_id))
