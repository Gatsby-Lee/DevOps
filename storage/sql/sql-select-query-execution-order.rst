SQL SELECT Query Execution Order
================================

.. code-block:: sql

  SELECT DISTINCT <TOP_specification> <select_list>
  FROM <left_table>
  <join_type> JOIN <right_table>
  ON <join_condition>
  WHERE <where_condition>
  GROUP BY <group_by_list>
  HAVING <having_condition>
  ORDER BY <order_by_list>



1. **FROM** clause
2. **ON** clause in JOIN**
3. **JOIN** clause
4. **WHERE** clause
5. **GROUP BY** clause
6. **HAVING** clause
7. **SELECT** clause
8. **DISTINCT** clause
9. **ORDER BY** clause
10. **TOP** clause

External References 
-------------------
* https://www.designcise.com/web/tutorial/what-is-the-order-of-execution-of-an-sql-query
