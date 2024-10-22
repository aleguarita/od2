import requests
import json

url_base = 'https://olddragon.com.br/'
url_especificas = {
    'classes': 'classes.json',
    'monstros': 'monstros.json',
    'equipamentos': 'equipamentos.json',
    'livros': 'livros.json',
    'magias': 'magias.json',
    'monstros': 'monstros.json',
    'raças': 'racas.json'
}
prefixo = 'od2_api_'

def pega_todos_dados(info_base: str):
    url = url_base + url_especificas[info_base]
    atual = 1
    tem_proximo = True
    dados_total = []

    while tem_proximo:
        resposta = requests.get(url, params={'page': atual})
        data = resposta.json()
        header = resposta.headers.get('Link')

        dados_total.extend(data)

        if header and 'rel="next"' in header:
            atual += 1
        else:
            tem_proximo = False

    dados_total = [dado for dado in dados_total if 'access' not in dado.keys() or dado['access'] != "limited"]

    return dados_total


def gera_arquivo(arquivo_base: str):
    with open(f'../data/{prefixo}{url_especificas[arquivo_base]}', 'w+') as arquivo:
        info = pega_todos_dados(arquivo_base)
        arquivo.write(json.dumps(info, indent=2))



if __name__ == '__main__':
    print('Gerando os arquivos, aguarde')
    print('-'.ljust(30, '-'))

    for chave in url_especificas.keys():
        print(f'Gerando {prefixo}{url_especificas[chave]}')
        gera_arquivo(chave)
        print(f'{url_especificas[chave]} finalizado')

    print('-'.ljust(30, '-'))
    print('Arquivos gerados')