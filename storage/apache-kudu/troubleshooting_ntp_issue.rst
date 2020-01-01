Troubleshooting NTP issue
#########################

Symtoms
=======

* kudu master stopped running
* kudu tserver stopped running

Log content
-----------

.. code-block:: text

    W1231 22:02:29.411993 20205 system_ntp.cc:82] could not find executable: chronyc
    W1231 22:02:29.434617 20205 system_ntp.cc:82] could not find executable: chronyc
    F1231 22:02:29.434728 20205 hybrid_clock.cc:340] Check failed: _s.ok() unable to get current time with error bound: Service unavailable: clock error estimate (10000016us) too high (clock considered synchronized by the kernel)


Resolution
==========

* ref: https://kudu.apache.org/docs/troubleshooting.html#ntp
* Update ntp config to use more than one source
* restart service
