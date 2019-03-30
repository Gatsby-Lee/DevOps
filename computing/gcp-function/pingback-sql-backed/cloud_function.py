"""
@author Gatsby Lee
@since 2018-10-28

Pingback service with Google Cloud Fuction.

@run
- python3.7

@ref:
- https://cloud.google.com/functions/docs/sql
- http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response

@expected HTTP STATUS code
    200: a Row is created
    400: taskId param is not provided
    409: Duplicated entry exists.
    500: Server Error.

@expected environment variables
    INSTANCE_CONNECTION_NAME: Cloud SQL unix_socket
    DB_USER
    DB_PASSWORD
    DB_NAME
    TABLE_NAME
"""
import logging
import os
import time

import pymysql
from pymysql.err import OperationalError, IntegrityError

INSTANCE_CONNECTION_NAME = os.getenv('INSTANCE_CONNECTION_NAME', '<YOUR INSTANCE CONNECTION NAME>')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', '<YOUR DB USER>')
DB_PASSWORD = os.getenv('DB_PASSWORD', '<YOUR DB PASSWORD>')
DB_NAME = os.getenv('DB_NAME', '<YOUR DB NAME>')
TABLE_NAME = os.getenv('TABLE_NAME', '<TABLE_NAME>')

UNIX_SOCKET = '/cloudsql/%s' % INSTANCE_CONNECTION_NAME
MYSQL_CONFIG = {
    'host': DB_HOST,
    'user': DB_USER,
    'password': DB_PASSWORD,
    'db': DB_NAME,
    'charset': 'latin1',
    # 'cursorclass': pymysql.cursors.DictCursor,
    'autocommit': True
}

# Create SQL connection globally to enable reuse
# PyMySQL does not include support for connection pooling
MYSQL_CONN = None
QUERY_INSERT = 'INSERT INTO {} VALUES (%s, %s, %s)'.format(TABLE_NAME)
RESPONSE_HEADER = {"content-type": "application/json; charset=utf-8"}


def _get_cursor():
    """
    Helper function to get a cursor
    """

    # Keep any declared in global scope (e.g. MYSQL_CONN) for later reuse.
    global MYSQL_CONN

    try:
        return MYSQL_CONN.cursor()
    # if MYSQL_CONN is not initialized, then AttributeError is raised.
    except AttributeError:
        # Initialize connections lazily, in case SQL access isn't needed for this
        # GCF instance. Doing so minimizes the number of active SQL connections,
        # which helps keep your GCF instances under SQL connection limits.
        try:
            MYSQL_CONN = pymysql.connect(**MYSQL_CONFIG)
        except OperationalError:
            MYSQL_CONFIG['unix_socket'] = UNIX_SOCKET
            MYSQL_CONN = pymysql.connect(**MYSQL_CONFIG)
        return MYSQL_CONN.cursor()
    # PyMySQL does NOT automatically reconnect,
    # so we must reconnect explicitly using ping()
    except OperationalError:
        MYSQL_CONN.ping(reconnect=True)
        return MYSQL_CONN.cursor()


def create_row(task_id, post_id):
    """Create a row with the give task_id and post_id
        Args:
            task_id: str
            post_id: str
        Returns: None
    """
    # Remember to close SQL resources declared while running this function.
    with _get_cursor() as cursor:
        cursor.execute(QUERY_INSERT, (task_id, post_id, int(time.time())))


def pingback(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/0.12/api/#flask.Flask.make_response>`.

    @note possible request
    http://your-server.com/pingscript?taskId=$task_id
    http://your-server.com/pingscript?taskId=$task_id&postId=$post_id
    """

    task_id = None
    try:
        task_id = request.args['taskId']
    except Exception:
        return ('[400, ["FAIL", "taskId param is required."]]', 400, RESPONSE_HEADER)

    post_id = '-1'
    try:
        post_id = request.args['postId']
    except Exception:
        pass

    try:
        create_row(task_id, post_id)
        b = '[200, ["OK", ["%s", "%s"]]]' % (task_id, post_id)
        return (b, 200, RESPONSE_HEADER)
    except IntegrityError as e:
        return ('[409, ["FAIL", "Duplicated Entry"]]', 409, RESPONSE_HEADER)
    except Exception as e:
        logging.error(e)
        return ('[500, ["FAIL", "Server Error"]]', 500, RESPONSE_HEADER)
