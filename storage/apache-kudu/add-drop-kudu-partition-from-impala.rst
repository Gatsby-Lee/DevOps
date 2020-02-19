Add / Drop KUDU partition from Impala
#####################################


Add / Drop range partition
====================

NOTE: Dropping Partition also deletes data as well.

.. code-block:: SQL

  alter table <table_name> DROP RANGE PARTITION 201701 <= VALUES < 201702;
  alter table <table_name> DROP RANGE PARTITION 202001 <= VALUES;

  alter table <table_name> ADD RANGE 201701 <= VALUES < 201702;
  alter table <table_name> ADD RANGE PARTITION 202001 <= VALUES;


External Resources
==================

* https://impala.apache.org/docs/build/html/topics/impala_kudu.html
