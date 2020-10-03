About Python Doctest
====================

How to run
----------

**Option 1:**

.. code-block:: python

    if __name__ == "__main__":
        import doctest
        doctest.testmod()
        
And run,

.. code-block:: bash

    $ python m.py
    $ python m.py -v

**Option 2:**

.. code-block:: bash

    $ python -m doctest m.py
    $ python -m doctest m.py -v


How to handle long output
-------------------------

Use directives, ``+NORMALIZE_WHITESPACE``, ``+ELLIPSIS``

ref: https://docs.python.org/3/library/doctest.html#directives

.. code-block:: python

    """
    >>> print range(20) # doctest: +NORMALIZE_WHITESPACE
    [0,   1,  2,  3,  4,  5,  6,  7,  8,  9,
    10,  11, 12, 13, 14, 15, 16, 17, 18, 19]
    """
