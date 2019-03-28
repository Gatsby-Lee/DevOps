Start HelloWorld Server with Pyramid
====================================

Lesson1 : Helloworld Server 만들어 보기 ( 파일 하나로 서버 돌리기 )
-----------------------------------------------------------

Imperative Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

* Configurator().add_view를 통해서 view를 mapping 해주는 방식.
* view.py 하나 만들어서, 아래 코드 복사/붙이기 해서 실행. python view.py. virtualenv가 필요하면 알아서 환경에 들어가셔요.

.. code-block:: python

    from wsgiref.simple_server import make_server
    from pyramid.config import Configurator
    from pyramid.response import Response

    def hello_world(request):
        return Response('Hello %(name)s!' % request.matchdict)

    if __name__ == '__main__':
        config = Configurator()
        config.add_route('Hello', '/hello/{name}')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
        server = make_server('0.0.0.0', 8080, app)
        server.serve_forever()


Declarative Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

* 위와 같은 내용이다. 다른점은 Configurator.scan() 이용해서, 사용할 view를 scan해서 등록했다는 점이 다른다.

.. code-block:: python

    from wsgiref.simple_server import make_server
    from pyramid.config import Configurator
    from pyramid.response import Response
    from pyramid.view import view_config

    @view_config()
    def hello(request):
        return Response('Hello')

    if __name__ == '__main__':
        config = Configurator()
        config.scan()
        app = config.make_wsgi_app()
        server = make_server('0.0.0.0', 8080, app)
        server.serve_forever()
        

서버 돌려보기
^^^^^^^^^^

.. code-block:: bash

    $ python service/pyramid_helloworld/view.py 

* 브라우져 띄워서 아래와 같이 실행하면, 화면에 Hello World라고 뜸.

.. code-block:: text

    http://127.0.0.1:8080/hello/World
    
    
    
Lesson 2: Pyramid가 가지고 있는 pyramid_jinja2_starter scaffold 이용해서 프로젝트 기본뼈대 만들기
-------------------------------------------------------------------------------------

* Pyramid가 제공하는 pcreate를 이용해서 pyramid_jinja2_starter로 프로젝트의 뼈대를 만든다. ( pip install pyramid_jinja2 )

.. code-block:: bash

  $ pcreate -s pyramid_jinja2_starter <project_name>

* 만들어진 폴더와 파일들은 다음과 같을 것이다.

.. code-block:: text

  MyProject/
    |-- CHANGES.txt
    |-- development.ini
    |-- MANIFEST.in
    |-- myproject
    |   |-- __init__.py
    |   |-- static
    |   |   |-- pyramid-16x16.png
    |   |   |-- pyramid.png
    |   |   |-- theme.css
    |   |   `-- theme.min.css
    |   |-- templates
    |   |   `-- mytemplate.pt
    |   |-- tests.py
    |   `-- views.py
    |-- production.ini
    |-- README.txt
    `-- setup.py
    
* 만든 project를 distribution Install한다. 

  * 이것을 왜하냐?: 만든 project가 import statements나 또는 pserve, pshell, proutes, 또는 pviews이 찾을 수 있게 하기위해서다.
  
.. code-block:: bash

  cd MyProject
  pip install -e . 
  
* 설치가 끝나면, pserve를 이용해서 서버를 띄워본다. ( 참고로 Pyramid는 development server로 waitress 쓴다.

.. code-block:: bash

  $ pserve development.ini --reload

* 브라우져에서 페이지를 열어본다.

  http://127.0.0.1:6543/
