Chapter 1
=========

사용된 디자인
----------

* 오리 - Duck (Abstract Class) 를 Parent Class로 정의.
* Child Class에서 반복적/공통적으로 사용 될만한 method는 구현.
* Abstract method를 이용하여, method에 signature를 규정해 두므로서 Child Class가 반드시 구현(implementing) 하도록 하였다.

기대 되어지는 효과
--------------

* 공통된 코드가 Duck에 구현 되어 있기 때문에 코드의 재활용 ( code reusablity ) 향상을 기대 할 수 있다.


문제가 무엇인가??
-------------

Duck에 구현된 method가 모든 Child Class에 적합하지는 않다. 그 예를, 날 수 없는 오리가(고무 오리 - RubberDuck) 날 수 있게 되는 경우를 예를 들고 있다.
RubberDuck이 날지 못하게 하는 방법 중에 하나는 fly() method를 overriding 해서 날지 못하는 방법을 보여준다.
하지만, 날 수 없는 오리들마다 fly() method를 overriding 해야 하는 문제점을 보여준다.


Java의 Interface 개념을 이용한다면? Flyable()
----------------------------------------

날 수 있는 오리들만 Flyable()을 구현하게 하는 방법을 제시하지만, 이 방법은 날 수 있는 오리들마다 같은 코드가 중복 될 수 있으므로 적절하지 않다고 말한다.


여기서 디자인 원칙!!
--------------

애플리케이션에서 달라지는 부분을 찾아내고, 달라지지 않는 부분으로부터 분리시킨다.


그래서 무엇이 달라지는 부분이라는 것인가?
-------------------------------

오리마다 달라지는 부분중에 하나는 나는 방법 fly()이다.


그래서 Child Class마다 다른 fly()를 어쩌겠다는 말인가?
----------------------------------------------

fly()를 더 이상 Duck의 Child Class가 구현(Implementing) 하게 하지 않고,
별도의 Class로 통해 행위를 구현한다. 이때 중요한 것은 Interface를 기준으로 구현한다는 점이다.

.. code-block:: python

  class FlyBehavior:
    def fly():
      raise NotImplemented()

  class FlyWithWings(FlyBehavior)
    def fly():
      // fly with wings implementation

  class FlyNoWay(FlyBehavior)
    def fly():
      // no fly

여기서 다시 디자인 원칙!!
-------------------

구현이 아닌 인터페이스에 맞춰서 프로그래밍한다.
( Program to an interface, not an implementation )


뭔 말이냐? 인터페이스에 맞춰서 프로그래밍한다는 것이??
-----------------------------------------

Client가 특정 구현 객체가 아닌 Interface를 이용하여 사용 할 수 있게 하는것.

예를들어, Client는 자신이 사용 하는 FlyBehavior가 어떤 것이지 상관없이 fly()를 통해 원하는 fly()를 할 수 있다는 것을 의미한다.
좀 더 Java적으로 설명하자면,

.. code-block:: java

  FlyBehavior f = new FlyWithWings()
  f.fly()


여기서 다시 디자인 원칙!!
-------------------

상속보다는 구성을 활용한다. ( Favor composition over inheritance )


뭔말이냐?? 구성을 활용한다는 말이??
---------------------------

상속을 통해서 반복되는 행동을 사용 하는 것이 아니라, 반복 되는 행동을 행동 객체로 분리하여 사용 하는 방법(?)

예를들면, 오리가 fly()를 구현해 놓고 상속하게끔 하는게 아니라, 분리되는 구현된 fly()를 사용하는 것.

.. code-block:: python

  class Duck(object):

    fly_behavior = None

  class RubberDuck(Duck):

    def __init__(self, fly):
      self.fly_behavior = fly


  duck = RubberDuck(FlyWithWings())


객체지향 패턴 ( Strategy Pattern )
-------------------------------

알고리즘군을 정의하고 각각을 캡슐화하여 교환해서 사용 할 수 있도록 만든다. Strategy Patter을 활용하면
알고리즘을 사용하는 클라이언트와는 독립적으로 알고리즘을 변경 할 수 있다.
( The 'Strategy Pattern' defines a family of algorithms, encapsulate each one,
and make them interchangeable. Strategy lets the algorithms vary independently from clients that use it. )
