from fastapi import FastAPI
from pydantic import BaseModel
import subprocess


# Este script é um aplicativo FastAPI que expõe um endpoint POST em "/urls".
#
# Como chamar a API ? 
# Você pode usar uma ferramenta como curl ou Postman para enviar uma solicitação POST para o endpoint "/urls" com um corpo de dados contendo o array de URLs.
# 
# Exemplo usando curl:
# curl -X POST "https://antoniodantasn8n.ddns.net/urls" -H "Content-Type: application/json" -d "{\"urls\": [\"http://example.com\", \"http://example.org\"]}"

app = FastAPI()

class Input(BaseModel):
    data: str

@app.post("/urls")
def run_script(input: Input):
    result = subprocess.run(
        ["python", "urls.py", input],
        capture_output=True,
        text=True # Adiciona esta linha para capturar a saída como texto em vez de bytes
    )
    
    return {
        "stdout": result.stdout,
        "stderr": result.stderr
    }