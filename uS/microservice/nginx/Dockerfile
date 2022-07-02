FROM nginx:alpine
 
RUN apk update && apk add bash

COPY ./nginx.conf /etc/nginx/nginx.conf
# COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./backend-not-found.html /var/www/html/backend-not-found.html
