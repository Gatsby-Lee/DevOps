Terraform Common
################

* https://github.com/terraform-providers/terraform-provider-google/blob/master/CHANGELOG.md


How to install Terrafom on Mac
==============================

Install with brew
-----------------

.. code-block:: bash

  brew install terraform


Install with binary
-------------------

* Download binary from https://www.terraform.io/downloads.html


How To constrain the provider version
=====================================

.. code-block:: bash

    $ cat providers.tf
    terraform {
        required_providers {
            google = "2.20.1" # or google = "<3.0"
        }
    }
