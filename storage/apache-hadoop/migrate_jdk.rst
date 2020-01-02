Migrate JDK
###########

Context
=======

* using CentOS 6.7
* using Oracle JDK 1.7
* migrating OpenJDK 1.8 ( java-1.8.0-openjdk-1.8.0.181-3.b13.el6_10.x86_64.rpm )
* using CDH 5.16.2 ( supporting OpenJDK 1.8.181 )


How to update to use JDK8?
==========================

* JDK version is picked by /usr/lib/bigtop-utils/bigtop-detect-javahome
* bigtop selects the lowest version if JDK 7 and 8 are installed.
* In order to use JDK8, either uninstall JDK 7 or set BIGTOP_JAVA_MAJOR=8 in /usr/lib/bigtop-utils/bigtop-detect-javahome
* I prefer to remove JDK7


Install OpenJDK8
================

* CentOS6.10 has java-1.8.0-openjdk-1.8.0.181-3.b13.el6_10.x86_64.rpm

  * http://mirror.centos.org/centos-6/6.10/updates/x86_64/Packages/java-1.8.0-openjdk-1.8.0.181-3.b13.el6_10.x86_64.rpm


* Check installed jdk

.. code-block:: bash

    yum list installed | grep jdk


* Uninstall different version of OpenJDK1.8 ( never uninstall packages without checking the dependency list )

.. code-block:: bash

    yum erase -y java-1.8.0-openjdk-headless


* Install OpenJDK 1.8
* Create symbolic link

.. code-block:: bash

    ln -sfn /usr/lib/jvm/jre-1.8.0-openjdk.x86_64 /usr/java/latest

* Check java version

.. code-block:: bash

    java -version
    /usr/java/default/bin/java -version

* Uninstall JDK7

.. code-block:: bash

    yum erase jdk.x86_64


Checking current config/java in Hadoop
======================================

.. code-block:: bash

    $ alternatives --display java | grep "link currently points to"
    link currently points to /usr/java/default/bin/java

    $ /usr/sbin/alternatives --config java
    There are 3 programs which provide 'java'.
    Selection    Command
    -----------------------------------------------
    1           /usr/lib/jvm/jre-1.8.0-openjdk.x86_64/bin/java
    2           /usr/lib/jvm/jre-1.5.0-gcj/bin/java
    *+ 3        /usr/java/default/bin/java

    $ /etc/alternatives/java -version
    java version "1.7.0_67"
    Java(TM) SE Runtime Environment (build 1.7.0_67-b01)
    Java HotSpot(TM) 64-Bit Server VM (build 24.65-b04, mixed mode)

    $ /usr/java/default/bin/java -version
    java version "1.7.0_67"
    Java(TM) SE Runtime Environment (build 1.7.0_67-b01)
    Java HotSpot(TM) 64-Bit Server VM (build 24.65-b04, mixed mode)

    $ /usr/lib/jvm/jre-1.8.0-openjdk.x86_64/bin/java -version
    openjdk version "1.8.0_71"
    OpenJDK Runtime Environment (build 1.8.0_71-b15)
    OpenJDK 64-Bit Server VM (build 25.71-b15, mixed mode)

    $ ls -al /usr/java/
    total 12
    drwxr-xr-x   3 root root 4096 Jul 25  2014 .
    drwxr-xr-x. 15 root root 4096 Jul 25  2014 ..
    lrwxrwxrwx   1 root root   16 Feb 10  2016 default -> /usr/java/latest
    drwxr-xr-x   8 root root 4096 Feb 10  2016 jdk1.7.0_67
    lrwxrwxrwx   1 root root   21 Feb 10  2016 latest -> /usr/java/jdk1.7.0_67

    $ ls -al /usr/bin/ | grep java
    lrwxrwxrwx    1 root root          42 Oct 30 17:52 bigtop-detect-javahome -> ../lib/bigtop-utils/bigtop-detect-javahome
    -rwxr-xr-x    1 root root       10464 Jul 22  2015 gjavah
    lrwxrwxrwx    1 root root          22 Feb 11  2016 java -> /etc/alternatives/java
    lrwxrwxrwx    1 root root          23 Jun 29  2016 javac -> /etc/alternatives/javac
    lrwxrwxrwx    1 root root          25 Jun 29  2016 javadoc -> /etc/alternatives/javadoc
    lrwxrwxrwx    1 root root          23 Jun 29  2016 javah -> /etc/alternatives/javah
    lrwxrwxrwx    1 root root          28 Feb 10  2016 javaws -> /usr/java/default/bin/javaws
    lrwxrwxrwx    1 root root          30 Feb 10  2016 jcontrol -> /usr/java/default/bin/jcontrol

    $ ls -al /usr/lib/jvm/
    total 16
    drwxr-xr-x   4 root root 4096 Jun 29  2016 .
    drwxr-xr-x. 51 root root 4096 Sep 27  2018 ..
    lrwxrwxrwx   1 root root   26 Jun 29  2016 java -> /etc/alternatives/java_sdk
    lrwxrwxrwx   1 root root   32 Jun 29  2016 java-1.5.0 -> /etc/alternatives/java_sdk_1.5.0
    lrwxrwxrwx   1 root root   22 Jun 29  2016 java-1.5.0-gcj -> java-1.5.0-gcj-1.5.0.0
    drwxr-xr-x   6 root root 4096 Jun 29  2016 java-1.5.0-gcj-1.5.0.0
    drwxr-xr-x   3 root root 4096 Feb 10  2016 java-1.8.0-openjdk-1.8.0.71-1.b15.el6_7.x86_64
    lrwxrwxrwx   1 root root   30 Jun 29  2016 java-gcj -> /etc/alternatives/java_sdk_gcj
    lrwxrwxrwx   1 root root   27 Feb 10  2016 jre-1.5.0 -> /etc/alternatives/jre_1.5.0
    lrwxrwxrwx   1 root root   26 Feb 10  2016 jre-1.5.0-gcj -> java-1.5.0-gcj-1.5.0.0/jre
    lrwxrwxrwx   1 root root   27 Feb 10  2016 jre-1.8.0 -> /etc/alternatives/jre_1.8.0
    lrwxrwxrwx   1 root root   50 Feb 10  2016 jre-1.8.0-openjdk-1.8.0.71-1.b15.el6_7.x86_64 -> java-1.8.0-openjdk-1.8.0.71-1.b15.el6_7.x86_64/jre
    lrwxrwxrwx   1 root root   50 Feb 10  2016 jre-1.8.0-openjdk.x86_64 -> java-1.8.0-openjdk-1.8.0.71-1.b15.el6_7.x86_64/jre
    lrwxrwxrwx   1 root root   25 Feb 10  2016 jre-gcj -> /etc/alternatives/jre_gcj
    lrwxrwxrwx   1 root root   29 Feb 10  2016 jre-openjdk -> /etc/alternatives/jre_openjdk
