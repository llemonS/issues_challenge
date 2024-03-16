FROM node:13.12.0-alpine
WORKDIR /frontend
ADD . /frontend
COPY package.json package-lock.json /frontend
RUN npm install 
RUN npm install react-scripts@3.4.1 -g 
EXPOSE 3000
VOLUME /frontend