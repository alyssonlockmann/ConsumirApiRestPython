FROM mongo

ENV MONGO_INITDB_ROOT_USERNAME mongoadmin
ENV MONGO_INITDB_ROOT_PASSWORD adminpass

ADD mongo-init.js /docker-entrypoint-initdb.d/

EXPOSE 27017