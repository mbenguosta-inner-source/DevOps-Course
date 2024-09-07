# Lab execution commands
### move to backend folder and complete the following steps

```sh
docker build -t my-app .
```

```sh
docker network create my-net
```

```sh
docker run -d  -p 27017:27017 --name database \
  --network my-net \
  -v my-volume:/data/db \
  -e MONGO_INITDB_ROOT_USERNAME=user \
  -e MONGO_INITDB_ROOT_PASSWORD=passer \
  mongo
```

```sh
docker run -d -p8000:8000 --name gr77 \
--network my-net \
-e DATABASE_HOST=database \
-e DATABASE_PORT=27017 \
-e DATABASE_USER=user \
-e DATABASE_PASSWORD=passer  \
gr77/backend:v1.0.0
```