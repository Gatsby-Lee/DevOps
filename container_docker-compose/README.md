# docker-compose spec

https://github.com/compose-spec/compose-spec/blob/master/spec.md


# Docker Compose Commands

The docker-compose command permits the management of multi-container applications. The command has the format:

```shell
$ docker-compose [options] [command] [arguments]
```
To list all the sub-commands including a short description of each command, use -h option for help.
```shell
$ docker-compose -h
```
## Docker compose file
The following docker compose file is used to practice the examples of docker compose commands.
```yml
# docker-compose.yml
version: "3.8"

services:
  adminer:
    image: adminer
    restart: always
    ports: 
      - "8080:8080"
    depends_on:
      - db

  db:
    image: postgres
    restart: always
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_USER=root
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=mydb
```

## Docker compose file location
The docker-compose command looks for the docker-compose.yml file in the current directory. If the the file has a different name or located in another folder, you may use the -f option followed by the compose file path.

```shell
$ docker-compose -f /linux/app/docker-compose.yml
```

## docker-compose ps
Lists containers and services including their names, commands executed at startup, states and ports.

```shell
$ docker-compose ps
```

Options:  
-q : Limit the display to container ids  
-a : Show all stopped containers

## docker-compose up
Builds, (re)creates, starts, and attaches to containers for a service. To start the containers in the background, use the  -d option.

```shell
$ docker-compose up -d
```

This command is also used to take into consideration changes to the compose file by stopping and starting the containers.

To scale the number of services, use the --scale option. The scale option accepts the service name and the number of services to start.
```shell
$ docker-compose up --scale db=2 -d
$ docker-compose ps
```

## docker-compose down
Stops and remove containers and networks defined in the compose file.

```shell
$ docker-compose down
```

Options:  
-v : remove named volumes defined under volumes section in the compose file  
--rmi all : remove all images used by the services  

## docker-compose build
Build services from Docker files. The name given to services are in the form: project-name_service-name. By default, the project name is the directory where the compose file is located. If no build option is specified in the compose file, no action is performed.

```shell
$ docker-compose build
```

## docker-compose config
Validates and checks for errors in the compose file. If there are no errors, the compose file is displayed to the screen.

```shell
$ docker-compose config
``` 

Options:  
--services : print services  
--volumes : print volumes

## docker-compose exec
Executes commands inside services. This command is equivalent to the `docker run` command. 

```shell
$ docker-compose exec <service> <command>
$ docker-compose exec db uname -a
$ docker-compose exec db sh     # start interactive shell
```

## docker-compose logs
Displays logs generated by services.
```shell
$ docker-compose logs [options] [service ...]
$ docker-compose logs
$ docker-compose logs -f db
```
Options:  
-f : follow log output (wait for logs)  
--tail=N or all : show the last N logs or all logs  

## docker-compose stop and start
Stops and starts a container. The stop does not remove the container. When stopped, the container is in the Exit(0) state. 
```shell
$ docker-compose stop adminer
$ docker-compose ps
$ docker-compose start adminer
$ docker-compose ps
```

## docker-compose top
Displays the processes running on services.
```shell
$ docker-compose top
$ docker-compose top adminer
```