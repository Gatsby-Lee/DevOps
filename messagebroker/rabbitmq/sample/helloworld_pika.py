"""
:author: Gatsby Lee
:since: 2019-03-28
"""
import logging
import os
import pika

LOGGER = logging.getLogger(__name__)

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
RABBITMQ_VHOST = os.getenv('RABBITMQ_VHOST', 'localhost')
RABBITMQ_USER = os.getenv('RABBITMQ_USER', '')
RABBITMQ_PASSWD = os.getenv('RABBITMQ_PASSWD', '')

CREDENTIAL_OBJ = pika.credentials.PlainCredentials(
    username=RABBITMQ_USER, password=RABBITMQ_PASSWD)

CONNECTION_PARAM = pika.ConnectionParameters(
    host=RABBITMQ_HOST, virtual_host=RABBITMQ_VHOST, credentials=CREDENTIAL_OBJ)


def create_queue(qname: str):
    with pika.BlockingConnection(CONNECTION_PARAM) as conn:
        channel = conn.channel()
        channel.queue_declare(qname)


def publish(qname: str, msg: str):
    with pika.BlockingConnection(CONNECTION_PARAM) as conn:
        channel = conn.channel()
        # Empty exchange means using default exchange
        # And, it's possible to define queue the msg should go by routing_key.
        channel.basic_publish(exchange='',
                              routing_key=qname,
                              body=msg)


if __name__ == '__main__':
    _qname = 'hello'
    create_queue(_qname)
    publish(_qname, 'hello world!!')
