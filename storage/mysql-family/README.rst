MySQL Family
============


Get size of table
-----------------

.. code-block:: SQL

    SELECT 
        table_name AS `Table`, 
        round(((data_length + index_length) / 1024 / 1024 / 1024), 2) `Size in GB` 
    FROM information_schema.TABLES 
    WHERE table_schema = "<database>"
        AND table_name = "<table-name>";
