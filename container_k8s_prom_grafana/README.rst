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


Container metric Calculation
============================

Pod Age
-------
* ``container_start_time_seconds ( Gauge ):`` the value doesn't change although Pod is restarted.
* multiple rows will be returned with different values for container like container="POD", container="", container="${pod_name}"
* I pick container="POD" since I care about Pod Age

``max(time()-container_start_time_seconds{pod=~"$pod_name-.*", container="POD"})by(pod)``


CPU Usage Percentage based on Limit
-----------------------------------

* ``container_cpu_usage_seconds_total ( Counter )``

    * container="${pod_name}" is necessary.
    * `irate`: diff between the recent two data points ( [5m] )
    * max .. by(pod): to aggregate - it doesn't matter to use ``max`` or ``sum``

* ``kube_pod_container_resource_requests_cpu_cores``

    * container="${pod_name}" is NOT necessary.
    * max .. by(pod): to aggregate - it doesn't matter to use ``max`` or ``sum``

``max(irate(container_cpu_usage_seconds_total{pod=~"${pod_name}-.*",container="${pod_name}"}[5m]))by(pod) / max(kube_pod_container_resource_requests_cpu_cores{pod=~"${pod_name}-.*"})by(pod) * 100``

