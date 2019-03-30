Redis Operation in general
==========================

Monitor Redis state
-------------------

.. code-block:: bash

  $ redis-cli --stat
  
  # output
  ------- data ------ --------------------- load -------------------- - child -
  keys       mem      clients blocked requests            connections          
  188        7.58M    144     105     3757434046 (+0)     9567463     
  196        8.91M    139     107     3757437367 (+3321)  9567465     
  ...
  
