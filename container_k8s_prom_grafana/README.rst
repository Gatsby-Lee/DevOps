K8s / Prometheus / Grafana
##########################

References
==========

cAdvisor
--------

* https://github.com/google/cadvisor/blob/master/docs/storage/prometheus.md
* https://docs.signalfx.com/en/latest/integrations/agent/monitors/cadvisor.html

Prometheus
----------

* https://prometheus.io/docs/prometheus/latest/querying/basics/

PromQL + cAdvisor
-----------------

* https://www.replex.io/blog/kubernetes-in-production-the-ultimate-guide-to-monitoring-resource-metrics


Prometheus Metric Types
=======================

ref: https://prometheus.io/docs/concepts/metric_types/

* Counter ( only increase or be reset to zero on restart ) - Cumulative
* Gauge ( go up and down )
* Histogram ( bucket / count )
* Summary ( quantiles )

References for Prometheus functions - rate / irate / increase
=============================================================

* https://stackoverflow.com/questions/54494394/do-i-understand-prometheuss-rate-vs-increase-functions-correctly
* https://github.com/prometheus/prometheus/issues/3746
* https://www.metricfire.com/blog/understanding-the-prometheus-rate-function/

References Prometheus Recording rules
=====================================

* https://deploy.live/blog/today-i-learned-prometheus-recording-rules/

Note: Duplicated cAdvisor output
=======================

ref: https://github.com/google/cadvisor/issues/2249

* `container="":` for pod cgroup ( exposed by cAdvisor )
* `container="POD"` for "pause" container for the pod. ( exposed by cAdvisor )
* `container="${pod_name}"` for a specific container in Pod


Metrics from cAdvisor
======================

cAdvisor is an open-source agent integrated into the kubelet binary that monitors resource usage and analyzes the performance of containers.

CPU
---

* container_cpu_user_seconds_total: Cumulative “user” CPU time consumed in seconds
* container_cpu_system_seconds_total: Cumulative “system” CPU time consumed in seconds
* container_cpu_usage_seconds_total: Cumulative CPU time consumed in seconds (sum of the above)
* container_cpu_cfs_throttled_seconds_total

Memory
-------

* container_memory_cache: Number of bytes of page cache memory
* container_memory_swap: Container swap usage in bytes
* container_memory_usage_bytes: Current memory usage in bytes, including all memory regardless of when it was accessed
* container_memory_max_usage_bytes: Maximum memory usage in byte

Disk
----

* container_fs_io_time_seconds_total: Count of seconds spent doing I/Os
* container_fs_io_time_weighted_seconds_total: Cumulative weighted I/O time in seconds
* container_fs_writes_bytes_total: Cumulative count of bytes written
* container_fs_reads_bytes_total: Cumulative count of bytes read

Network
-------

* container_network_receive_bytes_total: Cumulative count of bytes received
* container_network_receive_errors_total: Cumulative count of errors encountered while receiving
* container_network_transmit_bytes_total: Cumulative count of bytes transmitted
* container_network_transmit_errors_total: Cumulative count of errors encountered while transmitting


---------

Container metric Calculation - General
======================================

Pod Age
-------

* ``container_start_time_seconds ( Gauge ):``

  * container="${pod_name}" is necessary.
  * the value doesn't change although Pod is restarted.
  * max .. by(pod): to aggregate - it doesn't really matter to use ``max`` or ``sum`` since only one row will be returned.

``max(time()-container_start_time_seconds{pod=~"$pod_name-.*",container="$pod_name"})by(pod)``

Pod restart counts
------------------

* ``kube_pod_container_status_restarts_total ( Counter, cumulative )``

  * by default, return the last(latest) value
  * max .. by(pod): to aggregate - it doesn't matter to use ``max`` or ``sum``, but prefer ``max``

``max(kube_pod_container_status_restarts_total{pod=~"$pod_name-.*",container="$pod_name"})by(pod)``

Number of Running Pods
----------------------

``count(kube_pod_info{pod=~"$pod_name-.*"})``


Container metric Calculation - CPU
==================================

CPU current Usage
-----------------

* ``container_cpu_usage_seconds_total ( Counter, cumulative )``

  * container="${pod_name}" is necessary.
  * `irate`: diff between the recent two data points ( [5m] )
  * max .. by(pod): to aggregate - it doesn't matter to use ``max`` or ``sum``
  * time range the recent 5m
  * x1000 to covert to mCPU

``max(irate(container_cpu_usage_seconds_total{pod=~"$pod_name-.*",container="$pod_name"}[5m]))by(pod) * 1000``


CPU throttled second
--------------------

* ``container_cpu_cfs_throttled_seconds_total ( Counter, cumulative )``

  * container="${pod_name}" is necessary.
  * `irate`: diff between the recent two data points ( [5m] )
  * max .. by(pod): to aggregate - it doesn't matter to use ``max`` or ``sum``
  * time range the recent 5m
  * x1000 to covert to mCPU

``sum(irate(container_cpu_cfs_throttled_seconds_total{pod=~"$pod_name-.*",container="$pod_name"}[5m]))by(pod) * 1000``


CPU Usage Percentage based on Request
-------------------------------------

* ``container_cpu_usage_seconds_total ( Counter )``

    * container="$pod_name" is necessary.
    * `irate`: diff between the recent two data points ( [5m] )
    * max .. by(pod): to aggregate - it doesn't matter to use ``max`` or ``sum``

* ``kube_pod_container_resource_requests_cpu_cores``

    * container="$pod_name" is NOT necessary.
    * max .. by(pod): to aggregate - it doesn't matter to use ``max`` or ``sum``

``max(irate(container_cpu_usage_seconds_total{pod=~"$pod_name-.*",container="$pod_name"}[5m]))by(pod) / max(kube_pod_container_resource_requests_cpu_cores{pod=~"$pod_name-.*"})by(pod) * 100``


CPU Usage Percentage based on Limit
-------------------------------------

* ``container_cpu_usage_seconds_total ( Counter )``

    * container="$pod_name" is necessary.
    * `irate`: diff between the recent two data points ( [5m] )
    * max .. by(pod): to aggregate - it doesn't matter to use ``max`` or ``sum``

* ``kube_pod_container_resource_limits_cpu_cores``

    * container="$pod_name" is NOT necessary.
    * max .. by(pod): to aggregate - it doesn't matter to use ``max`` or ``sum``

``max(irate(container_cpu_usage_seconds_total{pod=~"$pod_name-.*",container="$pod_name"}[5m]))by(pod) / max(kube_pod_container_resource_limits_cpu_cores{pod=~"$pod_name-.*"})by(pod) * 100``


References about CPU
--------------------

* https://github.com/google/cadvisor/issues/2026



Container metric Calculation - Memory
=====================================

* `container_memory_usage_bytes vs. container_memory_working_set_bytes <https://blog.freshtracks.io/a-deep-dive-into-kubernetes-metrics-part-3-container-resource-metrics-361c5ee46e66>`_
* ``container_memory_usage_bytes``: Current memory usage in bytes, including all memory regardless of when it was accessed.
* ``container_memory_working_set_bytes``: Current working set in bytes. ( OOM killer is watching this )


Memory Current Usage
---------------------

* ``container_memory_working_set_bytes ( Gauge )``

  * container="${pod_name}" is necessary.
  * max .. by(pod): to aggregate - it doesn't really matter to use ``max`` or ``sum`` since only one row will be returned.

``max(container_memory_working_set_bytes{pod=~"$pod_name-.*",container="$pod_name"})by(pod)``


Memory Usage Percentage based on Limit
-----------------------------------
  
* ``container_memory_working_set_bytes ( Gauge )``

  * container="${pod_name}" is necessary.
  * max .. by(pod): to aggregate - it doesn't really matter to use ``max`` or ``sum`` since only one row will be returned.

* ``container_spec_memory_limit_bytes ( Gauge )``

  * container="${pod_name}" is necessary.
  * Since it is from config, the value is not changed unless updated manually.
  * max .. by(pod): to aggregate - it doesn't really matter to use ``max`` or ``sum`` since only one row will be returned.
  
``max(container_memory_working_set_bytes{pod=~"$pod_name-.*",container="$pod_name"})by(pod) / max(container_spec_memory_limit_bytes{pod=~"$pod_name-.*",container="$pod_name"})by(pod) * 100``


Container metric Calculation - Network
======================================

Network Outbound Useage
-----------------------

* ``container_network_transmit_bytes_total ( Counter, Cumulative, bytes )``

  * do not put container="${pod_name}"
  * ``irate`` if Table with Instant
  * ``rate`` if Graph
  * max .. by(pod): to aggregate - it doesn't really matter to use ``max`` or ``sum`` since only one row will be returned.

``max(irate(container_network_transmit_bytes_total{pod=~"$pod_name-.*"}[5m]))by(pod)``

Network Inboud Useage
---------------------

* ``container_network_receive_bytes_total ( Counter, Cumulative, bytes )``

  * do not put container="$pod_name"
  * ``irate`` if Table with Instant
  * ``rate`` if Graph
  * max .. by(pod): to aggregate - it doesn't really matter to use ``max`` or ``sum`` since only one row will be returned.

``max(irate(container_network_receive_bytes_total{pod=~"$pod_name-.*"}[5m]))by(pod)``

