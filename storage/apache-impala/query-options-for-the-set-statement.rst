Impala Query Options for the SET Statement
==========================================

To see current option in Impala CLI
-----------------------------------

https://www.cloudera.com/documentation/enterprise/5-8-x/topics/impala_set.html

.. code-block:: sql

    [localhost:21000] > set;
    Query options (defaults shown in []):
      ABORT_ON_DEFAULT_LIMIT_EXCEEDED: [0]
      ...
      V_CPU_CORES: [0]

    Shell Options
      LIVE_PROGRESS: False
      LIVE_SUMMARY: False

    Variables:
      CUTOFF: 3
      TABLE_NAME: staging_table


Parquet related
---------------

**PARQUET_FILE_SIZE**

Specifies the maximum size of each Parquet data file produced by Impala INSERT statements.

.. code-block:: sql

  -- 128 megabytes.
  set PARQUET_FILE_SIZE=134217728;
  -- 512 megabytes.
  set PARQUET_FILE_SIZE=512m;
  -- 1 gigabyte.
  set PARQUET_FILE_SIZE=1g;


**PARQUET_READ_STATISTICS**

The PARQUET_READ_STATISTICS query option controls whether to read statistics from Parquet files and use them during query processing.

In Impala Query Profile, by checking **NumStatsFilteredRowGroups**

.. code-block:: sql

  -- enable (default)
  set PARQUET_READ_STATISTICS=1;
  -- disable (default)
  set PARQUET_READ_STATISTICS=0;



External References
-------------------
* https://www.cloudera.com/documentation/enterprise/latest/topics/impala_query_options.html
