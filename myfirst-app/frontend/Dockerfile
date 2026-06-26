FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install cors
RUN npm install

COPY . .

EXPOSE 3000

CMD ["node", "server.js"]