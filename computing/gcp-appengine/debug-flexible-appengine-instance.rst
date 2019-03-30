Debug Flexible Appengine Instance
==================================

ref: https://cloud.google.com/appengine/docs/flexible/python/debugging-an-instance

Enable / Disable Debug
----------------------

.. code-block:: bash

  # check list of instances
  gcloud app instances list
  # enable debug
  gcloud app instances enable-debug

SSH by gcloud
-------------

.. code-block:: bash

  gcloud app instances ssh --service <service_name> --version <version> <instance_name>
  
  
