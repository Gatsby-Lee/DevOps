"""
:author: Gatsby Lee
:since: 2019-07-03
"""

def add_to_root_logger():

    # https://cloud.google.com/logging/docs/setup/python

    # Imports the Google Cloud client library
    import google.cloud.logging
    # Instantiates a client
    client = google.cloud.logging.Client()
    # Connects the logger to the root logging handler; by default this captures
    # all logs at INFO level and higher
    # !!! --- This is the one adding Stackdriver handler to root logger
    client.setup_logging()

    # --
    # Once the handler is attached, any logs at, by default,
    # INFO level or higher which are emitted in your application will be sent to Logging:

    # Imports Python standard library logging
    import logging

    # The data to log
    text = 'Hello, world!'

    # Emits the data using the standard logging module
    logging.warn(text)

add_to_root_logger()
