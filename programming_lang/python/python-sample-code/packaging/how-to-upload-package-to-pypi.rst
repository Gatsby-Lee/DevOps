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
============================
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
