Summary in Quick Tutorial for Pyramid
=====================================
* https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/index.html

Note
----

* workspace: smile
* project: SmilePyramidApi
* repo(module to import): smile_api


Installation / Requirement
--------------------------

.. code-block:: bash

  $ mkdir -p /home/web/smile_pyramid/{smileweb,ini}
  $ mkdir -p /home/web/smile_pyramid/smileweb/template
  $ mkdir -p /home/web/smile_pyramid/smileweb/static
  $ cd /home/web/smile_pyramid
  $ python3.6 -m venv py36_smile_pyramid
  $ source py36_smile_pyramid/bin/activate
  (py36_smile_pyramid)$ pip install --upgrade pip setuptools
  (py36_smile_pyramid)$ pip install "pyramid==1.9.2" waitress


01: Single-File Web Applications
--------------------------------

1. Create directories

.. code-block:: bash

  $ mkdir -p /home/web/smile_pyramid/smileweb; cd /home/web/smile_pyramid/smileweb


2. Create `/home/web/smile_pyramid/smileweb/app.py` with below code single_hello_world_code_extref_

.. _single_hello_world_code_extref: https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/hello_world.html


.. code-block:: python

    from waitress import serve
    from pyramid.config import Configurator
    from pyramid.response import Response


    def hello_world(request):
        print('Incoming request')
        return Response('<body><h1>Hello World!</h1></body>')


    if __name__ == '__main__':
        with Configurator() as config:
            config.add_route('hello', '/')
            config.add_view(hello_world, route_name='hello')
            app = config.make_wsgi_app()
        serve(app, host='0.0.0.0', port=6543)


Current directory should be like this

.. code-block:: text

    (py36_smile_pyramid)$ cd /home/web/; tree -I py36_smile_pyramid_api smile_pyramid
    smile_pyramid
    `-- smileweb
        `-- app.py

    1 directory, 1 file


3. Run the application:

.. code-block:: bash

  (py36_smile_pyramid)$ cd /home/web/smile_pyramid/smileweb; python app.py


4. Open http://localhost:6543/ in your browser.


02: Python Packages for Pyramid Applications
--------------------------------------------

What is Packages in Python?
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ref: https://docs.python.org/3/tutorial/modules.html#tut-packages
* Packages are a way of structuring Python’s module namespace by using “dotted module names”
* a package is a collection of modules.
* The __init__.py files are **REQUIRED** to make Python treat directories as containing packages.


1. Create /home/web/smile_pyramid/setup.py with below code.

  * /home/web/smile_pyramid_api is package directory


.. code-block:: python

    from setuptools import setup

    requires = [
        'pyramid',
        'waitress',
    ]

    setup(name='tutorial',
          install_requires=requires,
    )

2. Create /home/web/smile_pyramid/smileweb/__init__.py

.. code-block:: bash

  $ echo "#package" > /home/web/smile_pyramid/smileweb/__init__.py

3. Install package with development mode.


.. code-block:: bash

  (py36_smile_pyramid_api)$ cd /home/web/smile_pyramid; pip install -e .


3. Run the application:

.. code-block:: bash

  (py36_smile_pyramid)$ cd /home/web/smile_pyramid/smileweb; python app.py


4. Open http://localhost:6543/ in your browser.


03: Application Configuration with .ini Files
---------------------------------------------

Note
^^^^
* pserve looks for [app:main] and finds use = egg:tutorial.
* The projects's setup.py has defined an "entry point" (lines 10-13) for the project's "main" entry point of tutorial:main.
* The tutorial package's __init__ has a main function.
* This function is invoked, with the values from certain .ini sections passed in.

References
^^^^^^^^^^

* https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/environment.html
* https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/paste.html#paste-chapter

1. Create /home/web/smile_pyramid/ini directory.

.. code-block:: bash

  (py36_smile_pyramid)$ mkdir -p /home/web/smile_pyramid/ini


2. Update /home/web/smile_pyramid/setup.py with below code.

  * /home/web/smile_pyramid is package directory


.. code-block:: python

    from setuptools import setup

    requires = [
        'pyramid',
        'waitress',
    ]

    setup(name='smile_pyramid',
          install_requires=requires,
          entry_points="""\
          [paste.app_factory]
          main = smileweb:main
          """,
          )



3. Make a file /home/web/smile_pyramid/ini/dev.ini with below code

.. code-block:: ini

    [app:main]
    use = egg:smile_pyramid

    [server:main]
    use = egg:waitress#main
    listen = localhost:6543


4. Refactor app.py into /home/web/smile_pyramid/smileweb/__init__.py like below:

  * imperative configuration

.. code-block:: python

    from pyramid.config import Configurator
    from pyramid.response import Response


    def hello_world(request):
        return Response('<body><h1>Hello World!</h1></body>')


    def main(global_config, **settings):
        config = Configurator(settings=settings)
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        return config.make_wsgi_app()

5. Remove /home/web/smile_pyramid/smileweb/app.py

.. code-block:: bash

  (py36_smile_pyramid)$ /home/web/smile_pyramid/smileweb/app.py

6. Run Pyramid application with

* NOTE!!: `Serving on http://localhost:6543` is printed two times for IPv4 and IPv6
* ref: https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/startup.html#startup

.. code-block:: bash

    (py36_smile_pyramid)$ pserve ini/dev.ini --reload
    Starting monitor for PID 39799.
    Starting server in PID 39799.
    Serving on http://localhost:6543
    Serving on http://localhost:6543
 
7. Open http://localhost:6543/



07: Basic Web Handling With Views
---------------------------------

1. Update /home/web/smile_pyramid/smileweb/__init__.py like below:

.. code-block:: python

    from pyramid.config import Configurator


    def main(global_config, **settings):
        config = Configurator(settings=settings)
        # adding route mapping
        config.add_route('home', '/')
        config.add_route('hello', '/howdy')
        # auto-mapping
        config.scan('.views')
        return config.make_wsgi_app()


2. Create /home/web/smile_pyramid/smileweb/views.py with below code:

  *  declarative configuration in which a Python decorator is placed on the line above the view.

.. code-block:: python

    from pyramid.response import Response
    from pyramid.view import view_config


    # First view, available at http://localhost:6543/
    @view_config(route_name='home')
    def home(request):
        return Response('<body>Visit <a href="/howdy">hello</a></body>')


    # /howdy
    @view_config(route_name='hello')
    def hello(request):
        return Response('<body>Go back <a href="/">home</a></body>')


3. Run your Pyramid application with:

.. code-block:: bash

    (py36_smile_pyramid)$ pserve ini/dev.ini --reload
    Starting monitor for PID 44502.
    Starting server in PID 44502.
    Serving on http://localhost:6543
    Serving on http://localhost:6543


4. Open http://localhost:6543/ or http://localhost:6543/howdy


12: Templating With jinja2
--------------------------

* ref:

  * https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/jinja2.html
  * https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/routing.html

* More about Templates: https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/templates.html
* Merging with **08: HTML Generation With Templating**


1. This step depends on pyramid_jinja2, so add it as a dependency in /home/web/smile_pyramid/setup.py:

.. code-block:: python

    from setuptools import setup

    requires = [
        'pyramid',
        'pyramid_jinja2',
        'waitress',
    ]

    setup(name='smile_pyramid',
          install_requires=requires,
          entry_points="""\
          [paste.app_factory]
          main = smileweb:main
          """,
          )

2. We need to include pyramid_jinja2 in /home/web/smile_pyramid/smileweb/__init__.py:

.. code-block:: python

    from pyramid.config import Configurator


    def main(global_config, **settings):
        config = Configurator(settings=settings)
        # include pyramid_jinja2 package
        # this can be added into dev.ini as well instead.
        config.include('pyramid_jinja2')
        config.add_route('home', '/')
        config.add_route('hello', '/howdy')
        config.scan('.views')
        return config.make_wsgi_app()


3. Update /home/web/smile_pyramid/smileweb/views.py to use template

.. code-block:: python

    from pyramid.view import view_config


    # First view, available at http://localhost:6543/
    @view_config(route_name='home', renderer='home.jinja2')
    def home(request):
        return {'name': 'Home View'}


    # /howdy
    @view_config(route_name='hello', renderer='home.jinja2')
    def hello(request):
        return {'name': 'Hello View'}


4. Add /home/web/smile_pyramid/smileweb/template/home.jinja2 as a template:

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Quick Tutorial: {{ name }}</title>
    </head>
    <body>
    <h1>Hi {{ name }}</h1>
    </body>
    </html>


5. For convenience, change /home/web/smile_pyramid/ini/dev.ini to reload templates automatically with pyramid.reload_templates:

.. code-block:: python

    [app:main]
    use = egg:smile_pyramid
    pyramid.reload_templates = true

    [server:main]
    use = egg:waitress#main
    listen = localhost:6543


6. Run your Pyramid application with:

.. code-block:: bash

    (py36_smile_pyramid)$ pserve ini/dev.ini --reload
    Starting monitor for PID 44502.
    Starting server in PID 44502.
    Serving on http://localhost:6543
    Serving on http://localhost:6543


7. Open http://localhost:6543/ in your browser.


09: Organizing Views With View Classes
--------------------------------------

* ref: https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/view_classes.html


1. Update /home/web/smile_pyramid/smileweb/views.py like below:

.. code-block:: python

    from pyramid.view import (
        view_config,
        view_defaults
    )


    @view_defaults(renderer='smileweb:template/home.jinja2')
    class TutorialViews:
        def __init__(self, request):
            self.request = request

        @view_config(route_name='home')
        def home(self):
            return {'name': 'Home View'}

        @view_config(route_name='hello')
        def hello(self):
            return {'name': 'Hello View'}


2. Run your Pyramid application with:

.. code-block:: bash

    (py36_smile_pyramid)$ pserve ini/dev.ini --reload
    Starting monitor for PID 44502.
    Starting server in PID 44502.
    Serving on http://localhost:6543
    Serving on http://localhost:6543


3. Open http://localhost:6543/ in your browser.


11: Dispatching URLs To Views With Routing
------------------------------------------

1. Update /home/web/smile_pyramid/smileweb/__init__.py:

.. code-block:: python

    from pyramid.config import Configurator


    def main(global_config, **settings):
        config = Configurator(settings=settings)
        # include pyramid_jinja2 package
        # this can be added into dev.ini as well instea
        config.include('pyramid_jinja2')
        config.add_route('home', '/')
        config.add_route('hello', '/howdy/{first}/{last}')
        config.scan('.views')
        return config.make_wsgi_app()


2. Update /home/web/smile_pyramid/smileweb/views.py like below:

.. code-block:: python

    from pyramid.view import (
        view_config,
        view_defaults
    )


    @view_defaults(renderer='smileweb:template/home.jinja2')
    class TutorialViews:
        def __init__(self, request):
            self.request = request

        @view_config(route_name='home')
        def home(self):
            return {'name': 'Home View'}

        @view_config(route_name='hello')
        def hello(self):
            first = self.request.matchdict['first']
            last = self.request.matchdict['last']
            return {
                'name': 'Hello View',
                'first': first,
                'last': last
            }


4. Add /home/web/smile_pyramid/smileweb/template/home.jinja2 as a template:

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Quick Tutorial: {{ name }}</title>
    </head>
    <body>
    <h1>Hi {{ name }}</h1>
    <p>First: {{ first }}, Last: {{ last }}</p>
    </body>
    </html>


6. Run your Pyramid application with:

.. code-block:: bash

    (py36_smile_pyramid)$ pserve ini/dev.ini --reload
    Starting monitor for PID 44502.
    Starting server in PID 44502.
    Serving on http://localhost:6543
    Serving on http://localhost:6543


7. Open http://localhost:6543/howdy/hello/world in your browser. Check http://localhost:6543/howdy/ ( 404 ERROR )



13: CSS/JS/Images Files With Static Assets
------------------------------------------

* Ref About Cache Busting : https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/assets.html#cache-busting
* Preventing HTTP Cache: https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/environment.html#preventing-http-caching
* Cache Control in View: https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/viewconfig.html#influencing-http-caching


1. Update /home/web/smile_pyramid/smileweb/__init__.py:


.. code-block:: python

    from pyramid.config import Configurator


    def main(global_config, **settings):
        config = Configurator(settings=settings)
        # include pyramid_jinja2 package
        # this can be added into dev.ini as well instea
        config.include('pyramid_jinja2')
        config.add_route('home', '/')
        config.add_route('hello', '/howdy/{first}/{last}')
        config.add_static_view(name='static', path='smileweb:static')
        config.scan('.views')
        return config.make_wsgi_app()


2. Add a CSS link in the <head> of our template at /home/web/smile_pyramid/smileweb/template/home.jinja2:

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Quick Tutorial: {{ name }}</title>
        <link rel="stylesheet"
              href="{{ request.static_url('smileweb:static/app.css') }}"/>
    </head>
    <body>
    <h1>Hi {{ name }}</h1>
    <p>First: {{ first }}, Last: {{ last }}</p>
    </body>
    </html>


3. Add a CSS file at /home/web/smile_pyramid/smileweb/static/app.css:

.. code-block:: css

    body {
        margin: 2em;
        font-family: sans-serif;
    }


4. Run your Pyramid application with:

.. code-block:: bash

    (py36_smile_pyramid)$ pserve ini/dev.ini --reload
    Starting monitor for PID 44502.
    Starting server in PID 44502.
    Serving on http://localhost:6543
    Serving on http://localhost:6543


5. Open http://localhost:6543/howdy/hello/world in your browser.


Difference between request.static_path AND request.static_url
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**request.static_path:** showing path format for static asset


.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Quick Tutorial: Home View</title>
        <link rel="stylesheet"
              href="/static/app.css"/>
    </head>
    <body>
    <h1>Hi Home View</h1>
    <p>First: hello, Last: world</p>
    </body>
    </html>


**request.static_url:** showing url format for static asset


.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Quick Tutorial: Home View</title>
        <link rel="stylesheet"
              href="http://localhost:6543/static/app.css"/>
    </head>
    <body>
    <h1>Hi Home View</h1>
    <p>First: hello, Last: world</p>
    </body>
    </html>


14: AJAX Development With JSON Renderers
-----------------------------------------

* Like using Jinja2 renderer, JSON can used renderer as well.
* More about renderer: https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/renderers.html


1. Update /home/web/smile_pyramid/smileweb/__init__.py:


.. code-block:: python

    from pyramid.config import Configurator


    def main(global_config, **settings):
        config = Configurator(settings=settings)
        # include pyramid_jinja2 package
        # this can be added into dev.ini as well instea
        config.include('pyramid_jinja2')
        config.add_route('home', '/')
        config.add_route('hello', '/howdy/{first}/{last}')
        config.add_route('hello_json', '/howdy.json/{first}/{last}')
        config.add_static_view(name='static', path='smileweb:static')
        config.scan('.views')
        return config.make_wsgi_app()


2. Update /home/web/smile_pyramid/smileweb/views.py like below:

 * Same business logic `def hello` can be used for HTML and JSON

.. code-block:: python

    from pyramid.view import (
        view_config,
        view_defaults
    )


    @view_defaults(renderer='smileweb:template/home.jinja2')
    class TutorialViews:
        def __init__(self, request):
            self.request = request

        @view_config(route_name='home')
        def home(self):
            return {'name': 'Home View'}

        @view_config(route_name='hello')
        @view_config(route_name='hello_json', renderer='json')
        def hello(self):
            first = self.request.matchdict['first']
            last = self.request.matchdict['last']
            return {
                'name': 'Home View',
                'first': first,
                'last': last
            }


4. Run your Pyramid application with:

.. code-block:: bash

    (py36_smile_pyramid)$ pserve ini/dev.ini --reload
    Starting monitor for PID 44502.
    Starting server in PID 44502.
    Serving on http://localhost:6543
    Serving on http://localhost:6543


5. Open http://localhost:6543/howdy.json/hello/world in your browser.

Notes for JSON renderer
^^^^^^^^^^^^^^^^^^^^^^^

* In fact, for pure AJAX-style web applications, we could re-use the existing route by using Pyramid's view predicates to match on the Accepts: header sent by modern AJAX implementations.
* Pyramid's JSON renderer uses the base Python JSON encoder, thus inheriting its strengths and weaknesses. For example, Python can't natively JSON encode DateTime objects. There are a number of solutions for this in Pyramid, including extending the JSON renderer with a custom renderer.


15: More With View Classes ( Defining a View Callable as a Class )
------------------------------------------------------------------

* https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/views.html#class-as-view

  * an __init__ method that accepts a request argument
  * view object is available in template as well.

* https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/viewconfig.html#predicate-arguments
* https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/views.html

1. Update /home/web/smile_pyramid/smileweb/__init__.py:


.. code-block:: python

    from pyramid.config import Configurator


    def main(global_config, **settings):
        config = Configurator(settings=settings)
        # include pyramid_jinja2 package
        # this can be added into dev.ini as well instea
        config.include('pyramid_jinja2')
        config.add_route('post_list', '/post')
        config.add_route('post', '/post/{post_id}')
        config.add_static_view(name='static', path='smileweb:static')
        config.scan('.views')
        return config.make_wsgi_app()


2. Update /home/web/smile_pyramid/smileweb/views.py like below:

.. code-block:: python

    from pyramid.httpexceptions import HTTPFound
    from pyramid.view import (
        view_config,
        view_defaults
    )

    # testing purpose
    POSTS = {
        '1': {'post_id': 1, 'title': 'hello world'},
        '2': {'post_id': 2, 'title': 'nice weather'}
    }


    @view_defaults(route_name='post')
    class PostViews(object):
        def __init__(self, request):
            self.request = request
            self.view_name = 'PostViews'

        @view_config(route_name='post_list', renderer='smileweb:template/list.jinja2')
        def list(self):
            return {'posts': POSTS}

        @view_config(request_method='GET', renderer='smileweb:template/edit.jinja2')
        def edit_get(self):
            post_id = self.request.matchdict['post_id']
            return {'post': POSTS[post_id]}

        @view_config(request_method='POST', request_param='form.edit')
        def edit_post(self):
            post_id = self.request.matchdict['post_id']
            title = self.request.params['title']
            POSTS[post_id]['title'] = title
            return HTTPFound(location=self.request.route_path('post_list'))


3. Add /home/web/smile_pyramid/smileweb/template/list.jinja2 as a template:

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Quick Tutorial</title>
        <link rel="stylesheet"
              href="{{ request.static_url('smileweb:static/app.css') }}"/>
    </head>
    <body>
        <h1>Posts - {{ view.view_name }}</h1>
        <ul>
        {% for post_id, detail in posts.items() %}
            <li>{{ detail.title }}
                | <a href="{{ request.route_path('post', post_id=detail.post_id) }}">edit</a>
            </li>
        {% endfor %}
        </ul>
    </body>
    </html>


3. Add /home/web/smile_pyramid/smileweb/template/edit.jinja2 as a template:

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Quick Tutorial</title>
        <link rel="stylesheet"
              href="{{ request.static_url('smileweb:static/app.css') }}"/>
    </head>
    <body>
        <h1>Posts - {{ view.view_name }}</h1>
        <form method='POST' action="{{ request.route_path('post', post_id=post.post_id) }}">
            <input name='title' value='{{ post.title }}'>
            <input type='submit' name='form.edit' value='Save'>
        </form>
    </body>
    </html>


4. Run your Pyramid application with:

.. code-block:: bash

    (py36_smile_pyramid)$ pserve ini/dev.ini --reload
    Starting monitor for PID 44502.
    Starting server in PID 44502.
    Serving on http://localhost:6543
    Serving on http://localhost:6543


5. Open http://localhost:6543/post in your browser.


16: Collecting Application Info With Logging
--------------------------------------------

* https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/logging.html


5. Update /home/web/smile_pyramid/ini/dev.ini like below.

.. code-block:: ini

    [app:main]
    use = egg:smile_pyramid
    pyramid.reload_templates = true

    [server:main]
    use = egg:waitress#main
    listen = localhost:6543

    # Begin logging configuration

    [loggers]
    keys = root, smileweb

    [logger_root]
    level = INFO
    handlers = console

    [logger_smileweb]
    level = DEBUG
    handlers =
    qualname = smileweb

    [handlers]
    keys = console

    [handler_console]
    class = StreamHandler
    args = (sys.stderr,)
    level = NOTSET
    formatter = generic

    [formatters]
    keys = generic

    [formatter_generic]
    format = %(asctime)s %(levelname)-5.5s [%(name)s][%(threadName)s] %(message)s

    # End logging configuration


2. Update /home/web/smile_pyramid/smileweb/views.py like below:

.. code-block:: python

    import logging

    from pyramid.httpexceptions import HTTPFound
    from pyramid.view import (
        view_config,
        view_defaults
    )

    LOGGER = logging.getLogger(__name__)

    # testing purpose
    POSTS = {
        '1': {'post_id': 1, 'title': 'hello world'},
        '2': {'post_id': 2, 'title': 'nice weather'}
    }


    @view_defaults(route_name='post')
    class PostViews(object):
        def __init__(self, request):
            self.request = request
            self.view_name = 'PostViews'

        @view_config(route_name='post_list', renderer='smileweb:template/list.jinja2')
        def list(self):
            return {'posts': POSTS}

        @view_config(request_method='GET', renderer='smileweb:template/edit.jinja2')
        def edit_get(self):
            post_id = self.request.matchdict['post_id']
            LOGGER.info('edit request for post_id=%s', post_id)
            return {'post': POSTS[post_id]}

        @view_config(request_method='POST', request_param='form.edit')
        def edit_post(self):
            post_id = self.request.matchdict['post_id']
            title = self.request.params['title']
            POSTS[post_id]['title'] = title
            return HTTPFound(location=self.request.route_path('post_list'))


4. Run your Pyramid application with:

.. code-block:: bash

    (py36_smile_pyramid)$ pserve ini/dev.ini --reload
    Starting monitor for PID 44502.
    Starting server in PID 44502.
    Serving on http://localhost:6543
    Serving on http://localhost:6543


5. Open http://localhost:6543/post in your browser.


17: Transient Data Using Sessions
---------------------------------

* https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/sessions.html


What is Session?
^^^^^^^^^^^^^^^^

A namespace that is valid for some period of continual activity that can be used to represent a user's interaction with a web application.

Flash message?
^^^^^^^^^^^^^^
* ref: https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/sessions.html#flash-messages
* "Flash messages" are simply a queue of message strings stored in the session.
* To use flash messaging, you must enable a session factory
* Flash messaging has two main uses: 

  * to display a status message only once to the user after performing an "internal redirect"
  * to allow generic code to log messages for single-time display without having direct access to an HTML template.

1. Update /home/web/smile_pyramid/smileweb/__init__.py:

Initialize SignedCookieSessionFactory

.. code-block:: python

    from pyramid.config import Configurator
    from pyramid.session import SignedCookieSessionFactory


    def main(global_config, **settings):
        my_session_factory = SignedCookieSessionFactory(
            'itsaseekreet')
        config = Configurator(settings=settings,
                              session_factory=my_session_factory)
        # include pyramid_jinja2 package
        # this can be added into dev.ini as well instea
        config.include('pyramid_jinja2')
        config.add_route('post_list', '/post')
        config.add_route('post', '/post/{post_id}')
        config.add_static_view(name='static', path='smileweb:static')
        config.scan('.views')
        return config.make_wsgi_app()


2. Update /home/web/smile_pyramid/smileweb/views.py like below:

  * Add counter property
  * Use request.session.flash to send / use message in redirected view 

.. code-block:: python

    import logging

    from pyramid.httpexceptions import HTTPFound
    from pyramid.view import (
        view_config,
        view_defaults
    )

    LOGGER = logging.getLogger(__name__)

    # testing purpose
    POSTS = {
        '1': {'post_id': 1, 'title': 'hello world'},
        '2': {'post_id': 2, 'title': 'nice weather'}
    }


    @view_defaults(route_name='post')
    class PostViews(object):
        def __init__(self, request):
            self.request = request
            self.view_name = 'PostViews'

        @view_config(route_name='post_list', renderer='smileweb:template/list.jinja2')
        def list(self):
            return {'posts': POSTS}

        @view_config(request_method='GET', renderer='smileweb:template/edit.jinja2')
        def edit_get(self):
            post_id = self.request.matchdict['post_id']
            LOGGER.info('edit request for post_id=%s', post_id)
            return {'post': POSTS[post_id]}

        @view_config(request_method='POST', request_param='form.edit')
        def edit_post(self):
            post_id = self.request.matchdict['post_id']
            title = self.request.params['title']
            POSTS[post_id]['title'] = title
            self.request.session.flash('post is updated.')
            return HTTPFound(location=self.request.route_path('post_list'))

        @property
        def counter(self):
            session = self.request.session
            if 'counter' in session:
                session['counter'] += 1
            else:
                session['counter'] = 1

            return session['counter']



3. Update /home/web/smile_pyramid/smileweb/template/list.jinja2 as a template:

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Quick Tutorial</title>
        <link rel="stylesheet"
              href="{{ request.static_url('smileweb:static/app.css') }}"/>
    </head>
    <body>
        <h1>Posts - {{ view.view_name }} - view count {{ view.counter }}</h1>
        {% for msg in request.session.pop_flash() %}
        <p>{{ msg }}</p>
        {% endfor%}
        <hr />
        <ul>
        {% for post_id, detail in posts.items() %}
            <li>{{ detail.title }}
                | <a href="{{ request.route_path('post', post_id=detail.post_id) }}">edit</a>
            </li>
        {% endfor %}
        </ul>
    </body>
    </html>


4. Run your Pyramid application with:

.. code-block:: bash

    (py36_smile_pyramid)$ pserve ini/dev.ini --reload
    Starting monitor for PID 44502.
    Starting server in PID 44502.
    Serving on http://localhost:6543
    Serving on http://localhost:6543


5. Open http://localhost:6543/post in your browser.


05: Unit Tests and pytest
-------------------------

* ref: https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/unit_testing.html


06: Functional Testing with WebTest
-----------------------------------

* ref: https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/functional_testing.html




External References
-------------------

* Pyramid GitHub: https://github.com/Pylons/pyramid/
* Pyramid cookiecutters: https://github.com/Pylons?q=pyramid-cookiecutter
