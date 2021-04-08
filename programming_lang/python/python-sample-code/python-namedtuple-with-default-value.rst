Python: Namedtuple with default value
=====================================

ref: https://stackoverflow.com/questions/11351032/namedtuple-and-default-values-for-optional-keyword-arguments/16721002

Python 3.7
----------

.. code-block:: python

  >>> from collections import namedtuple
  >>> fields = ('val', 'left', 'right')
  >>> Node = namedtuple('Node', fields, defaults=(None,) * len(fields))
  >>> Node()
  Node(val=None, left=None, right=None)


Before Python 3.7
-----------------

.. code-block:: python

  >>> from collections import namedtuple
  >>> Node = namedtuple('Node', 'val left right')
  >>> Node.__new__.__defaults__ = (None,) * len(Node._fields)
  >>> Node()
  Node(val=None, left=None, right=None)
