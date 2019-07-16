Build/Upload Container to Google Container Registry
===================================================

Prepare Simple Flask Application
------------------------------

.. code-block:: bash

    git clone git@github.com:Gatsby-Lee/simple_docker_flask_app.git


Build Docker Container
----------------------

Be sure to include the '.' at the end of the command.
This tells Docker to start looking for the Dockerfile in the current working directory.

.. code-block:: bash

    docker build -t py-web-server:v1 .


Run/Test Container
------------------

Run container / Make request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    docker run -d -p 5000:5000 --name py-web-server -h my-web-server py-web-server:v1
    curl http://localhost:5000


Stop container
^^^^^^^^^^^^^^

.. code-block:: bash

    docker rm -f py-web-server


Upload Container to Google Container Registry
---------------------------------------------

Build Container with gcr.io tag
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Upload the Docker image to your private image repository in Google Cloud Registry (gcr.io).

.. code-block:: bash

    export GCP_PROJECT=<your_project>
    docker build -t "gcr.io/${GCP_PROJECT}/py-web-server:v1" .


Upload Container to Google Container Registry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configure Docker to use gcloud as a Container Registry credential helper (you are only required to do this once).

.. code-block:: bash

    PATH=/usr/lib/google-cloud-sdk/bin:$PATH
    gcloud auth configure-docker
    docker push gcr.io/${GCP_PROJECT}/py-web-server:v1


Container can be found in `Container Registry`

Container Image binary can be found in your Google Cloud Storage


Run Container with Image in Container Registry
----------------------------------------------

Run container / Make request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    docker run -d -p 5000:5000 --name py-web-server -h my-web-server gcr.io/${GCP_PROJECT}/py-web-server:v1
    curl http://localhost:5000


Stop container
^^^^^^^^^^^^^^

.. code-block:: bash

    docker rm -f py-web-server

