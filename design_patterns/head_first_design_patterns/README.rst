Head First - Design Patterns
============================

Chapter 1
----------

객체지향의 기초

* 추상화 ( abstration )
* 캡슐화 ( encapsulation )
* 다형성 ( polymorphism )
* 상속 ( inheritance )


객체지향 원칙

* 바뀌는 부분을 분리하여 캡슐화 한다.
* 상속(inheritance)보다는 구성(composition)을 활용한다.
* 구현이 아닌 인터페이스에 맞춰서 프로그래밍한다. ( favor composition over inheritance )


객체지향 패턴 ( Strategy Pattern )

알고리즘군을 정의하고 각각을 캡슐화하여 교환해서 사용 할 수 있도록 만든다. Strategy Patter을 활용하면
알고리즘을 사용하는 클라이언트와는 독립적으로 알고리즘을 변경 할 수 있다.
( The 'Strategy Pattern' defines a family of algorithms, encapsulate each one,
and make them interchangeable. Strategy lets the algorithms vary independently from clients that use it. )
