from dataclasses import dataclass

from .atributos import ATRIBUTOS, ATRIBUTOS_EXTENSO, ATRIBUTOS_MOD
from .modificadores import MOD_TESTES
from .dados_api import classes, racas, equipamentos, monstros


@dataclass
class DATA:
    ATRIBUTOS = ATRIBUTOS
    ATRIBUTOS_EXTENSO = ATRIBUTOS_EXTENSO
    ATRIBUTOS_MOD = ATRIBUTOS_MOD
    TESTES_MOD = MOD_TESTES

    CLASSES = classes
    RACAS = racas
    EQUIPAMENTOS = equipamentos
    MONSTROS = monstros