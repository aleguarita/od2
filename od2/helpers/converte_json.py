import json
from pathlib import Path

def converte_json(nome_arquivo: str):
    prefixo = 'od2_api_'
    arquivo = Path(f'RPG/sistemas/od2/data/{prefixo}{nome_arquivo}.json').resolve()
    if arquivo.exists():
        with open(arquivo) as arquivo:
            return json.loads(arquivo.read())
    else:
        return f'arquivo {prefixo}{nome_arquivo} não encontrado'
