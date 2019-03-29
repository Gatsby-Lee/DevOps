How to handle exception in doctest
==================================

.. code-block:: python

  def add_number(a,b):
  """
  >>> add_number(1,'b')
  Traceback (most recent call last):
  ...
  TypeError: unsupported operand type(s) for +: 'int' and 'str'
  """
  return a+b


External References
-------------------
* https://docs.python.org/3/library/doctest.html#what-about-exceptions
