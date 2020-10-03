How to Package Python Project
=============================

Check Description Locally
-------------------------

.. code-block:: bash

    $ pip install readme_renderer
    $ python setup.py check -r -s
    running check
    The project's long description is valid RST.


Build Source distributions ( Required )
---------------------------------------

.. code-block:: bash

    python setup.py sdist

External References
-------------------
* https://github.com/pypa/readme_renderer
* https://packaging.python.org/guides/distributing-packages-using-setuptools/
