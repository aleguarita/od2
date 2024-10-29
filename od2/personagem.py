

from .gera_atributos import Atributos
from .helpers import Atributo
from .raca import buscar_raca, Raca

class Personagem:
    def __init__(self,
                 nome: str,
                 atributos: tuple | Atributos,
                 raca: dict | str,
                 ):
        
        self._atributos = atributos if type(atributos) is Atributos else Atributos(*atributos)
        self._raca = raca

        self.nome = nome

        self._ajustar_raca()


    #! Propriedades
    @property
    def FOR(self):
        return Atributo(self._atributos.FOR)

    @property
    def DES(self):
        return Atributo(self._atributos.DES)

    @property
    def CON(self):
        return Atributo(self._atributos.CON)

    @property
    def INT(self):
        return Atributo(self._atributos.INT)

    @property
    def SAB(self):
        return Atributo(self._atributos.SAB)

    @property
    def CAR(self):
        return Atributo(self._atributos.CAR)
    
    
    @property
    def raca(self):
        return self._raca
    
    @property
    def movimento(self):
        return self.raca.movimento


    #! Métodos inicializadores ou privados
    def _ajustar_raca(self):
        if type(self._raca) is str:
            self._raca = buscar_raca(self._raca)

        self._raca = Raca(self._raca)
