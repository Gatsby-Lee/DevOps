Desigin Codebase for Pyramid Framework WEB service
==================================================

Approach 1
----------

Objectives
^^^^^^^^^^

* Simple
* Build service quickly
* Only focus on building WEB service

Directory
^^^^^^^^^

* git repo name: smile
* pyramid app package name: smile_pyramid_web
* pyramid app base dir: smile/smile_pyramid_web/web

.. code-block:: text

    smile
    |-- bin
    `-- smile_pyramid_web
        |-- ini
        |   |-- dev.ini
        |   `-- prod.ini
        |-- setup.py
        `-- web
            |-- __init__.py
            |-- model
            |   `-- __init__.py
            `-- view
                `-- __init__.py
                

Analysis
--------

* no consideration for building re-usable logic between API and WEB service.
* only WEB service is in repo.
* Pysically seperate API and WEB service codbase for cohesion 



Approach 2
----------

Objectives
^^^^^^^^^^

* Reduce maintainance cost by sharing common logic for API and WEB service.
* Build reusable logic/module for API and WEB service
* Define interface for application logic for API and API and WEB service


What can be common between API and WEB service?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* service(application logic) like common CRUD.

What can be common between API and WEB service?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* The way handling Client Request?
* The way handling Authenticate Client?
* The format of Response?
* The latency of Response?


Directory
^^^^^^^^^

* git repo name: smile
* pyramid app package name: smile_pyramid_web
* pyramid app base dir: smile/smile_pyramid_web/web


.. code-block:: text

    smile
    |-- bin
    |-- smile_grpc_api
    |-- smile_pyramid_web
    |   |-- ini
    |   |   |-- dev.ini
    |   |   `-- prod.ini
    |   |-- setup.py
    |   `-- web
    |       |-- __init__.py
    |       `-- view
    |           `-- __init__.py
    `-- smilepy
        |-- __init__.py
        |-- gutil
        |   `-- __init__.py
        |-- model
        |   |-- __init__.py
        |   `-- user.py
        `-- service
            |-- __init__.py
            `-- user.py

    10 directories, 11 files
 
 
 
Analysis
-----------
 
smile/smilepy
^^^^^^^^^^^^^
 
* Hold re-usable module
* Define service(application logic) which can be used by `smile_pyramid_web` and `smile_grpc_api`
 
 
smile/smile_pyramid_web
^^^^^^^^^^^^^^^^^^^^^^^
 
* root of Pyramid WEB service ( package )
* Define `setup.py`
 
 
