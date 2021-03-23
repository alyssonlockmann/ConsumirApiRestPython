FROM mongo

ENV MONGO_INITDB_ROOT_USERNAME mongoadmin
ENV MONGO_INITDB_ROOT_PASSWORD adminpass

COPY mongo-init.js /docker-entrypoint-initdb.d/

EXPOSE 27017