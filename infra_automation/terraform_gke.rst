Terraform GKE
#############

How to enable `Stackdriver Kubernetes Engine Monitoring`
========================================================

* terraform ver: v0.12.18
* google provider ver: v2.20.1
* ref: https://cloud.google.com/monitoring/kubernetes-engine/installing

.. code-block:: text

  # - Enable 'Stackdriver Kubernetes Engine Monitoring'
  # - Disable 'Legacy Stackdriver Monitoring'
  # - Disable 'Legacy Stackdriver Logging'
  logging_service = "logging.googleapis.com/kubernetes"
  monitoring_service = "monitoring.googleapis.com/kubernetes"
