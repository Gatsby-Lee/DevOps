Add / Drop KUDU partition from Impala
=====================================


DROP range partition
--------------------

NOTE: Dropping Partition also deletes data as well.


.. code-block:: SQL

  alter table kudu_table DROP RANGE PARTITION 201701 <= VALUES < 201702;
  alter table kudu_table DROP RANGE PARTITION 202001 <= VALUES;

External Resources
------------------
* https://impala.apache.org/docs/build/html/topics/impala_kudu.html
