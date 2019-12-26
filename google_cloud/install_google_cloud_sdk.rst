Install Google Cloud SDK
########################

Red Hat / CentOS
================

* ref: https://cloud.google.com/sdk/docs/downloads-yum


1. Setup YUM repo file
----------------------

.. code-block:: text

    sudo tee -a /etc/yum.repos.d/google-cloud-sdk.repo << EOM
    [google-cloud-sdk]
    name=Google Cloud SDK
    baseurl=https://packages.cloud.google.com/yum/repos/cloud-sdk-el7-x86_64
    enabled=1
    gpgcheck=1
    repo_gpgcheck=1
    gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
        https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
    EOM


2. Install package
------------------

.. code-block:: bash

    dnf install google-cloud-sdk

