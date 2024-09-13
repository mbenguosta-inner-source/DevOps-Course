# Docker Essentials
[Dockerhub documentation ](https://hub.docker.com/) <br>
[Docker documentation ](https://docs.docker.com/reference/cli/docker/container/)

## Initialize and Run docker locally
```sh
docker init
docker start
docker stop
```
1- Interactive container creation
```sh
docker pull postgres
docker run postgres
docker run postgres:16.4
```
note: -d :  detached mode <br>
2- List docker images
```sh
docker images list
```

3- List running docker container
```sh
docker ps
docker ps -a
```
4- Open Port 
```sh
docker run -d -p27017:27017  mongo
```
5-assign name to containers
```sh
docker run -d -p27017:27017  --name database mongo
```
Note: <br>
image is the  package ( application and its dependencies)<br>
Container: Image running loccaly as a separate virtual environment<br>

## Build your own image and package your application

To do so, you need a ``` Dockerfile``` file. Its content is like bellow

```yaml

FROM node:18.16.0-alpine3.17
RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY src/package.json src/package-lock.json .
RUN npm install
COPY src/ .
EXPOSE 3000
CMD [ "node", "index.js"]

```
Build and tag your image

```sh
docker build -t [YOUR TAG] [DOCKERFILE PATH]

#When you run the command in the same directory that Dockerfile is located
docker build -t my-app-image .

#Dockerfile in another directory like /home/user/files
docker build -t my-app-image /home/user/files
```
Note: ``` Dockerfile ``` is the default name of your docker image configurations file.<br>
If you wanna ignore some files/folder when buildong your docker file, list them to a ``` .dockerignore ``` file<br>

Example
```sh
node_modules
file1
file2
...
```

## Docker debugging (for log viewing for example)

View container logs 
```sh
docker logs [CONTAINER ID]
docker logs [CONTAINER NAME]
```
Connect to container
```sh
docker exec -it [CONTAINER ID] /bin/bash
docker exec -it [CONTAINER NAME] /bin/bash
```

Update app.py
```sh
#format
sed -i 's/[Old_string]/[New_string]/' [FileName]
sed 's/Welcome to this fantastic app/Welcome to app Ibrahima/' app.py
```

## Commit container changes
```sh
docker commit [CONTAINER ID] [NEW CONTAINER TAG]

#Or send changes when committing
docker commit --change "ENV DEBUG=true" [CONTAINER ID] [NEW CONTAINER TAG]

```
## Docker network

It isolates docker containers and enable container communication using container name.<br>

list default docker network<br>
```sh
docker network ls
```
Create network
```sh
docker network create my-network
```
Specify network when creating docker container
```sh
docker run -d -p27017:27017  --name database --network my-network mongo
```
## Docker Volumes

Create docker volume
```sh
docker volume create my-volume
```

With mountpoint
```sh
docker volume create \
    --opt type=none \
    --opt o=bind \
    --opt device=/path/on/host \
    my_volume
  ```

List docker volume
```sh
docker volume ls
```

Inspect volume
```sh
docker volume inspect my_volume
```

Mount volume (case mongo DB)
```sh
docker run -d \
  --name=mongo \
  -p 27017:27017 \
  -v my-volume:/data/db \
  mongo

#Or
docker run -d \
  --name=mongo \
  -p 27017:27017 \
  -v /home/<user>/data:/data/db \
  mongo

#Or

docker run -d \
  --name=mongo \
  --mount source=/home/<user>/data,destination=/data/db \
  mongo
```
Note: /home/user/data is just an example. You can choose another folder to store data<br>


## Share Container images
Note: To do this, you need to create a container repository in a container registry like docker hub.<br>
1- Create a registry account in dockerhub<br>
2-Note your accound ID. It'll be used to tag your images<br>
3-tag your images with your ID as prefix<br>
```sh
#Format
docker build -t [YOUR ID]/[IMAGE NAME]:[IMAGE VERSION]

#Example

docker build -t mbenguosta/backend:v2.0.0
```
4- Push it to the online repository

```sh
#Log in to the repo
docker login

#Publish your image
docker push [YOUR ID]/[IMAGE NAME]:[IMAGE VERSION]
```


Recommendation:  <br> <br>
1- Use alpine version of base image for less image and more security <br> <br>
2- Copy dependencies file and install then before copying the code to the container image. <br> <br>
3-adopt tag format [YOUR ID]/[IMAGE NAME]:V$.$.$ where $ is a digit  <br> <br>



