"""
:author: Gatsby Lee
:since: 2019-03-28
"""
import argparse
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


def publish(qname: str, msg: str):
    with pika.BlockingConnection(CONNECTION_PARAM) as conn:
        channel = conn.channel()
        # create queue - idempotent
        channel.queue_declare(qname)
        # Empty exchange means using default exchange
        # And, it's possible to define queue the msg should go by routing_key.
        channel.basic_publish(exchange='',
                              routing_key=qname,
                              body=msg)

        LOGGER.info('Sent msg to qname=%s', qname)


def consumer(qname: str):

    def callback(ch, method, properties, body):
        print("Received msg: %r" % body)

    with pika.BlockingConnection(CONNECTION_PARAM) as conn:
        channel = conn.channel()
        channel.basic_consume(
            queue=qname, on_message_callback=callback, auto_ack=True)

        LOGGER.info('Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()


def __parse_args():

    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('--qname', default='hello')

    parser = argparse.ArgumentParser(parents=[parent_parser])
    cmd_parser = parser.add_subparsers(dest='cmd', required=True)

    publisher_parser = cmd_parser.add_parser('publisher')
    publisher_parser.add_argument('--msg', required=True)
    consumer_parser = cmd_parser.add_parser('consumer')

    return parser.parse_args()


if __name__ == '__main__':

    # logging.basicConfig(level=logging.INFO)

    args = __parse_args()
    _qname = args.qname
    if args.cmd == 'publisher':
        publish(_qname, args.msg)
    elif args.cmd == 'consumer':
        consumer(_qname)
