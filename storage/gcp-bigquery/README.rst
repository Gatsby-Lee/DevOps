Google BigQuery
===============

Dataset
-------

Limitation

 * https://cloud.google.com/bigquery/docs/datasets-intro
 * Geographic location can be set only at creation time only ( immutable and can't be changed later )
 * When copying a table, the datasets containing the source table and destination table must reside in the same location.
 * Dataset names must be unique per project.
 
Table
-----

Limitation

  * https://cloud.google.com/bigquery/quotas
  * There is limit for number of queries, operation and partitions size.
  

External References
-------------------
* https://mvnrepository.com/artifact/com.google.cloud.bigdataoss/gcs-connector/1.7.0-hadoop2
* https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#supported_cloud_dataproc_versions
* https://medium.com/mark-rittman/date-partitioning-and-table-clustering-in-google-bigquery-and-looker-pdts-2bab9ec3be19
* https://medium.com/@tennysusanto/google-cloud-platform-poc-part-1-hadoop-distcp-to-google-cloud-storage-1ef2ad75831d
* https://cloud.google.com/solutions/migration/hadoop/hadoop-gcp-migration-data
* https://cloud.google.com/dataproc/docs/concepts/connectors/install-storage-connector
* https://github.com/GoogleCloudPlatform/bigdata-interop/tree/master/gcs
