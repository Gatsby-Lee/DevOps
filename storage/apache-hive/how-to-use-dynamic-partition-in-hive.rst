How to use Dynamic Partition in Hive
=========================


Config for dynamic partition
----------------------------

.. code-block::

  set hive.exec.dynamic.partition=true;
  set hive.exec.dynamic.partition.mode=nonstrict;
  set hive.exec.max.dynamic.partitions=1000;
  set hive.exec.max.dynamic.partitions.pernode=1000;
  
