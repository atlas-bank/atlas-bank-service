# atlas-bank-service

# Como rodar o serviço

    pip install -r requirements.txt 
    
    $env:PYTHONPATH="src"
    
    uvicorn src.main:app --reload

Importante estar com o `venv` ativo

File> Setting> Python> Interpreter: selecionar o interpreter

após isso, o serviço vai estar rodando localmente na porta 8000
