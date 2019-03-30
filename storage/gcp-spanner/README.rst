Google Spanner
==============

Required
--------

* Download Service API key(JSON) from Google Cloud Console
* Set Service API key location

.. code-block:: bash

  export GOOGLE_APPLICATION_CREDENTIALS="<location_of_service_api_json>"


Getting Started in Python Spanner Client API
--------------------------------

Install python Client
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

  $ pip install google-cloud-spanner

Create Spanner Client
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  >>> from google.cloud import spanner
  >>> client = spanner.Client()


Data Type
---------
* ref: https://cloud.google.com/spanner/docs/data-types


External References
-------------------
* API reference: http://google-cloud-python.readthedocs.io/en/latest/spanner/api-reference.html
* Python Example: https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/spanner/cloud-client/snippets.py
* SQL syntax: https://cloud.google.com/spanner/docs/query-syntax
* Python Client code for Spanner: https://github.com/GoogleCloudPlatform/google-cloud-python/tree/master/spanner
* Session: https://github.com/GoogleCloudPlatform/google-cloud-python/blob/master/docs/spanner/advanced-session-pool-topics.rst
* Tutorial: https://github.com/hostirosti/til-about-cloudspanner
* right PK: https://medium.com/google-cloud/cloud-spanner-choosing-the-right-primary-keys-cd2a47c7b52d

Loading data
^^^^^^^^^^^^
* https://cloudplatform.googleblog.com/2018/07/cloud-spanner-adds-import-export-functionality-to-ease-data-movement.html

