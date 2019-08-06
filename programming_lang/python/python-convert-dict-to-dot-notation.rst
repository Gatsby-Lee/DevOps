Python: Convert dict to dot notation
====================================

Python3


.. code-block:: python

  >>> from types import SimpleNamespace
  >>> d = {'name':'Gatsby', 'age':100}

  # init
  >>> s = SimpleNamespace(d)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: no positional arguments expected
  >>> s = SimpleNamespace(**d)

  >>> s
  namespace(age=100, name='Gatsby')
  >>> s.age
  100
  >>> s.name
  'Gatsby'

  # when accessing non-existing attribute
  >>> s.nickname
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  AttributeError: 'types.SimpleNamespace' object has no attribute 'nickname'
