from fastapi import FastAPI
import subprocess


# Este script é um aplicativo FastAPI que expõe um endpoint POST em "/urls".
#
# Como chamar a API ? 
# Você pode usar uma ferramenta como curl ou Postman para enviar uma solicitação POST para o endpoint "/urls" com um corpo de dados contendo o array de URLs.
# 
# Exemplo usando curl:
# curl -X POST "http://localhost:8000/urls" -H "Content-Type: application/json" -d "{\"urls\": [\"http://example.com\", \"http://example.org\"]}"

app = FastAPI()

@app.post("/urls")
def run_script(data: str):
    result = subprocess.run(
        ["python", "urls.py", data],
        capture_output=True,
        text=True # Adiciona esta linha para capturar a saída como texto em vez de bytes
    )
    
    return {
        "stdout": result.stdout,
        "stderr": result.stderr
    }