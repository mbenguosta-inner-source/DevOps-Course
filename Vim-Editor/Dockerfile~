// my dockerfile
FROM node:10-alpine

RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app

WORKDIR /home/node/app

COPY package*.json ./
// User in this test
USER node
// install  test packages
RUN npm install

COPY --chown=node:node . .
//expose this test app to 8080
EXPOSE 8080

CMD [ "node", "app.js" ]
