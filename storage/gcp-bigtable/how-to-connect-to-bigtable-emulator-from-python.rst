How to connect to BigTable emulator for Python
==============================================

.. code-block:: python

    import os
    from google.auth.credentials import AnonymousCredentials
    from google.cloud.bigtable import Client

    # this is not necessary if $(gcloud beta emulators bigtable env-init) run.
    os.environ["BIGTABLE_EMULATOR_HOST"] = 'localhost:8086'

    client = Client(project='IGNORE_ENVIRONMENT_PROJECT',
                    credentials=AnonymousCredentials(),
                    admin=True)
    table = client.instance("fake_instance").table("some_table")
    table.create()  # No error here, which is good!
