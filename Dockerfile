FROM python:3.11-slim

# O CONTAINER JÁ INICIA NESSE DIRETÓRIO. NÃO PRECISA PASSAR ELE QUANDO FOR EXECUTAR O SCRIPT
WORKDIR /app 

RUN pip install --no-cache-dir fastapi uvicorn

COPY ./Scripts/urls.py .

CMD ["uvicorn", "urls:app", "--host", "0.0.0.0", "--port", "8000"]