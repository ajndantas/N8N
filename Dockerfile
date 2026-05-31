# Use uma imagem Python oficial e leve como base
FROM n8nio/n8n:latest

# Define o usuário root temporariamente para garantir que as pastas tenham a permissão correta
USER root

# Cria o diretório e garante que o usuário 'node' seja o dono dele
RUN mkdir -p /home/node/.n8n && chown -R node:node /home/node/.n8n

# Volta para o usuário padrão do n8n (segurança)
USER node

# Define a porta padrão que o Cloud Run vai injetar (o n8n lê a variável PORT nativamente)
ENV PORT=5678

# Comando para iniciar o n8n corretamente
CMD ["n8n", "start"]