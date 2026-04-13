from fastapi import FastAPI
import subprocess


# Este script é um aplicativo FastAPI que expõe um endpoint POST em "/urls".

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