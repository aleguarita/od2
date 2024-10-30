import json
import pathlib

from ..CONFIG import PREFIXO, URL_ESPECIFICAS


def converte_json(nome_arquivo: str):
    arquivo = pathlib.Path(f'od2/{PREFIXO}{URL_ESPECIFICAS[nome_arquivo]}').resolve()
    
    if arquivo.exists():
        with open(arquivo) as arquivo:
            return json.loads(arquivo.read())
    else:
        return f'arquivo *{PREFIXO}{URL_ESPECIFICAS[nome_arquivo]}* não encontrado'

classes = converte_json('classes')
racas = converte_json('raças')
equipamentos = converte_json('equipamentos')

