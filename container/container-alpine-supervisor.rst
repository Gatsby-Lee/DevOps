Install supervior on alpine container
=====================================

ref: https://docs.docker.com/config/containers/multi-service_container/

..code-block:: ini

  FROM python:3.6-alpine
  RUN apk add --update supervisor && rm  -rf /tmp/* /var/cache/apk/*
  CMD ["/usr/bin/supervisord", "--nodaemon", "--configuration", "/etc/supervisord.conf"]
  
