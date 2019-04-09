Tag
===

.. code-block:: bash

  # create tag
  git tag -a v0.2.0 <commit_hash>
  # share tag ( or push tag on remote )
  git push origin v0.2.0

  # delete tag
  git tag -d v0.2.0
  # delete tag on remote
  git push origin :refs/tags/v0.2.0
