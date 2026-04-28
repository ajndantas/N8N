import json
from os import getenv
from dotenv import load_dotenv
from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import List
from fastapi import Header, HTTPException, Depends

# Este script é um aplicativo FastAPI que expõe um endpoint POST em "/urls".
#
# Como chamar a API ? 
# Você pode usar uma ferramenta como curl ou Postman para enviar uma solicitação POST para o endpoint "/urls" com um corpo de dados contendo o array de URLs.
# 
# Exemplo usando curl:
# curl -X POST "https://sua-api/urls"  -H "Content-Type: application/json" -H "x-api-key: minha_chave_super_secreta" -d '{"data": [{"url":"http://example.com"}, {"url":"http://example.org"}]}'

app = FastAPI()

load_dotenv() # Carrega as variáveis de ambiente do arquivo .env

#class Input(BaseModel):
#    data: List[dict] 


# AUTENTICAÇÃO SIMPLES COM API KEY
def verify_api_key(x_api_key: str = Header(...)):
    
    if x_api_key != getenv("API_KEY"):
        raise HTTPException(status_code=401, detail="Unauthorized")
    

@app.post("/urls")
def run_script(input: str, api_key: str = Depends(verify_api_key)):

    
    #json_data = json.dumps(input.data)
    json_data = input

    result = subprocess.run(
        ["python", "postagem_linkedin/Scripts/urls.py", json_data], # O script "urls.py" deve estar no mesmo diretório que este arquivo "app.py"
        
        capture_output=True,
        text=True # Adiciona esta linha para capturar a saída como texto em vez de bytes
    )

        
    return {
        "stdout": result.stdout,
        "stderr": result.stderr
    }