#!/bin/sh
docker container stop elk-webserver
docker container rm elk-webserver
docker images rm elk-webserver:v1
docker build -t elk-webserver:v1 .
docker run -d -p 8080:80 \
-v "./nginx.conf:/etc/nginx/nginx.conf" \
-v "./htpasswd.elastic.users:/etc/nginx/htpasswd.elastic.users" \
-v "vol-certs:/etc/nginx/certs" \
--network mynets \
--name elk-webserver \
elk-webserver:v1