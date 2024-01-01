=============================
How to Upload package to PyPi
=============================

Requirements
===================
* create account in https://test.pypi.org/
* create account in https://pypi.org/
* install twine - ``pip install twine``
* your packaged project

Setup credential ``~/.pypirc``
======================================================

NOTE: using username/password won't work anymore as of Two-way auth is enabled.

Either Trusted Publisher or API Token has to be used.

Ref: https://packaging.python.org/en/latest/specifications/pypirc/

* Create ``~/.pypirc`` with your credentials

.. code-block:: ini

  [distutils]
  index-servers =
    pypi
    testpypi
  
  [pypi]
  username=your_username
  password=your_password
  
  [testpypi]
  repository: https://test.pypi.org/legacy/
  username=your_username
  password=your_password


* OR Create ``~/.pypirc`` with your credentials

.. code-block:: ini

  [distutils]
  index-servers =
    pypi
    testpypi
  
  [pypi]
  username = __token__
  password = <TestPyPI token>
  
  [testpypi]
  repository: https://test.pypi.org/legacy/
  username = __token__
  password = <TestPyPI token>


* change permission of file - ``chmod 600 ~/.pypirc``


Upload to TestPyPI (testing)
==============================
``twine upload --repository testpypi dist/*``

Uploaded package can be found::
  https://test.pypi.org

Test installing package in TestPyPI::
  ``pip install --index-url https://test.pypi.org/simple/ your-package``

If dependent packages need to be pulled from PyPI, use `--extra-index-url`::
  ``pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple your-package``


In case, the upload doesn't work due to some format issue.

.. code-block:: bash

  # first, check `long_description_content_type="text/markdown",` in setup.py if Markdown is used for README.md

  pip install -U twine wheel setuptools docutils

  https://github.com/pypi/warehouse/issues/5890#issuecomment-494868157
  rm -rf dist
  python setup.py sdist
  python setup.py bdist_wheel
  twine check dist/*


Upload to PyPI
==============================
``twine upload dist/*``

Uploaded package can be found::
  https://pypi.org

External References
===================
* https://packaging.python.org/guides/
* https://packaging.python.org/guides/using-testpypi/
* https://packaging.python.org/guides/distributing-packages-using-setuptools/
