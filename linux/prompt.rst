Prompt
======

.bashrc
-------

.. code-block:: bash

  $ cat ~/.bashrc 
  # .bashrc

  # Source global definitions
  if [ -f /etc/bashrc ]; then
      . /etc/bashrc
  fi

  # User specific aliases and functions
  PS1="[\t \u@\h:\w]$ "
