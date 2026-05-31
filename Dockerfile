# Use uma imagem Python oficial e leve como base
FROM docker.n8n.io/n8nio/n8n:latest

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /home/node/.n8n

ARG PORT

EXPOSE ${PORT}