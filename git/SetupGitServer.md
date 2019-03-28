Setup Git Server
================

Setup `git` user
-----------------------
* `adduser git`
* `su git`
* `cd ~` or `cd`
* `mkdir .ssh && chmod 700 .ssh`
* `touch .ssh/authorized_keys && chmod 600 .ssh/authorized_keys`

Setup Git root repo dir
-----------------------
* `mkdir /srv/git`
* `chown git:git /srv/git`

Setup new Git repo
-----------------------
* `mkdir /srv/git/project_name.git`
* `git init --bare`

Add deverlop SSH key
----------------
* Append developer SSH Keys to `authorized_keys` for the `git` user
* `cat /tmp/id_rsa.john.pub >> ~/.ssh/authorized_keys`

Clone newly created Git repo
----------------
* `git clone git@gitserver:/srv/git/project_name.git`
* `cd project`
* `vim README`
* `git commit -am 'fix for the README file'`
* `git push origin master`


References
----------------
* https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server
