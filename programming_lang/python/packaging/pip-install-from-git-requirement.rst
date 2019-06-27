pip install from Git in requirements.txt
========================================

Typically using pypi server to install packages

.. code-block:: text

  boto3==1.9.178
  retry-redis


Using Git repo
--------------

``-e`` option is necessy to freeze package info properly

.. code-block:: text

  -e git@github.com:Gatsby-Lee/retry-redis.git@v1.1.1#egg=retry-redis
  boto3==1.9.178
  retry-redis
