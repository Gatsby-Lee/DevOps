How to Fetch from Spanner
=========================


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

Snapshot.read
-------------

*Read by Primary key*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* If primary key of table is consited of multiple columns, then those columns have to be listed as well.
* `KeySet` is used as **key** which matches to `Primary key`, so it has to have values for all columns in `Primary key`

.. code-block:: python

    from google.cloud import spanner
    from google.cloud.spanner import KeySet

    def fetch_with_read(instance_id, database_id):

        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id)

        # List `Primary key` for the wanted row
        to_fetch = KeySet(keys=[(1,), (10,), ])

        with database.snapshot() as snapshot:
            results = snapshot.read(
                table='Singers',
                # columns have to have all columns consisting of `Primary key`
                columns=('SingerId', 'FirstName', 'LastName',),
                keyset=to_fetch)

        for row in results:
            print(u'SingerId: {}, FirstName: {}, LastName: {}'.format(*row))


*Read all*
^^^^^^^^^^

.. code-block:: python

    from google.cloud import spanner
    from google.cloud.spanner import KeySet

    def fetch_all_read(instance_id, database_id):

        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id)

        to_fetch = KeySet(all_=True)

        with database.snapshot() as snapshot:
            results = snapshot.read(
                table='Singers',
                columns=('SingerId', 'FirstName', 'LastName',),
                keyset=to_fetch)

        for row in results:
            print(u'SingerId: {}, FirstName: {}, LastName: {}'.format(*row))


*Read all with 15sec stable*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import datetime
    from google.cloud import spanner
    from google.cloud.spanner import KeySet

    def read_stale_data(instance_id, database_id):

        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id)

        staleness = datetime.timedelta(seconds=15)

        with database.snapshot(exact_staleness=staleness) as snapshot:
            results = snapshot.read(
                table='Singers',
                columns=('SingerId', 'FirstName', 'LastName',),
                keyset=KeySet(all_=True))

            for row in results:
                print(u'SingerId: {}, AlbumId: {}, AlbumTitle: {}'.format(*row))



Snapshot.execute_sql
--------------------

*Query*
^^^^^^^

.. code-block:: python

    from google.cloud import spanner

    def query_data(instance_id, database_id):
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id)

        with database.snapshot() as snapshot:
            results = snapshot.execute_sql(
                'SELECT SingerId, FirstName, LastName FROM Singers')

            for row in results:
                print(u'SingerId: {}, AlbumId: {}, AlbumTitle: {}'.format(*row))


*Query with Parameter*
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from google.cloud import spanner
    from google.cloud.spanner import param_types

    def query_data(instance_id, database_id):
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id)

        with database.snapshot() as snapshot:
            results = snapshot.execute_sql(
                'SELECT SingerId, FirstName, LastName FROM Singers WHERE SingerId=@singer_id',
                params={'singer_id': 1},
                param_types={'singer_id': param_types.INT64}
            )


*Query all with 15sec stable*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import datetime
    from google.cloud import spanner
    from google.cloud.spanner import KeySet

    def read_stale_data(instance_id, database_id):

        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id)

        staleness = datetime.timedelta(seconds=15)

        with database.snapshot(exact_staleness=staleness) as snapshot:
            results = snapshot.execute_sql(
                'SELECT SingerId, FirstName, LastName FROM Singers')

            for row in results:
                print(u'SingerId: {}, AlbumId: {}, AlbumTitle: {}'.format(*row))
