# https://docs.python.org/3/tutorial/errors.html
import logging

logging.basicConfig(level=logging.INFO)

try:
    raise ValueError
except Exception:
    logging.info("handle exception")
    raise  # re-raising ValueError exception
