FROM node:17

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 4000

CMD [ "npm" , "start" ]
# CMD ["node", "--no-warnings", "node_modules/react-scripts/scripts/start.js"]
