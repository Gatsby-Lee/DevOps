GitNote
=======

Modify files
------------
* `git update-index --chmod=+x <file>`: add execute permission

Amend with author
-----------------
* `git commit --amend --author="Name <email>"`

Stash
-----
* `git stash -k`: stash files on change stage

set-upstream-to
---------------

* `git branch --set-upstream-to=<remove/branch> <localbranch>`

Commiter Info
-----
* `--global` option can be used to set config on global level
* `git config user.email "your_email"`: set user email on repo level ( override global one )
* `git config user.name "your_name"`: set user name on repo level ( override global one )


# Branch

Remove Remote branch
---------------------
* git push <remote_name> --delete <branch_name>
