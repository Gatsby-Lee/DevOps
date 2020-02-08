Kudo CLI
########

List / Remove / Describe tables
===============================

.. code-block:: bash

    $ kudu table
    Usage: /usr/lib/kudu/bin/kudu table <command> [<args>]

    <command> can be one of the following:
            delete   Delete a table
          describe   Describe a table
              list   List tables
        locate_row   Locate which tablet a row belongs to
     rename_column   Rename a column
      rename_table   Rename a table
              scan   Scan rows from a table
              copy   Copy table data to another table

    # list
    $ kudu table list <master_nodename>
    impala::impala_kudu.test3
    impala::impala_kudu.test
    impala::impala_kudu.test2

    # delete
    $ kudu table delete <master_nodename> impala::impala_kudu.test3

    # describe
    $ kudu table describe <master_nodename> impala::impala_kudu.test2
    TABLE impala::impala_kudu.test2 (
        name STRING NOT NULL,
        PRIMARY KEY (name)
    )
    REPLICAS 3
