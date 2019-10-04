How to check impala is ready to take request
============================================

HAProxy + xinetd: http://sysbible.org/2008/12/04/having-haproxy-check-mysql-status-through-a-xinetd-script/


.. code-block:: python

    import argparse
    import urllib2
    import json

    HOST = '127.0.0.1'
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


    def parse_args():

        parser = argparse.ArgumentParser()
        parser.add_argument('--host', default=HOST)

        return parser.parse_args()


    def main():

        args = parse_args()

        timeout = 10
        impala_server_status = False
        try:
            url = 'http://%s:25000/metrics?json' % (args.host)
            handle = urllib2.urlopen(url, timeout=timeout)
            content = json.loads(handle.read())
            _, v = recursive_check(content['metric_group'])
            impala_server_status = v
        except Exception:
            pass
        print impala_server_status


    if __name__ == '__main__':
        main()
