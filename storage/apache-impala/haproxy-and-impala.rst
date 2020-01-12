HAProxy and Impala
##################

Summary
=======

* Impala Dedicated Coordinator
* High Availablity and Load Balancing ( HAProxy )
* xinetd


Setup HAProxy
=============

Setup HAProxy to use `httpchk` to check health of server with port 9200

.. code-block:: conf

    listen impala_coordinators
        bind *:30000
        balance first
        option httpchk
        default-server port 9200 inter 60s downinter 5s rise 4 fall 2
        server impala_c1  impala-c1.test.com:21050 check inter 60s maxconn 90
        server impala_c2  impala-c2.test.com:21050 check inter 60s maxconn 90


Setup xinetd
============

create /usr/local/bin/impalacheck
---------------------------------

* change permission to 755

.. code-block:: python

    #!/usr/bin/env python
    import json
    import sys

    try:
        # For Python 3.0 and later
        from urllib.request import urlopen
        from urllib.error import URLError
    except ImportError:
        # Fall back to Python 2's urllib2
        from urllib2 import urlopen

    HOST = '127.0.0.1'
    PORT = 25000
    KEY_LOOKFOR = 'catalog.ready'

    # Strucutre of JSON
    # metric_group
    #   - name: str
    #   - metrics: list of metric(name:.., value:..)
    #   - child_groups: list of metric_group


    def recursive_check(metric_group):

        for m in metric_group['metrics']:
            if m['name'] == KEY_LOOKFOR:
                return (True, m['value'])

        for next_metric_group in metric_group['child_groups']:
            found, v = recursive_check(next_metric_group)
            if found:
                return (found, v)

        return (False, False)


    def generate_http_response(impala_server_status):

        if impala_server_status:
            return """\
    HTTP/1.1 200 OK

    Impala server is running
    """
        else:
            return """\
    HTTP/1.1 503 Service Unavailable

    Impala server is down
    """


    def parse_args():
        """
        Parsing arguments host and port
        @note: in order to handle multiple version of python,
            common library in python built-in module.
        """
        host = HOST
        try:
            host = sys.argv[1]
        except Exception:
            pass

        port = PORT
        try:
            port = sys.argv[2]
        except Exception:
            pass

        return (host, port)


    def main():

        host, port = parse_args()

        timeout = 10
        impala_server_status = False
        try:
            url = 'http://%s:%s/metrics?json' % (host, port)
            handle = urlopen(url, timeout=timeout)
            res = handle.read()
            content = json.loads(res)
            _, v = recursive_check(content['metric_group'])
            impala_server_status = v
        except Exception as e:
            pass
        res = generate_http_response(impala_server_status)
        print(res)


    if __name__ == '__main__':
        main()


create /etc/xinetd.d/impala-chk
------------------------

.. code-block:: bash

    service impala-chk
    {
        disable = no
        flags = REUSE
        socket_type = stream
        port = 9200
        wait = no
        user = root
        server = /usr/local/bin/impalacheck
        log_on_failure += USERID
        per_source = UNLIMITED
        # suppress logging to /varlog/message
        log_on_success =
    }

append to `/etc/services`
-------------------------

.. code-block:: cfg

    impala-chk       9200/tcp               # Impala check


References
==========
* HAProxy + xinetd: http://sysbible.org/2008/12/04/having-haproxy-check-mysql-status-through-a-xinetd-script/

