FROM node:20

WORKDIR /flask-app
COPY package*.json ./
RUN npm install
# Copy the rest of the app code
COPY . .

CMD [ "npm", "run", "build" ]