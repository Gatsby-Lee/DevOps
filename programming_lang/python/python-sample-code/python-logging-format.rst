Python Logging Format
#####################

Used most
=========

.. code-block:: python

  "%(asctime)s (%(filename)s, %(funcName)s, %(lineno)d) [%(levelname)8s] %(message)s"
  "%(asctime)s (%(filename)s, %(funcName)s, %(lineno)d) [%(levelname)8s] %(threadName)s %(message)s"
  "%(asctime)s (%(filename)s, %(funcName)s, %(lineno)d) [%(levelname)8s] %(process)s %(threadName)s %(message)s"


basicConfig
===========

.. code-block:: python

  FORMAT = '%(asctime)s (%(filename)s, %(funcName)s, %(lineno)d) [%(levelname)8s] %(message)s'
  logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt='%Y-%m-%d %H:%M:%S')
