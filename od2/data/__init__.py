from dataclasses import dataclass

from .atributos import ATRIBUTOS, ATRIBUTOS_EXTENSO, ATRIBUTOS_MOD
from .modificadores import MOD_TESTES
from .dados_api import classes, equipamentos, livros, magias, monstros, racas


@dataclass
class DATA:
    ATRIBUTOS = ATRIBUTOS
    ATRIBUTOS_EXTENSO = ATRIBUTOS_EXTENSO
    ATRIBUTOS_MOD = ATRIBUTOS_MOD
    TESTES_MOD = MOD_TESTES

    CLASSES = classes
    EQUIPAMENTOS = equipamentos
    LIVROS = livros
    MAGIAS = magias
    MONSTROS = monstros
    RACAS = racas

    def buscar(
            lista: list,
            termo_busca: str,
            chave: str = 'name'
        ) -> dict:
        """Realiza uma busca por um termo exato

        Args:
            lista (list): qual a lista que se deseja buscar
            termo_busca (str): qual o termo a ser buscado
            chave (str, optional): qual a chave que se deseja buscar. Defaults to 'name'.

        Returns:
            dict: o dicionário do item buscado na lista
        """
        buscar = lambda x: x.get(chave).lower() == termo_busca.lower()
        resultado = filter(buscar, lista)

        return list(resultado)[0]
    
    def filtrar(
            lista: list,
            termo_busca: str,
            chave: str = 'name'
    ) -> list:
        """Filtra a lista para o termo escolhido com relação à chave escolhida ('name') por padrão

        Args:
            lista (list): qual a lista que se deseja filtrar
            termo_busca (str): qual o termo a ser buscado
            chave (str, optional): qual a chave que se deseja buscar. Defaults to 'name'.

        Returns:
            list: o resultado do filtra, como lista
        """
        filtrar = lambda x: termo_busca.lower() in x.get(chave).lower()
        resultado = filter(filtrar, lista)

        return list(resultado)

    def filtrar_alcance(
            lista: list,
            chave: str,
            maior_que: int | float = float('-inf'),
            menor_que: int | float = float('inf'),
        ):
        pre_filtro = lambda x: isinstance(x.get(chave), (int, float)) or (isinstance(x.get(chave), str) and x.get(chave).isdigit())
        filtrar = lambda x: maior_que <= float(x.get(chave)) <= menor_que
        resultado = filter(filtrar, filter(pre_filtro, lista))

        return list(resultado)

    def filtrar_por_exclusao(
        lista: list,
        termo_excluir: str,
        chave: str = 'name'
    ):
        filtrar = lambda x: termo_excluir.lower() not in x.get(chave).lower()
        resultado = filter(filtrar, lista)

        return list(resultado)
        