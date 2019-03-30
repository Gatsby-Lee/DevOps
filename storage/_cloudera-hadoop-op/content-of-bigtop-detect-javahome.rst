Content of `bigtop-detect-javahome`
===================================

Source Code
-----------

.. code-block:: bash

    $ cat /usr/lib/bigtop-utils/bigtop-detect-javahome
    #!/usr/bin/env bash

    # Licensed to the Apache Software Foundation (ASF) under one or more
    # contributor license agreements.  See the NOTICE file distributed with
    # this work for additional information regarding copyright ownership.
    # The ASF licenses this file to You under the Apache License, Version 2.0
    # (the "License"); you may not use this file except in compliance with
    # the License.  You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.


    # Override JAVA_HOME in the file below if you want to disable
    # automatic JAVA_HOME detection
    BIGTOP_DEFAULTS_DIR=${BIGTOP_DEFAULTS_DIR-/etc/default}
    [ -n "${BIGTOP_DEFAULTS_DIR}" -a -r ${BIGTOP_DEFAULTS_DIR}/bigtop-utils ] && . ${BIGTOP_DEFAULTS_DIR}/bigtop-utils

    JAVA6_HOME_CANDIDATES=(
        '/usr/lib/j2sdk1.6-sun'
        '/usr/lib/jvm/java-6-sun'
        '/usr/lib/jvm/java-1.6.0-sun-1.6.0'
        '/usr/lib/jvm/j2sdk1.6-oracle'
        '/usr/lib/jvm/j2sdk1.6-oracle/jre'
        '/usr/java/jdk1.6'
        '/usr/java/jre1.6'
    )

    OPENJAVA6_HOME_CANDIDATES=(
        '/usr/lib/jvm/java-1.6.0-openjdk'
        '/usr/lib/jvm/jre-1.6.0-openjdk'
    )

    JAVA7_HOME_CANDIDATES=(
        '/usr/java/jdk1.7'
        '/usr/java/jre1.7'
        '/usr/lib/jvm/j2sdk1.7-oracle'
        '/usr/lib/jvm/j2sdk1.7-oracle/jre'
        '/usr/lib/jvm/java-7-oracle'
    )

    OPENJAVA7_HOME_CANDIDATES=(
        '/usr/lib/jvm/java-1.7.0-openjdk'
        '/usr/lib/jvm/java-7-openjdk'
    )

    JAVA8_HOME_CANDIDATES=(
        '/usr/java/jdk1.8'
        '/usr/java/jre1.8'
        '/usr/lib/jvm/j2sdk1.8-oracle'
        '/usr/lib/jvm/j2sdk1.8-oracle/jre'
        '/usr/lib/jvm/java-8-oracle'
    )

    OPENJAVA8_HOME_CANDIDATES=(
        '/usr/lib/jvm/java-1.8.0-openjdk'
        '/usr/lib/jvm/java-8-openjdk'
    )

    MISCJAVA_HOME_CANDIDATES=(
        '/Library/Java/Home'
        '/usr/java/default'
        '/usr/lib/jvm/default-java'
        '/usr/lib/jvm/java-openjdk'
        '/usr/lib/jvm/jre-openjdk'
    )

    # Note that the JDK versions recommended for production use in CDH
    # may not reflect the current recommendations for Apache Bigtop
    case ${BIGTOP_JAVA_MAJOR} in
        6) JAVA_HOME_CANDIDATES=(${JAVA6_HOME_CANDIDATES[@]})
        ;;
        7) JAVA_HOME_CANDIDATES=(${JAVA7_HOME_CANDIDATES[@]} ${OPENJAVA7_HOME_CANDIDATES[@]})
        ;;
        8) JAVA_HOME_CANDIDATES=(${JAVA8_HOME_CANDIDATES[@]} ${OPENJAVA8_HOME_CANDIDATES[@]})
        ;;
        *) JAVA_HOME_CANDIDATES=(${JAVA7_HOME_CANDIDATES[@]}
                                 ${JAVA8_HOME_CANDIDATES[@]}
                                 ${MISCJAVA_HOME_CANDIDATES[@]}
                                 ${OPENJAVA7_HOME_CANDIDATES[@]}
                                 ${OPENJAVA8_HOME_CANDIDATES[@]})
        ;;
    esac

    # attempt to find java
    if [ -z "${JAVA_HOME}" ]; then
        for candidate_regex in ${JAVA_HOME_CANDIDATES[@]}; do
            for candidate in `ls -rvd ${candidate_regex}* 2>/dev/null`; do
                if [ -e ${candidate}/bin/java ]; then
                    export JAVA_HOME=${candidate}
                    break 2
                fi
            done
        done
    fi
 
 
 
 
What is using this script?
--------------------------
 
 .. code-block:: text
 
     $ grep /usr/lib/bigtop-utils/bigtop-detect-javahome /etc/init.d/*
    /etc/init.d/hadoop-0.20-mapreduce-jobtracker:if [ -f /usr/lib/bigtop-utils/bigtop-detect-javahome ]; then
    /etc/init.d/hadoop-0.20-mapreduce-jobtracker:  . /usr/lib/bigtop-utils/bigtop-detect-javahome
    /etc/init.d/hadoop-0.20-mapreduce-tasktracker:if [ -f /usr/lib/bigtop-utils/bigtop-detect-javahome ]; then
    /etc/init.d/hadoop-0.20-mapreduce-tasktracker:  . /usr/lib/bigtop-utils/bigtop-detect-javahome
    /etc/init.d/hadoop-hdfs-namenode:if [ -f /usr/lib/bigtop-utils/bigtop-detect-javahome ]; then
    /etc/init.d/hadoop-hdfs-namenode:  . /usr/lib/bigtop-utils/bigtop-detect-javahome
    /etc/init.d/hadoop-hdfs-secondarynamenode:if [ -f /usr/lib/bigtop-utils/bigtop-detect-javahome ]; then
    /etc/init.d/hadoop-hdfs-secondarynamenode:  . /usr/lib/bigtop-utils/bigtop-detect-javahome
    /etc/init.d/hadoop-mapreduce-historyserver:if [ -f /usr/lib/bigtop-utils/bigtop-detect-javahome ]; then
    /etc/init.d/hadoop-mapreduce-historyserver:  . /usr/lib/bigtop-utils/bigtop-detect-javahome
    /etc/init.d/hadoop-yarn-resourcemanager:if [ -f /usr/lib/bigtop-utils/bigtop-detect-javahome ]; then
    /etc/init.d/hadoop-yarn-resourcemanager:  . /usr/lib/bigtop-utils/bigtop-detect-javahome
    /etc/init.d/hbase-master:if [ -f /usr/lib/bigtop-utils/bigtop-detect-javahome ]; then
    /etc/init.d/hbase-master:  . /usr/lib/bigtop-utils/bigtop-detect-javahome
    /etc/init.d/hbase-regionserver:. /usr/lib/bigtop-utils/bigtop-detect-javahome
    /etc/init.d/hbase-rest:if [ -f /usr/lib/bigtop-utils/bigtop-detect-javahome ]; then
    /etc/init.d/hbase-rest:  . /usr/lib/bigtop-utils/bigtop-detect-javahome
    /etc/init.d/hbase-thrift:if [ -f /usr/lib/bigtop-utils/bigtop-detect-javahome ]; then
    /etc/init.d/hbase-thrift:  . /usr/lib/bigtop-utils/bigtop-detect-javahome
    /etc/init.d/hive-server2:if [ -f /usr/lib/bigtop-utils/bigtop-detect-javahome ]; then
    /etc/init.d/hive-server2:  . /usr/lib/bigtop-utils/bigtop-detect-javahome
    /etc/init.d/impala-catalog:if [ -f /usr/lib/bigtop-utils/bigtop-detect-javahome ]; then
    /etc/init.d/impala-catalog:  . /usr/lib/bigtop-utils/bigtop-detect-javahome
    /etc/init.d/impala-server:if [ -f /usr/lib/bigtop-utils/bigtop-detect-javahome ]; then
    /etc/init.d/impala-server:  . /usr/lib/bigtop-utils/bigtop-detect-javahome
    /etc/init.d/impala-state-store:if [ -f /usr/lib/bigtop-utils/bigtop-detect-javahome ]; then
    /etc/init.d/impala-state-store:  . /usr/lib/bigtop-utils/bigtop-detect-javahome
    /etc/init.d/spark-worker:if [ -f /usr/lib/bigtop-utils/bigtop-detect-javahome ]; then
    /etc/init.d/spark-worker:  . /usr/lib/bigtop-utils/bigtop-detect-javahome
    /etc/init.d/zookeeper-server:. /usr/lib/bigtop-utils/bigtop-detect-javahome
