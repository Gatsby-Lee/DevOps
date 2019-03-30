Google Cloud - BigTable
=======================

BigTable Overall
----------------
* A single value in each row is indexed with value called `row key`.
* high read and write throughput at low latency.
* it is an ideal data source for MapReduce operations

BigTable Emulator
-----------------
* ref: https://cloud.google.com/bigtable/docs/emulator

Install BigTable cbt
--------------------
* ref: https://github.com/Gatsby-Lee/ClouldInfraWiki/blob/master/gcp/install-google-cloud-bigtable-cbt-by-yum.rst

Performance
-----------
* https://cloud.google.com/bigtable/docs/performance

HelloWorld with Python Client
-----------------------------
* ref:

  * https://cloud.google.com/bigtable/docs/samples-python-hello
  * https://googleapis.github.io/google-cloud-python/latest/bigtable



Row keys
--------
* ref: https://cloud.google.com/bigtable/docs/schema-design
* keep your row keys reasonably short
* no longer recommend using a hashed row key
* if row key includes multiple values, separate those values with a delimiter.
