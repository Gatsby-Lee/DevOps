Apache KUDU
===========

Check Health
------------

.. code-block:: bash

  sudo -u kudu kudu cluster ksck <kudu-lead-master-hostname>

Scale Limitation
----------------

* ref: https://kudu.apache.org/docs/known_issues.html#_scale
* Recommended maximum number of tablet servers is 100.
* Recommended maximum number of masters is 3.
* Recommended maximum amount of stored data, post-replication and post-compression, per tablet server is 8TB.
* Recommended maximum number of tablets per tablet server is 2000, post-replication.
* Maximum number of tablets per table for each tablet server is 60, post-replication, at table-creation time.

References
-----------
* https://kudu.apache.org/docs/command_line_tools_reference.html
* https://kudu.apache.org/docs/configuration_reference.html
