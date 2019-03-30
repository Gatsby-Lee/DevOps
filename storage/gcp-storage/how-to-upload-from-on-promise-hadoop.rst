How to Upload from on-promise Hadoop
====================================

Environments
------------
* CDH 5.15
* java version "1.7.0_79"

Required
--------
* GCS connector
* .p12 key from service account
* Bucket in Google Cloud Storage ( GCS ) with name "hadoop-storage"

Download / Setup gcs-connnector
-------------------------------
* pick / download GCS connnector complied with java version you use.
* https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop2-latest.jar
  
* copy downloaded gcs connector to /usr/lib/hadoop-mapreduce/ in all nodes
* and generate symbolic link


.. code-block:: sh

  $ cp gcs-connector-1.7.0-hadoop2.jar /usr/lib/hadoop-mapreduce/
  $ ln -s /usr/lib/hadoop-mapreduce/gcs-connector-1.7.0-hadoop2.jar /usr/lib/hadoop-mapreduce/gcs-connector.jar
  
  
Download / Setup p12 key
------------------------
* create service account / p12 key
* copy downloaded p12 key
* generate symbolic link


.. code-block:: sh

  $ cp gcp-development1-36f62e64656f.p12 /etc/hadoop/conf/
  $ ln -s /etc/hadoop/conf/gcp-development1-36f62e64656f.p12 /etc/hadoop/conf/gcp-hadoop.p12
  

Update core-site.xml
--------------------

.. code-block:: xml

    <property>
      <name>fs.gs.impl</name>
      <value>com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem</value>
    </property>
    <property>
      <name>fs.gs.project.id</name>
      <value>your-ascii-google-project-id</value>
    </property>
    <property>
      <name>fs.gs.system.bucket</name>
      <value>some-bucket-your-project-owns</value>
    </property>
    <property>
      <name>fs.gs.working.dir</name>
      <value>/</value>
    </property>
    <property>
      <name>fs.gs.auth.service.account.enable</name>
      <value>true</value>
    </property>
    <property>
      <name>fs.gs.auth.service.account.email</name>
      <value>your-service-account-email@developer.gserviceaccount.com</value>
    </property>
    <property>
      <name>fs.gs.auth.service.account.keyfile</name>
      <value>/path/to/hadoop/conf/gcs-hadoop.p12</value>
    </property>
