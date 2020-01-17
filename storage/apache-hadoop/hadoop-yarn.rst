Hadoop YARN
###########

decommission/recommission node
==============================

* ref: https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/GracefulDecommission.html

Summary
-------

* add `yarn.resourcemanager.nodes.exclude-path` property into `yarn-site.xml`
* add hostname to decommision into `yarn.exclude`
* yarn rmadmin -refreshNodes -g -client

    * NodesListManager refresh its list
    * ResourceManager will send kill SIGNAL to hadoop-yarn-nodemanager
    * hadoop-yarn-nodemanager will die.

* To recommission, remove hostname from `yarn.exclude`
* yarn rmadmin -refreshNodes -g -client

  * NodesListManager refresh its list.

* Start hadoop-yarn-nodemanager


update yarn-site.xml
--------------------

* add below configuration into `yarn-site.xml`

.. code-block:: xml

  <property>
    <name>yarn.resourcemanager.nodes.exclude-path</name>
    <value>/etc/hadoop/conf/yarn.exclude</value>
    <description>Path to file with nodes to exclude.</description>
  </property>


decommissioning yarn node
-------------------------

* NOTE: decommissioned node will kill hadoop-yarn-nodemanager

1. add hostname to decommission
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

* `/etc/hadoop/conf/yarn.exclude`

.. code-block:: text

    hadoop1-wn1.test.com


2. execute yarn command to refresh NodesListManager
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

* -g : graceful ( without this, it's not graceful )
* -client: command waits until timeout or nodes are decommisioned.
* -server: command is sent ResourceManager and RM will tracking decommissioning.

.. code-block:: bash

    # this cmd notify NodesListManager to update its exclude/include host list
    $ yarn rmadmin -refreshNodes -g -client
    20/01/16 21:45:02 INFO client.RMProxy: Connecting to ResourceManager at hadoop1-nn.test.com/10.168.16.62:8033
    Nodes 'hadoop-wn1.peak.test.com:38109' are still decommissioning.
    Nodes 'hadoop-wn1.peak.test.com:38109' are still decommissioning.
    ...
    ...
    Nodes 'hadoop1-wn1.test.com:38109' are still decommissioning.
    Nodes 'hadoop1-wn1.test.com:38109' are still decommissioning.
    Graceful decommissioning completed in 50 seconds.


recommissioning decommissioned yarn node
----------------------------------------

* NOTE: on decommissioned node `hadoop-yarn-nodemanager` will die again if restarted without notifying NodesListManager to update its exclude/include host list

1. remove (or comment) hostname from `/etc/hadoop/conf/yarn.exclude`
2. execute yarn command to refresh NodesListManager

.. code-block:: bash

    yarn rmadmin -refreshNodes -g -client
