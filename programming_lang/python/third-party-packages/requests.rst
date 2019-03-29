requests
========
* http://docs.python-requests.org/en/master/



Diff between res.text and res.content
-------------------------------------

* res.text is for text response, such as html, xml
* res.content is for binary response like PDF
* ref: http://docs.python-requests.org/en/master/user/quickstart/#binary-response-content

.. code-block:: python

  >>> r.content
  b'[{"repository":{"open_issues":0,"url":"https://github.com/...

  >>> from PIL import Image
  >>> from io import BytesIO

  >>> i = Image.open(BytesIO(r.content))

