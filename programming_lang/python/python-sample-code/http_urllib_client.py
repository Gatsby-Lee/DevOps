"""
Python3
"""

import json
import logging
import urllib3

from base64 import b64encode
from urllib3.util import make_headers

LOGGER = logging.getLogger(__name__)

class RequestTimedOutException(Exception):
    pass


class HTTPUrllibClient:

    __slots__ = ("username", "password", "urllib_pool")

    def __init__(
        self,
        http_endpoint,
        username,
        password,
        proxy_obj=None,
        request_timeout=60,
        https=False,
    ):
        """
        @param str username
        @param str api_password
        """
        self.username = username
        self.password = password
        # Reconnect 3x if connection is closed? Disable all other retries
        # (We already have our own retry logic wrapped around API requests in vendor client classes)
        retries = urllib3.Retry(total=0, connect=3)
        # maxsize=1 to limit the connectionpool size to only 1 connection (each thread will create their own instance)
        if proxy_obj is None:
            connection_pool_class = urllib3.HTTPConnectionPool
            if https:
                connection_pool_class = urllib3.HTTPSConnectionPool
            self.urllib_pool = connection_pool_class(
                http_endpoint, maxsize=1, retries=retries, timeout=request_timeout
            )
        else:
            proxy_url = f"{proxy_obj.host}:{proxy_obj.port}"
            proxy_headers = {}
            if proxy_obj.auth_user and proxy_obj.auth_pass:
                user_pass = f"{proxy_obj.auth_user}:{proxy_obj.auth_pass}"
                base64_bytes = b64encode(user_pass.encode("ascii")).decode("ascii")
                proxy_headers["Proxy-Authorization"] = "Basic %s" % base64_bytes
            self.urllib_pool = urllib3.ProxyManager(
                proxy_url,
                maxsize=1,
                retries=retries,
                proxy_headers=proxy_headers,
                cert_reqs=proxy_obj.cert_reqs,
                timeout=request_timeout,
            )

    def request(self, path, method, headers=None, data=None):
        response_str_decoded = status_code = None
        default_headers = {"Content-Type": "application/json"}
        if self.username is not None and self.password is not None:
            username_password = f"{self.username}:{self.password}"
            auth_headers = make_headers(basic_auth=username_password)
            default_headers.update(auth_headers)
        if headers is not None:
            default_headers.update(headers)
        try:
            response = self.urllib_pool.request(
                method, path, body=data, headers=default_headers
            )
            status_code = response.status
            # In python3, defaultencoding is utf-8.
            # In python2, defaultencoding is ascii.
            response_str = response.data
            response_headers = response.headers
            response_str_decoded = response_str.decode("utf-8")
        except (urllib3.exceptions.ConnectTimeoutError) as e:
            LOGGER.error("Timed out request on %s, %s: %s", method, path, e)
            raise RequestTimedOutException("Timed out request: %s" % e) from None
        return {
            "response": response_str_decoded,
            "headers": response_headers,
            "status_code": status_code,
        }

    def get(self, path, headers=None):
        return self.request(path=path, method="GET", headers=headers)

    def post(self, path, data, headers=None):
        if isinstance(data, str):
            data_str = data
        else:
            data_str = json.dumps(data)
        return self.request(path=path, method="POST", headers=headers, data=data_str)
