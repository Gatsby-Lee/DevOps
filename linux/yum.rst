YUM
###

yum --showduplicates list java-1.8.0-openjdk
============================================

.. code-block:: bash

    yum --showduplicates list java-1.8.0-openjdk
    Loaded plugins: fastestmirror
    Loading mirror speeds from cached hostfile
    Installed Packages
    java-1.8.0-openjdk.x86_64                                                                                         1:1.8.0.181-3.b13.el6_10                                                                                          @updates
    Available Packages
    java-1.8.0-openjdk.x86_64                                                                                         1:1.8.0.171-8.b10.el6_9                                                                                           base
    java-1.8.0-openjdk.x86_64                                                                                         1:1.8.0.181-3.b13.el6_10                                                                                          updates
    java-1.8.0-openjdk.x86_64                                                                                         1:1.8.0.191.b12-0.el6_10                                                                                          updates
    java-1.8.0-openjdk.x86_64                                                                                         1:1.8.0.201.b09-1.el6_10                                                                                          updates
    java-1.8.0-openjdk.x86_64                                                                                         1:1.8.0.201.b09-2.el6_10                                                                                          updates
    java-1.8.0-openjdk.x86_64                                                                                         1:1.8.0.212.b04-0.el6_10                                                                                          updates
    java-1.8.0-openjdk.x86_64                                                                                         1:1.8.0.222.b10-0.el6_10                                                                                          updates
    java-1.8.0-openjdk.x86_64                                                                                         1:1.8.0.232.b09-1.el6_10                                                                                          updates


Install specific version
========================

ref: https://unix.stackexchange.com/questions/189020/how-can-i-instruct-yum-to-install-a-specifc-version-of-openjdk

.. code-block:: bash

    yum install java-1.8.0-openjdk-1:1.8.0.181-3.b13.el6_10


Downgrade to specific version
=============================

If RPM is in repo.

.. code-block:: bash

    yum downgrade java-1.8.0-openjdk-1.8.0.181-3.b13.el6_10.x86_64 java-1.8.0-openjdk-headless-1.8.0.181-3.b13.el6_10.x86_64


Restrict package to be upgraded
===============================

* ref: https://access.redhat.com/solutions/98873


Install yum plugin
------------------

.. code-block:: bash

    yum install yum-plugin-versionlock


Add packages to versionlock
---------------------------

.. code-block:: bash

    # It's possible directly to add into /etc/yum/pluginconf.d/versionlock.list
    $ yum versionlock add java-1.8.0-openjdk
    $ yum versionlock add java-1.8.0-openjdk-headless

    # Check list in versionlock
    $ yum versionlock list
    Loaded plugins: fastestmirror, versionlock
    1:java-1.8.0-openjdk-1.8.0.181-3.b13.el6_10.*
    1:java-1.8.0-openjdk-headless-1.8.0.181-3.b13.el6_10.*
    versionlock list done

    # Try to upgrade to confirm
    $ yum update java-1.8.0-openjdk
    Loaded plugins: fastestmirror, versionlock
    Setting up Update Process
    Loading mirror speeds from cached hostfile
    No Packages marked for Update


Delete packages from versionlock
--------------------------------

.. code-block:: bash

    $ yum versionlock delete 1:java-1.8.0-openjdk-1.8.0.181-3.b13.el6_10.*
    Loaded plugins: fastestmirror, versionlock
    Deleting versionlock for: 1:java-1.8.0-openjdk-1.8.0.181-3.b13.el6_10.*
    versionlock deleted: 1

    $ yum versionlock list
    Loaded plugins: fastestmirror, versionlock
    1:java-1.8.0-openjdk-headless-1.8.0.181-3.b13.el6_10.*
    versionlock list done


Export installed package with CSV format
========================================

https://stackoverflow.com/questions/104055/how-to-list-the-contents-of-a-package-using-yum

.. code-block:: bash

  # print all supported query tags
  rpm --querytags
  # print installed packages
  rpm -qa --queryformat "%{NAME}.%{ARCH},%{VERSION}-%{RELEASE},%{VENDOR}\n" | sort -t\; -k 1
