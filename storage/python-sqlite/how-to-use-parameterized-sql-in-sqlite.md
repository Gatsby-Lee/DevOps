Python SQLite3
==============

Paramiterized SQL
-----------------
```
sql1 = 'select * from testing where :1 = :2'
cur.execute(sql1, ('column2', 'A'))
```
```
sql2 = 'update testing set %s = :1 where %s = :2' % ('column1', 'column2')
x = cur.execute(sql2, ('C', 'A'))
```

* https://stackoverflow.com/questions/11853167/parameter-unsupported-when-inserting-int-in-sqlite?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
* https://stackoverflow.com/questions/973541/how-to-set-sqlite3-to-be-case-insensitive-when-string-comparing?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
* https://stackoverflow.com/questions/12105198/sqlite-how-to-get-insert-or-ignore-to-work?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
* https://medium.com/@PyGuyCharles/python-sql-to-json-and-beyond-3e3a36d32853
