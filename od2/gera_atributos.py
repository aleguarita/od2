from typing import Literal
from collections import namedtuple
from RPG.dado import Dado

from .data import DATA


LISTA_ATRIBUTOS = Literal['FOR', 'DES', 'CON', 'INT', 'SAB', 'CAR']

ESTILOS = Literal[
    'clássico',
    'aventureiro',
    'heroico',
    # 'duplo',
    # 'camponês',
    # 'distribuição',
    # 'racial'
]

Atributos = namedtuple('Atributos', ('FOR', 'DES', 'CON', 'INT', 'SAB', 'CAR'))

def rolar_atributos(estilo: ESTILOS = 'clássico'):
    return RolarAtributos(estilo)


class RolarAtributos:
    def __init__(self, estilo: ESTILOS):
        self._estilo = estilo

        self.__iniciar_escolhidos__()
        self.rolar()
        self.rolamento_original = tuple(self.rolamento)

    def __repr__(self) -> str:
        return f'{self.atributos}'
    

    # ? Métodos privados
    def __iniciar_escolhidos__(self):
        self._ordem_escolhidos = [None for _ in range(6)]

    def __rolamento_classico_aventureiro__(self):
        if self._estilo == 'clássico' or 'aventureiro':
            self.rolamento = [Dado(3, 6) for _ in range(6)]
            self._rolamento_totais = [rolamento.total for rolamento in self.rolamento]

    def __rolamento_heroico__(self):
        if self._estilo == 'heroico':
            self.rolamento = [Dado(4, 6) for _ in range(6)]

            retira_menor = list(self.rolamento)
            for dado in retira_menor:
                dado.retirar_menor()

            self._rolamento_totais = [rolamento.total for rolamento in retira_menor]

    def __resultado_na_ordem__(self):
        if self._estilo == 'clássico' or 'duplo':
            self._ordem_escolhidos = [atr for atr in DATA.ATRIBUTOS]

    def __resultado_fora_ordem__(self):
        pass

    def __resultado_final__(self):
        if None not in self._ordem_escolhidos:
            final = []
            for i in DATA.ATRIBUTOS:
                indice = self._ordem_escolhidos.index(i)
                final.append(self._rolamento_totais[indice])
            
            self.atributos = Atributos(*final)
                

        else:
            pass


    # ! Métodos públicos
    def rolar(self):
        self.__iniciar_escolhidos__()
        self.__rolamento_classico_aventureiro__()
        self.__rolamento_heroico__()
        self.__resultado_na_ordem__()
        self.__resultado_fora_ordem__()
        self.__resultado_final__()


        