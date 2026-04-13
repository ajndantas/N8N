# Use uma imagem leve
FROM docker.n8n.io/n8nio/n8n:latest

WORKDIR /home/node/.n8n
COPY . .

# INSTALANDO APK
USER root
RUN wget https://gitlab.alpinelinux.org/api/v4/projects/5/packages/generic//v2.12.14/x86_64/apk.static 
RUN chmod +x apk.static
RUN ./apk.static -X http://dl-cdn.alpinelinux.org/alpine/latest-stable/main -U --allow-untrusted --initdb add apk-tools-static
RUN ./apk.static update
RUN ./apk.static -X http://dl-cdn.alpinelinux.org/alpine/latest-stable/main -U --allow-untrusted add apk-tools
RUN apk update
RUN apk upgrade

# INSTALANDO SQLITE
RUN apk add --no-cache vim sqlite bash

# OUTROS ITENS
RUN ln -sf /usr/bin/vim /usr/bin/vi


USER node
