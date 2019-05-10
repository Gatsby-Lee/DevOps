Setup GCP Python OSX
====================

Download / Install SDK ( gcloud )
---------------------------------

* Download https://cloud.google.com/sdk/docs/ ( It will be downloaded to ~\Downloads )
* unzip downloaded SDK:: tar -xvzf google-cloud-sdk-*.tar.gz
* ./google-cloud-sdk/install.sh
* ./google-cloud-sdk/bin/gcloud init
* PATH will be updated. In order to apply updated path, source ~/.bash_profile


Install / Remove components
---------------------------

ref: https://cloud.google.com/sdk/docs/components

.. code-block:: bash

  $ gcloud components list
  $ gcloud components install app-engine-python
  $ gcloud components remove app-engine-python
