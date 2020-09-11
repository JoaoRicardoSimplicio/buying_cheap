FROM postgres:10.1-alpine

ENV POSTGRES_USER postgres

COPY init.sql /docker-entrypoint-initdb.d/

