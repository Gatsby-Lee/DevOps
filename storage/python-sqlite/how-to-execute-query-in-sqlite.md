how to execute query in sqlite
==============================

Standard by Cursor
-----------------------
```
c = sqlite3.connect()
cursor = c.cursor()
cursor.execute(query)
cursor.commit()
cursor.close()
c.close()
```

Non-Standard by Connection
----------------------
* shortcut of these
  * creating a cursor object by calling the cursor() method
  * calling the cursor’s execute() method with the parameters given
  * returning the cursor
```
c = sqlite3.connect()
c.execute(query)
c.commit()
c.close()
```
