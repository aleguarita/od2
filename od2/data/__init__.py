from dataclasses import dataclass

from .atributos import ATRIBUTOS, ATRIBUTOS_EXTENSO, ATRIBUTOS_MOD
from .dados_api import classes, racas


@dataclass
class DATA:
    ATRIBUTOS = ATRIBUTOS
    ATRIBUTOS_EXTENSO = ATRIBUTOS_EXTENSO
    ATRIBUTOS_MOD = ATRIBUTOS_MOD

    CLASSES = classes
    RACAS = racas