YUM / RPM
=========

* https://stackoverflow.com/questions/104055/how-to-list-the-contents-of-a-package-using-yum


Export installed package with CSV format
----------------------------------------

.. code-block:: bash

  # print all supported query tags
  rpm --querytags
  # print installed packages
  rpm -qa --queryformat "%{NAME}.%{ARCH},%{VERSION}-%{RELEASE},%{VENDOR}\n" | sort -t\; -k 1
  
