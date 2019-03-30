Find
====


Remove files
------------

* https://stackoverflow.com/questions/11289551/argument-list-too-long-error-for-rm-cp-mv-commands

.. code-block:: bash

  # delete matched one
  find /mnt/tmp/ -maxdepth 1 -name 'pattern_to_delete_*' -delete

  # delete older than 7 days
  find /mnt/tmp/ -maxdepth 1 -name '*log*' -mtime +7 -delete
