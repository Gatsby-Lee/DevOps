Configuring Google Cloud Storage Connectivity
#############################################

Enviroments
============

* CentOS 6.10
* CDH 5.16.2
* OpenJDK 1.8.181 ( JDK 8 is required as minimum to use GCS connector )


Download / Copy to
==================

* ref: https://cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage
* Download GCS connector and copy to `/usr/lib/hadoop/`


Add properties in core-site.xml ( all nodes - wn,nn )
=====================================================

* ref: https://github.com/GoogleCloudPlatform/bigdata-interop/blob/master/gcs/INSTALL.md
* below config is a sample using Service Account
* HDFS services have to be restarted ( hadoop-hdfs-namenode, hadoop-hdfs-datanode )

.. code-block:: xml

  <property>
    <name>fs.AbstractFileSystem.gs.impl</name>
    <value>com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS</value>
  </property>
  <property>
    <name>fs.gs.project.id</name>
    <value></value>
  </property>
  <property>
    <name>google.cloud.auth.service.account.enable</name>
    <value>true</value>
  </property>
  <property>
    <name>google.cloud.auth.service.account.json.keyfile</name>
    <value>service_account_local_path</value>
  </property>


Access GCS
==========

.. code-block:: bash

  hdfs dfs -ls gs://<gcs-bucket-name>


References
==========

* https://github.com/GoogleCloudPlatform/bdutil/blob/master/conf/hadoop2/gcs-core-template.xml
