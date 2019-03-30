SQL LEFT OUTER JOIN ( or. LEFT JOIN )
==================

.. image:: https://www.w3schools.com/sql/img_leftjoin.gif
   :target: https://www.w3schools.com/sql/img_leftjoin.gif
   :alt: www.w3schools.com
(image source: www.w3schools.com )


Summary
-------

* The **LEFT OUTER JOIN** returns

  - **ALL** records from **Left Table** (table1)
  
    - This is VERY Important. Left Table can't be filtered by On clause as expected. )

  - matched records by **ON clause** from **Right Table** or Null value if not matched.



LEFT OUTER JOIN Syntax
----------------------

.. code-block:: sql

  SELECT column_name(s)
  FROM table1
  LEFT JOIN table2 ON table1.column_name = table2.column_name;


LEFT OUTER JOIN output
----------------------

Test data
^^^^^^^^^

.. code-block:: sql

  CREATE TABLE fruit (
    fruit_id int,
    fruit_name VARCHAR(255),
    color_id int
  );
  CREATE TABLE color (
    color_id int,
    color_name VARCHAR(255)
  );
  INSERT into color VALUES (1,'orange'), (2,'yellow'), (3,'red'), (4,'blue');
  INSERT into fruit VALUES (1, 'banana',2), (2, 'mango',2), (3, 'orange',1), (4, 'apple',3), (5, 'grapes',5), (6, 'avocado',null), (7, 'banana',8);

records in **fruit table**

.. code-block:: text

    fruit_id |fruit_name |color_id |
    ---------|-----------|---------|
    1        |banana     |2        |
    2        |mango      |2        |
    3        |orange     |1        |
    4        |apple      |3        |
    5        |grapes     |5        |
    6        |avocado    |Null     |
    7        |banana     |8        |


records in **color table**

.. code-block:: text

    color_id |color_name |
    ---------|-----------|
    1        |orange     |
    2        |yellow     |
    3        |red        |
    4        |blue       |


Test LEFT OUTER JOIN
^^^^^^^^^^^^^^^^^^^^

* ALL records in **Fruit Table** are returned even for the records which don't have matched color_id on **Color Table**, such as fruit_id in (5,6,7)
* Null values are returned from **Color Table** if matched color_id does't exist for color_id in (5,Null,8)

.. code-block:: sql

    select * from fruit f
    left outer join color c on f.color_id = c.color_id;

    fruit_id |fruit_name |color_id |color_id |color_name |
    ---------|-----------|---------|---------|-----------|
    3        |orange     |1        |1        |orange     |
    1        |banana     |2        |2        |yellow     |
    2        |mango      |2        |2        |yellow     |
    4        |apple      |3        |3        |red        |
    5        |grapes     |5        |Null     |Null       |
    6        |avocado    |Null     |Null     |Null       |
    7        |banana     |8        |Null     |Null       |


.. code-block:: sql

    select * from fruit f
    left outer join color c on f.color_id = c.color_id and c.color_name = 'red';

    fruit_id |fruit_name |color_id |color_id |color_name |
    ---------|-----------|---------|---------|-----------|
    4        |apple      |3        |3        |red        |
    1        |banana     |2        |Null     |Null       |
    2        |mango      |2        |Null     |Null       |
    3        |orange     |1        |Null     |Null       |
    5        |grapes     |5        |Null     |Null       |
    6        |avocado    |Null     |Null     |Null       |
    7        |banana     |8        |Null     |Null       |

.. code-block:: sql

    select * from fruit f
    left outer join color c on f.color_id = c.color_id and f.fruit_name = 'banana';

    fruit_id |fruit_name |color_id |color_id |color_name |
    ---------|-----------|---------|---------|-----------|
    1        |banana     |2        |2        |yellow     |
    2        |mango      |2        |Null     |Null       |
    3        |orange     |1        |Null     |Null       |
    4        |apple      |3        |Null     |Null       |
    5        |grapes     |5        |Null     |Null       |
    6        |avocado    |Null     |Null     |Null       |
    7        |banana     |8        |Null     |Null       |

    select * from fruit f
    left outer join color c on f.color_id = c.color_id and f.fruit_name = 'banana'
    where c.color_id is null;

    fruit_id |fruit_name |color_id |color_id |color_name |
    ---------|-----------|---------|---------|-----------|
    2        |mango      |2        |Null     |Null       |
    3        |orange     |1        |Null     |Null       |
    4        |apple      |3        |Null     |Null       |
    5        |grapes     |5        |Null     |Null       |
    6        |avocado    |Null     |Null     |Null       |
    7        |banana     |8        |Null     |Null       |

.. code-block:: sql

    select * from fruit f
    left outer join color c on f.color_id = c.color_id
    where f.fruit_name = 'banana';

    fruit_id |fruit_name |color_id |color_id |color_name |
    ---------|-----------|---------|---------|-----------|
    1        |banana     |2        |2        |yellow     |
    7        |banana     |8        |Null     |Null       |

    select * from fruit f
    left outer join color c on f.color_id = c.color_id
    where f.fruit_name = 'banana' and c.color_id is null;

    fruit_id |fruit_name |color_id |color_id |color_name |
    ---------|-----------|---------|---------|-----------|
    7        |banana     |8        |Null     |Null       |


External References
-------------------
* https://stackoverflow.com/questions/354070/sql-join-where-clause-vs-on-clause/354094
* https://stackoverflow.com/questions/34085064/why-left-join-on-clause-doesnt-work/34085154#34085154
* http://www.tech-recipes.com/rx/47637/inner-and-left-outer-join-with-where-clause-vs-on-clause/
* https://stackoverflow.com/questions/42288760/sql-filter-left-table-before-left-join?rq=1
* https://community.modeanalytics.com/sql/tutorial/sql-pivot-table/
* https://blog.jooq.org/2014/11/20/use-mysqls-strict-mode-on-all-new-projects/
