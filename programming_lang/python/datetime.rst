All About datetime in Python
============================


Timezone
--------

.. code-block:: python

  # As of python 3.9, ZoneInfo can be used
  from datetime import datetime, timedelta
  from zoneinfo import ZoneInfo
  now_current_tz = datetime.now(tz=ZoneInfo("America/Los_Angeles"))
  prev_current_tz = now_current_tz - timedelta(seconds=3600)


Loading string datetime
-----------------------

.. code-block:: python
  
  from datetime import datetime
  a = '2023-10-08 16:52:32.459914-07:00'
  datetime.strptime(a, '%Y-%m-%d %H:%M:%S.%f%z')
