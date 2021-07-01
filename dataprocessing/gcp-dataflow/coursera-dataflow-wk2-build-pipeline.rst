Serverless Data Processing with Dataflow: Develop Pipelines
===========================================================

Summary of the learning


Beam Concepts Review
====================

Beam Basics
-----------

Providing a structure that unifies "Batch" and "Streaming" processing concepts.


Fore main concepts
>>>>>>>>>>>>>>>>>>

* PTransforms: holding "input", "transformation(actions)", "output"
* PCollections:
  * "the data held on a distributed data structure"
  * Immutable
* Pipelines: Identifies "the date to be processed" and "the action to be taken on the data"
* Pipeline Runners

.. image:: ./images/gcp_k8s_workload/gcp-dataflow-wk2-1.png


Utility Transforms
------------------

* ParDo
* ParalleDo
* GroupByKey: we can put all the elements with the same key together in the same worker.
* Combine: if group is very large or data is very skewed. This is betther than "GroupByKey"
* CoGroupByKey: Left/Right Outer Join, Inner Join ( different value type )
* Flatten: merge more than two PCollections ( for exactly the same type )
* Partition: opposite of "Flatten". This divides PCollection to several PCollections by applying a function that assigns a group ID to each element in the input PCollection.

DoFn Lifecycle
--------------

* ParDo: kind of simple "map" or "filter"

.. image:: ./images/gcp_k8s_workload/gcp-dataflow-wk2-2.png
.. image:: ./images/gcp_k8s_workload/gcp-dataflow-wk2-3.png
.. image:: ./images/gcp_k8s_workload/gcp-dataflow-wk2-4.png


* references
  * https://beam.apache.org/documentation/basics/
  * https://beam.apache.org/documentation/programming-guide/
  * https://beam.apache.org/documentation/resources/learning-resources/
  * https://beam.apache.org/documentation/patterns/overview/


.. code-block:: python

    # we can override function to control how to interact with each data bundle.
    # Runner may recycle Do Function or process the same bundle in different workers for redundancy.
    # so, do not mutate external state from your process method.
    # Ensure any state variable is clear in the start bundle method
    # otherwise, the state variable might have one from prev. bundle.
    # FYI, bundle may contain several keys, so store state in maps based on that key.
    class MyDoFn(beam.DoFn):
        def setup(self):
            # google palce to setup db connection / helper process
            pass
        def start_bundle(self):
            pass
        def process(self, element):
            # this is main function
            # this is where tranform happens.
            pass
        def finish_bundle(self):
            pass
        def teardown(self):
            pass


Windows, Watermarks, Triggers
=============================
