# Employee backend api 
  
  This api is build with fastapi framework
  It's a small entreprise api that host employees informations in a mongo database
  
  Run locally
  ## Docker
  ```
  docker network create aka-net
  ```
  ```
  docker run -d  -p 27017:27017 --name database \
	--net aka-net \
	-e MONGO_INITDB_ROOT_USERNAME=[YOUR DB USER]  \
	-e MONGO_INITDB_ROOT_PASSWORD=[YOUR DB PWD] \
	mongo
  
  ```
  
  ```
 docker run -d -p8000:8000 --name backend \
--net aka-net \
-e DATABASE_HOST=database \
-e DATABASE_PORT=27017 \
-e DATABASE_USER=[YOUR DB USER] \
-e DATABASE_PASSWORD=[YOUR DB PWD]  \
mbenguosta/aka_back:v1.0.0

  ```

## Docker compose
Before running the command you've to create the volume directory that persist tha database data.
In this configuration it will be located in the root folder of the project

NOTE: You can change this directory name and location but you've to update the docker-compose backend's volumes in the file
```
docker-compose up
```
