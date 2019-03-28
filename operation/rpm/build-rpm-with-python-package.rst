Build RPM with Python Package on CentOS 6.x
===========================================

Check if `rpmbuild` is installed
--------------------------------

.. code-block:: bash

  # if bunch of details of the build environment printed,
  # then rpmbuild is installed.
  rpmbuild --showrc


Setup RPM build env
-------------------

* Install packages

.. code-block:: bash

  yum install rpm-build redhat-rpm-config
  yum install git python-devel python-setuptools
  
* Create `build` user and become `build` user

.. code-block:: bash

  $ useradd build
  $ su - build

* Download python package to build RPM ( supervisord is example here )

.. code-block:: bash

  $ mkdir /home/build/python-pkg

  # From github, get the latest package download link
  # https://github.com/Supervisor/supervisor/releases
  $ curl -L https://github.com/Supervisor/supervisor/archive/3.3.5.tar.gz \
    -o /home/build/python-pkg/supervisor-3.3.1.tar.gz


Rerferences
-----------
* https://wiki.centos.org/HowTos/SetupRpmBuildEnvironment
* https://rpmbuild-supervisor.readthedocs.io/en/latest/
* https://docs.python.org/2.0/dist/creating-rpms.html
