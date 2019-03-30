Apache Hive
===========

This is Query Execution engine, not storeage engine.


Hive query option of contiune on error
--------------------------------------

.. code-block::

  hive --hiveconf hive.cli.errors.ignore=true -e 'select (*) from a;select (*) from b'


Hive --hiveconf / --hivevar
---------------------------

* --hiveconf : recommended for hive setting.
 
  * the value can be fetched by ${hiveconf:name} if wanted to use in query. - for this, use --hivevar


* --hivevar : recommended for passing user variables.

  * the value can be fetched by ${name}


.. code-block::

  hive --hiveconf hive.cli.errors.ignore=true --hiveconf ym=2010 --hivevar table_name=test -e "select (*) from ${table_name} where ym=${hiveconf:ym}"


External References
-------------------
* https://www.cloudera.com/documentation/enterprise/latest/PDF/cloudera-hive.pdf
* https://cwiki.apache.org/confluence/display/Hive/Configuration+Properties
* https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Cli
