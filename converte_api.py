from pathlib import Path
import webbrowser
import json
import pprint

def abrir_api():
    """Abra a API num navegador para baixar o JSON
    """
    print('No navegador, autorize a aplicação')
    print('Tenha paciência, que demora mesmo')
    print('Baixe os arquivos e coloque na pasta src/od2/data/api')
    webbrowser.open_new_tab('https://od2-aleguarita.glitch.me/')


def converter_para_py():
    caminho_api = Path('src/od2/data/api').resolve()

    for arquivo_json in caminho_api.glob('*.json'):
        print(f'Processando: {arquivo_json.name}...')
        nome_da_variavel = arquivo_json.stem
        caminho_py = arquivo_json.with_suffix('.py')

        try:
            with open(arquivo_json, 'r', encoding='utf-8') as f_json:
                dados_dict = json.load(f_json)

            with open(caminho_py, 'w', encoding='utf-8') as f_py:
                f_py.write(f'#? Arquivo gerado a partir de {arquivo_json.name}\n\n')
                conteudo_formatado = pprint.pformat(dados_dict)
                f_py.write(f'{nome_da_variavel} = {conteudo_formatado}\n')

            print(f' -> Criando/Atualizando: {caminho_py.name} (com variável "{nome_da_variavel}")')

        except json.JSONDecodeError:
            print(f' -> ERRO: O arquivo {arquivo_json.name} não contém JSON válido e foi ignorado')
        except Exception as e:
            print(f" -> ERRO: Ocorreu um problema ao processar {arquivo_json.name}: {e}")


def rodar():
    separador = '-'.ljust(80, '-')

    texto = separador
    texto += '\nATUALIZAR API\n'
    texto += separador
    texto += '\nAtualiza a API, levando para o site para baixar os JSON\n'
    texto += 'e convertendo para python. Escolha uma das opções\n'
    texto += separador
    texto += '\n1. Abrir navegado para baixar os .json'
    texto += '\n2. Converter os .json para .py'
    texto += '\n3. Sair\n'
    texto += '> '

    while True:
        opcao = int(input(texto))
        
        match opcao:
            case 1:
                abrir_api()
            case 2:
                converter_para_py()
            case 3:
                print('Encerrando')
                break
            case _:
                print('Valor inválido')


if __name__ == '__main__':
    rodar()
