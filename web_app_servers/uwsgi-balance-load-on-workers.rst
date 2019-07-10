Balance Load on Workers
=======================

If few workers do most of jobs, add `thunder-lock=true` into uwsgi.ini or append --thunder-lock option.

Why load is not balanced
------------------------

* https://blog.cloudflare.com/the-sad-state-of-linux-socket-balancing/


References
----------

* https://cra.mr/2013/06/27/serving-python-web-applications
* https://github.com/unbit/uwsgi/issues/1063
* https://uwsgi-docs.readthedocs.io/en/latest/articles/SerializingAccept.html
