How to Handle exception in Python Unittest
==========================================


with context manager
--------------------

.. code-block:: python

  def test_1_cannot_add_int_and_str(self):
      with self.assertRaises(TypeError):
          1 + '1'

without context manager
-----------------------

.. code-block:: python

  def test_2_cannot_add_int_and_str(self):
      import operator
      self.assertRaises(TypeError, operator.add, 1, '1')

Tag
---
* python
* python unittest
* unittest

