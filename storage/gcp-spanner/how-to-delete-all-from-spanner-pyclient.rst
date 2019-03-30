How to Delete ALL from Spanner with Python Client
=============================================

Delete All
----------

.. code-block:: python

    from google.cloud import spanner
    from google.cloud.spanner import KeySet

    def delete_all(instance_id, database_id):
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id)

        with database.batch() as batch:
            # batch.delete('<table_name>', key_set)
            batch.delete('Singers', KeySet(all_=True))


Changes
-------
* 2018-06-17: tested with python==3.6, google-cloud-spanner==1.4.0
