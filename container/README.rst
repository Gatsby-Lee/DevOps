Container
=========

* `Build simple docker flask app: <https://github.com/Gatsby-Lee/simple_docker_flask_app>`_


Docker: Understand how CMD and ENTRYPOINT interact
--------------------------------------------------

ref: https://docs.docker.com/engine/reference/builder/#understand-how-cmd-and-entrypoint-interact

Both CMD and ENTRYPOINT instructions define what command gets executed when running a container. There are few rules that describe their co-operation.

1. Dockerfile should specify at least one of CMD or ENTRYPOINT commands.

2. ENTRYPOINT should be defined when using the container as an executable.

3. CMD should be used as a way of defining default arguments for an ENTRYPOINT command or for executing an ad-hoc command in a container.

4. CMD will be overridden when running the container with alternative arguments.

5. The table below shows what command is executed for different ENTRYPOINT / CMD combinations:
