InnoDB Buffer Pool
==================

Use cases
---------
* Reducing disk IO by storing(caching) data and indexes in memory

What is "Buffer Pool"
-----------------------------
* The memory area holding cached InnoDB data for both tables and indexes.


How InnoDB Buffer Pool works?
-----------------------------
* keeping frequently-used blocks in the buffer
* structure: a list consisted of two lists, a **new** and **old** list
  * By default, **37%** of the list is reserved for the **old** list.
* if new info is accessed that does not exist in the **new** and **old** list,
  * it is placed at the top of **old** list
  * the **oldest** one in the **old** list is removed.
  * in consequence, everything else move back one position in the **old** list.
* if info is accessed that exists in the **old** list,
  * it is moved to the top of **new** list.
  * in consequence, everything else move back one position in the **new** list.
  * Possiable Question)
    * Then, is the one in the **old** list removed? ( not sure yet )

related config variables
------------------------
### buffer pool
* innodb_buffer_pool_size
* innodb_buffer_pool_instances

### **old** list related
* innodb_old_blocks_pct
* innodb_old_blocks_time

References
------------------------
* https://mariadb.com/kb/en/library/xtradbinnodb-buffer-pool/
* https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_buffer_pool_size
* https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_buffer_pool_instances

* https://dev.mysql.com/doc/refman/8.0/en/glossary.html#glos_buffer_pool
* page
* in-memory database
* https://dev.mysql.com/doc/refman/8.0/en/glossary.html#glos_adaptive_hash_index
* https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_adaptive_hash_index
* https://dev.mysql.com/doc/refman/8.0/en/innodb-memcached.html
* how to investigate contention issue?
 * https://stackoverflow.com/questions/21117927/how-do-you-investigate-contention-issues-on-mysql?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
* lock: https://stackoverflow.com/questions/3230693/get-locked-tables-in-mysql-query
* show open tables: https://dev.mysql.com/doc/refman/8.0/en/show-open-tables.html
* https://michael.bouvy.net/blog/en/2015/01/18/understanding-mysql-innodb-buffer-pool-size/
