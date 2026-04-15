FROM python:3.11-slim

# Defina variáveis de ambiente para evitar prompts interativos durante a instalação e para garantir que a saída do Python seja exibida imediatamente no console
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# O CONTAINER JÁ INICIA NESSE DIRETÓRIO. NÃO PRECISA PASSAR ELE QUANDO FOR EXECUTAR O SCRIPT
WORKDIR /app 

RUN pip install --no-cache-dir fastapi uvicorn dotenv

# Ele está iniciando o servidor Uvicorn para rodar a aplicação FastAPI definida em app.py, 
# ouvindo em todas as interfaces de rede
CMD uvicorn "postagem_linkedin.Scripts.app:app" --host "0.0.0.0" --port "8000"

