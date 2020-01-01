Network Time Protocol ( NTP )
#############################

NTP Configuration Best Practices
================================

ref: https://kudu.apache.org/docs/troubleshooting.html#_ntp_configuration_best_practices

* Always configure at least four time sources for NTP
* Pick servers in your server’s local geography
* Use the iburst option for faster synchronization at startup


Setup ntp
=========

* ref:

  * https://www.tldp.org/LDP/sag/html/basic-ntp-config.html
  * https://www.ntppool.org/en/use.html



How to check health
===================

`ntpstat` exit code
-------------------

* exit 0: Clock is synchronised
* exit 1: Clock is NOT synchronised
* exit 2: If clock state is indeterminant, for example if ntpd is not contactable.

.. code-block:: bash

    $ ntpstat;echo $?
    unsynchronised
    polling server every 8 s
    1


`ntptime`
---------

Unhealthy status
>>>>>>>>>>>>>>>>

Note the UNSYNC status and the 16-second maximum error.

.. code-block:: bash

    $ ntptime
    ntp_gettime() returns code 5 (ERROR)
      time e1b77c3a.4947f114  Wed, Jan  1 2020 12:14:50.286, (.286254310),
      maximum error 16000000 us, estimated error 16 us, TAI offset 0
    ntp_adjtime() returns code 5 (ERROR)
      modes 0x0 (),
      offset 0.000 us, frequency 24.391 ppm, interval 1 s,
      maximum error 16000000 us, estimated error 16 us,
      status 0x6041 (PLL,UNSYNC,NANO,MODE),
      time constant 3, precision 0.001 us, tolerance 500 ppm,


Healthy status
>>>>>>>>>>>>>>

.. code-block:: bash

    $ ntptime
    ntp_gettime() returns code 0 (OK)
      time e1b78c2f.d5c6b004  Wed, Jan  1 2020 13:22:55.835, (.835063888),
      maximum error 308938 us, estimated error 1297 us, TAI offset 0
    ntp_adjtime() returns code 0 (OK)
      modes 0x0 (),
      offset -682.553 us, frequency 24.154 ppm, interval 1 s,
      maximum error 308938 us, estimated error 1297 us,
      status 0x2001 (PLL,NANO),
      time constant 6, precision 0.001 us, tolerance 500 ppm,


How to get  time servers and details
====================================

ntpq
----

* ref:

  * https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/s1-checking_the_status_of_ntp
  * http://doc.ntp.org/4.1.0/ntpq.htm

.. code-block:: bash

    $ ntpq -p
     remote           refid      st t when poll reach   delay   offset  jitter
    ==============================================================================
    -voipmonitor.wci 66.220.9.122     2 u   52   64  377   22.865    0.351   0.277
    +y.ns.gin.ntt.ne 249.224.99.213   2 u   18   64  367    1.858   -0.378   0.397
    +sombrero.spider 142.66.101.13    2 u   50   64  377   70.647   -0.456   0.301
    *clock.nyc.he.ne .CDMA.           1 u   49   64  377   70.590    0.961   0.256

    $ ntpq -nc opeers
        remote           local      st t when poll reach   delay   offset    disp
    ==============================================================================
    -204.11.201.10   172.17.20.3      2 u   45   64  377   22.865    0.351   1.260
    +129.250.35.251  172.17.20.3      2 u    9   64  173    1.858   -0.378  66.834
    +185.213.26.143  172.17.20.3      2 u   43   64  377   70.647   -0.456   3.360
    *209.51.161.238  172.17.20.3      1 u   45   64  377   70.590    0.961   2.820

    $ ntpq -nc lpeers
        remote           refid      st t when poll reach   delay   offset  jitter
    ==============================================================================
    -204.11.201.10   66.220.9.122     2 u   29   64  377   22.865    0.351   0.277
    +129.250.35.251  249.224.99.213   2 u   59   64  173    1.858   -0.378   0.404
    +185.213.26.143  142.66.101.13    2 u   27   64  377   70.647   -0.456   0.301
    *209.51.161.238  .CDMA.           1 u   26   64  377   70.590    0.961   0.256


* **remote and refid:** remote NTP server, and its NTP server
* **st:** stratum of server
* **t:** type of server (local, unicast, multicast, or broadcast)
* **poll:** how frequently to query server (in seconds)
* **when:** how long since last poll (in seconds)
* **reach:** octal bitmask of success or failure of last 8 queries (left-shifted); 377 = 11111111 = all recent queries were successful; 257 = 10101111 = 4 most recent were successful, 5 and 7 failed
* **delay:** network round trip time (in milliseconds)
* **offset:** difference between local clock and remote clock (in milliseconds)
* **jitter:** difference of successive time values from server (high jitter could be due to an unstable clock or, more likely, poor network performance)


ntpdc
-----

.. code-block:: bash

    $ ntpdc -c sysinfo
    system peer:          0.0.0.0
    system peer mode:     unspec
    leap indicator:       11
    stratum:              16
    precision:            -24
    root distance:        0.00000 s
    root dispersion:      1.09222 s
    reference ID:         [73.78.73.84]
    reference time:       00000000.00000000  Sun, Dec 31 1899 16:00:00.000
    system flags:         auth monitor ntp kernel stats
    jitter:               0.000000 s
    stability:            0.000 ppm
    broadcastdelay:       0.000000 s
    authdelay:            0.000000 s
