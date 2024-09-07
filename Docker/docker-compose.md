# Container Orchestration
[Docker compose docs](https://docs.docker.com/compose/)

### Run compose
```sh
docker-compose up 
```
Note: Use ``` -d``` to run containers in detached mode

### List running containers

```sh
docker-compose ps 
```

### Stop running containers

```sh
docker-compose kill 
```

### Delete containers

```sh
docker-compose rm 
```

### Stop and remove containers, images and volumes created previously by compose

```sh
docker-compose down 
```