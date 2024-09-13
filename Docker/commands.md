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
docker run -d -p8200:8000 --name mouhagueye01 \
--network my-net \
-e DATABASE_HOST=database \
-e DATABASE_PORT=27017 \
-e DATABASE_USER=user \
-e DATABASE_PASSWORD=passer  \
mouhagueye01/backend:v2.0.0
```

```sh
docker volume create my-volume
docker volume inspect my-volume
```

```sh
docker run -d  -p 27017:27017 --name database \
  --network my-net \
  -v my-volume:/data/db \
  -e MONGO_INITDB_ROOT_USERNAME=user \
  -e MONGO_INITDB_ROOT_PASSWORD=passer \
  mongo
```
Update & commit image from running container
connect to backend Container
```sh
docker exec -it backend /bin/bash
```

```sh
sed -i 's/Welcome to this fantastic app/Welcome to app Ibrahima/' app.py
```
exit container & commit new image

```sh
docker commit backend [DOCKERHUB ID]/backend:v2.0.0
```