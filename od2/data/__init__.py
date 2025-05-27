from dataclasses import dataclass

from .atributos import ATRIBUTOS, ATRIBUTOS_EXTENSO, ATRIBUTOS_MOD
from .modificadores import MOD_TESTES
from .dados_api import classes, equipamentos, livros, magias, monstros, racas
from .filtros import buscar, filtrar, filtrar_alcance, filtrar_por_exclusao, filtrar_livro_basico


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


    def buscar(propriedade: str, termo_busca: str, chave: str = 'name'):
        """Filtra a fonte de dados para o termo escolhido com relação à chave escolhida ('name') por padrão

        Args:
            porpriedade (str): qual a propriedade dos dados que deve ser filtrada
            termo_busca (str): qual o termo a ser buscado
            chave (str, optional): qual a chave que se deseja buscar. Defaults to 'name'.

        Returns:
            generator: um gerador com o resultado
        """
        lista = getattr(DATA, propriedade.upper())
        return buscar(lista, termo_busca, chave)
    
    def filtrar(propriedade: str, termo_busca: str, chave: str = 'name'):
        """Filtra a fonte de dados para o termo escolhido com relação à chave escolhida ('name') por padrão

            Args:
                propriedade (str): qual a propriedade da lista que se deseja filtrar
                termo_busca (str): qual o termo a ser buscado
                chave (str, optional): qual a chave que se deseja buscar. Defaults to 'name'.

            Returns:
                generator: um gerador com o resultado
        """
        lista = getattr(DATA, propriedade.upper())
        return filtrar(lista, termo_busca, chave)

    def filtrar_alcance(
        propriedade: str,
        chave: str,
        maior_que: int | float = float('-inf'),
        menor_que: int | float = float('inf'),
    ):
        """Filtra por alcance de valores, por exemplo: monstros com XP entre 100 e 300

        Args:
            propriedade (str): A propriedade dos dados a ser buscada
            chave (str): A chave para a consulta ('xp' no exemplo acima)
            maior_que (int | float, optional): O valor que a busca deve ser maior ou igual (100 no exemplo). Defaults to float('-inf').
            menor_que (int | float, optional): O valor que a busca deve ser menor ou igual (300 no exemplo). Defaults to float('inf').

        Returns:
            generator: um gerador com o resultado
        """
        lista = getattr(DATA, propriedade.upper())
        return filtrar_alcance(lista, chave, maior_que, menor_que)

    def filtrar_por_exclusao(propriedade: str, termo_excluir: str, chave: str = 'name'):
        """Filtra por itens que não coincidam com o termo

        Args:
            propriedade (str): A propriedade dos dados a ser buscada
            termo_excluir (str): O termo que não deve estar na lista
            chave (str, optional): Qual a chave a ser buscada na lista. Defaults to 'name'.

        Returns:
            generator: O gerador com o resultado
        """
        lista = getattr(DATA, propriedade.upper())
        return filtrar_por_exclusao(lista, termo_excluir, chave)

    def filtrar_livro_basico(propriedade: str):
        """Filtra por somente itens que existam nos três livros básicos

        Args:
            propriedade (str): qual a propriedade no banco de dados que deve ser filtrada

        Returns:
            generator: O gerador como resultado
        """
        lista = getattr(DATA, propriedade.upper())
        return filtrar_livro_basico(lista)
