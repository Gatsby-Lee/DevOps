CDH Kudu related Known Issues
#############################

CDH 6.3.2
=========

* https://docs.cloudera.com/documentation/enterprise/6/release-notes/topics/rg_cdh_630_known_issues.html#cdh620_ki_kudu


Failed to create KUDU table without setting HMS in hive-site.xml
----------------------------------------------------------------

Details about failure
>>>>>>>>>>>>>>>>>>>>>

* executed creating KUDU table command through Impala
* `ERROR: IllegalArgumentException: null` is raised.
* In KUDU, the table is created, but in Impala, the created table is missing.

.. code-block:: bash

    ***********************************************************************************
    Welcome to the Impala shell.
    (Impala Shell v3.2.0-cdh6.3.2 (1bb9836) built on Fri Nov  8 07:25:47 PST 2019)

    To see live updates on a query's progress, run 'set LIVE_SUMMARY=1;'.
    ***********************************************************************************
    impala> create table test(name string, primary key(name) ) stored as kudu;
    Query: create table test(name string, primary key(name) ) stored as kudu
    ERROR: IllegalArgumentException: null

Why does it happen?
>>>>>>>>>>>>>>>>>>>

There is bug in KuduTable.java

.. code-block:: bash

    # hmsUris can be empty if HMS is configured to use direct connection to Metastore.
    # However, this logic can't accecpt the case
    # https://github.com/apache/impala/blob/branch-3.3.0/fe/src/main/java/org/apache/impala/catalog/KuduTable.java#L214
    public static boolean isHMSIntegrationEnabledAndValidate(String kuduMasters,
        String hmsUris) throws ImpalaRuntimeException {
        Preconditions.checkNotNull(hmsUris);
        Preconditions.checkArgument(!hmsUris.isEmpty());

    # Fixed version.
    public static boolean isHMSIntegrationEnabledAndValidate(String kuduMasters,
        String hmsUris) throws ImpalaRuntimeException {
        if (hmsUris == null || hmsUris.isEmpty()) {
            return false;
        }


Fixs / Related to linkes
>>>>>>>>>>>>>>>>>>>>>>>>

* https://issues.apache.org/jira/browse/IMPALA-8974
* https://issues.apache.org/jira/browse/IMPALA-9264
* https://gerrit.cloudera.org/#/c/14398/
