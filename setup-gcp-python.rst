Setup GCP Python OSX
====================

ref: https://cloud.google.com/sdk/docs/quickstart-macos

Download / Install SDK (gcloud)
---------------------------------

* Download https://cloud.google.com/sdk/docs/ ( It will be downloaded to ~\Downloads )
* unzip downloaded SDK:: tar -xvzf google-cloud-sdk-*.tar.gz
* ./google-cloud-sdk/install.sh
* ./google-cloud-sdk/bin/gcloud init
* PATH will be updated. In order to apply updated path, source ~/.bash_profile


Install / Remove components
---------------------------

ref: https://cloud.google.com/sdk/docs/components

.. code-block:: bash

  $ gcloud components list
  $ gcloud components install app-engine-python
  $ gcloud components remove app-engine-python

Create Project
--------------

.. code-block:: bash

  gcloud projects create [YOUR_PROJECT_NAME] --set-as-default
  gcloud projects describe [YOUR_PROJECT_NAME]


Hello World - AppEngine
------------------------

ref: https://cloud.google.com/appengine/docs/standard/python/quickstart

.. code-block:: bash

  cd /home/web
  git clone https://github.com/GoogleCloudPlatform/python-docs-samples
  cd python-docs-samples/appengine/standard/hello_world
  dev_appserver.py app.yaml
  # open browser with http://localhost:8080/
  ## --- Deploying
  gcloud app deploy
  gcloud app browse


Code in python-docs-samples/appengine/standard/hello_world
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

main.py

.. code-block:: python

    import webapp2

    class MainPage(webapp2.RequestHandler):
        def get(self):
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Hello, World!')


    app = webapp2.WSGIApplication([
        ('/', MainPage),
    ], debug=True)
  
  
app.yaml
  
.. code-block:: yaml
  
    runtime: python27
    api_version: 1
    threadsafe: true

    handlers:
    - url: /.*
      script: main.app


My Hello World - AppEngine
------------------------

ref: https://cloud.google.com/appengine/docs/standard/python/quickstart

.. code-block:: bash

  cd /home/web
  git clone https://github.com/Gatsby-Lee/gcp-appengine-helloworld
  cd gcp-appengine-helloworld/flask_standard
  dev_appserver.py app.yaml
  # open browser with http://localhost:8080/
  ## --- Deploying
  gcloud app deploy
  gcloud app browse


Code in gcp-appengine-helloworld/flask_standard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

main.py

.. code-block:: python

    from flask import Flask

    app = Flask(__name__)


    @app.route('/')
    def index():
        return 'Flask - GoogleAppEngine(GAE) Standard'


    if __name__ == '__main__':
        app.run(debug=True)
  
  
app.yaml
  
.. code-block:: yaml
  
    runtime: python37
    api_version: 1
    threadsafe: true

    handlers:
    - url: /.*
      script: main.app
