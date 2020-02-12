Timezone in Impala
##################

Noticed changes in Impala 2.x to 3.x
====================================

PDT is not consided as valid Timezone
-------------------------------------

* wanted to take out hard-coded timezone in timezone_db.cc to give timezone source option to admin. Default is IANA

  * https://issues.apache.org/jira/browse/IMPALA-3307 ( https://github.com/apache/impala/commit/17749dbcfc51ebe67c269ce812749d1845e47e7a )
  * https://impala.apache.org/docs/build/html/topics/impala_timezone.html
  * https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
  * https://github.com/apache/impala/blob/branch-3.2.0/be/src/exprs/timezone_db.cc
  * https://github.com/apache/impala/blob/branch-2.12.0/be/src/exprs/timezone_db.cc
  * https://github.com/google/cctz


.. code-block:: bash

    [hadoop1-nn.test.com:21000] default> select to_utc_timestamp(now(), 'PDT'), to_utc_timestamp(now(), 'PST'), to_utc_timestamp(now(), 'PST8PDT');
    Query: select to_utc_timestamp(now(), 'PDT'), to_utc_timestamp(now(), 'PST')
    Query submitted at: 2020-02-12 08:42:32 (Coordinator: http://hadoop1-nn.test.com:25000)
    Query progress can be monitored at: http://hadoop1-nn.test.com:25000/query_plan?query_id=d14372ce12e03f43:a7c5345600000000
    +--------------------------------+--------------------------------+------------------------------------+
    | to_utc_timestamp(now(), 'pdt') | to_utc_timestamp(now(), 'pst') | to_utc_timestamp(now(), 'pst8pdt') |
    +--------------------------------+--------------------------------+------------------------------------+
    | 2020-02-12 08:46:06.442360000  | 2020-02-12 16:46:06.442360000  | 2020-02-12 16:46:06.442360000      |
    +--------------------------------+--------------------------------+------------------------------------+
    WARNINGS: UDF WARNING: Unknown timezone 'PDT'

    Fetched 1 row(s) in 0.12s


Setting customizing time zones
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

* https://docs.cloudera.com/runtime/7.0.3/impala-sql-reference/topics/impala-custom-timezones.html
