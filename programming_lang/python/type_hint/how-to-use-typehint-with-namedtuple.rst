How to use TypeHint with NamedTuple
===================================

.. code-block:: python

  from collections import namedtuple

  CategoryNode = namedtuple('CategoryNode', ('cid', 'fname'))


.. code-block:: python

  from typing import NamedTuple

  class CategoryNode(NamedTuple):
      cid: str
      fname: str

