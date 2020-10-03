Python Built-in Data Structures
===============================

list
----

**Convert List to Dict with index**

.. code-block:: python

  >>> a = [51,27,13,56]
  >>> b = dict(enumerate(a))

dict
----

**Fetch value by key**

.. code-block:: python

  # dict.get / dict.pop
  >>> a = {'name':'Gatsby'}
  >>> a.get('name')
  'Gatsby'
  >>> a.get('age') # no exception or error although key, `age` doesn't exist. Returns None
  >>> print(a.get('age', 23)) # use default, if `age` key doesn't exists.

two dimentional arrays with collections.defaultdict
---------------------------------------------------

.. code-block:: python

  >>> import collections
  >>> c = collections.defaultdict(lambda: collections.defaultdict(int))
  >>> c['a']['b'] += 1
