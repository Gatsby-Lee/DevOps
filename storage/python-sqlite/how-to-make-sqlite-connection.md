how to make sqlite connection
==============================

Memory based Storage
--------------------
```
import sqlite3
c = sqlite3.connect(':memory:')
```
* Storage is process level scope, it cannot be accessed by other processes.


File based Storage
--------------------
```
import sqlite3
c = sqlite3.connect('/tmp/test.db')
```

