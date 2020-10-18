Jenkins CI / Gerrit / Large Git Rep
###################################

Context
=======

* Google Kubernetes Engine
* Setup Jenkins CI ( master / agent ) on GKE by Helm Chart
* Gerrit in private in-house machine
* Run a Jenkins build with one of directory in repo, size around 1.3G
* Using Pipeline

Problem
=======

* By default, Jenkins git-fetch ( not git-pull ) Repo.
* Reducing the amount of data make it efficient ( faster )


How to optimize
===============

1. Reducing the amount code to fetch ( Checkout code only you need )
2. Reducing the amount of .git data to fetch

  * don't fetch tags
  * don't let intial-clone do full-fetching
  * don't fetch all git commit history ( fetch only recent history or just the latest one )


1. Reducing the amount code to fetch
------------------------------------

"Sparse checkout" - checkout directory / code only what you need

* Pipeline: pipeline script from SCM
* Advanced behaviours: Sparse Checkout paths


2. Reducing the amount of .git data to fetch
------------------------------------

* Pipeline: pipeline script from SCM
* Advanced behaviours: Advanced clone behaviours

  * uncheck "fetch tags"
  * check "Honor refspec on initial clone"
  * check "Shallow clone" - If "Shallow clone depth" is empty, the only latest one will be fetched.


References
==========

* https://www.jenkins.io/files/2016/jenkins-world/large-git-repos.pdf
* https://aws.amazon.com/blogs/devops/using-jenkins-with-codeartifact/
