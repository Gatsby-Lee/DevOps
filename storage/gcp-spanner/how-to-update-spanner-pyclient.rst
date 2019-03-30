How to Update data in Spanner with Python Client
================================================

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


Update by PrimaryKey
--------------------

* If primary key of table is consited of multiple columns, then those columns have to be listed as well.
* If matched row doesn't exist, `google.api_core.exceptions.NotFound` exception raised

.. code-block:: python

    def update_by_pk(instance_id, database_id):
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id)

        with database.batch() as batch:
            # SingerId is used as key to find row
            # if matched row is found, then LastName column is updated.
            # if not found, then google.api_core.exceptions.NotFound exception raise.
            batch.update(
                table='Singers',
                columns=('SingerId', 'LastName'),
                values=[
                    (5, u'hello world'),
                    (8, u'hello world2'),
                ])


Changes
-------
* 2018-06-17: tested with python==3.6, google-cloud-spanner==1.4.0
