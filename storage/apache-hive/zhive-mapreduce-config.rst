Hive MapReduce Config
=====================

* Fraction of the number of maps in the job which should be complete before reduces are scheduled for the job.

.. code-block::
  
  SET mapreduce.job.reduce.slowstart.completedmaps=0.95;


External Resources
------------------
* https://cwiki.apache.org/confluence/display/Hive/Configuration+Properties
