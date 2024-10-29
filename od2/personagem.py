from typing import Literal

from .gera_atributos import Atributos
from .helpers import Atributo, AtributoBase
from .raca import buscar_raca, Raca
from .classe import buscar_classe, Classe


ALINHAMENTOS = Literal[
    'ordeiro',
    'neutro',
    'caótico'
]


class Personagem:
    def __init__(self,
                 nome: str,
                 atributos: tuple | Atributos,
                 raca: dict | str,
                 classe: dict | str,
                 alinhamento: ALINHAMENTOS,
                 xp: int = 0,
                 ):
        
        self._atributos = atributos if type(atributos) is Atributos else Atributos(*atributos)
        self._raca = raca
        self._classe = classe
        self._xp = xp

        self.nome = nome
        self.alinhamento = alinhamento.capitalize()

        self._ajustar_raca()
        self._ajustar_classe()


    def __repr__(self) -> str:
        return f"Personagem(classe='{self.classe.data['name']}', raça='{self.raca.data['name']}', alinhamento='{self.alinhamento}', nivel={self.nivel})"

    def __str__(self):
        return f'{self.nome}: {self.classe.data['name']} {self.raca.data['name']} {self.alinhamento}, nível {self.nivel}'


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
    def classe(self):
        return self._classe
    
    @property
    def xp(self):
        return self._xp
    
    @property
    def nivel(self):
        xps = self.classe.xp

        xp_proximo_nivel = next((i for i in xps if i > self.xp), None)
        nivel = xps.index(xp_proximo_nivel) if xp_proximo_nivel else 15

        return nivel
    

    @property
    def JP(self):
        return self.classe.jp[self.nivel]

    @property
    def JPC(self):
        return AtributoBase(self.JP + self.CON.modificador)

    @property
    def JPD(self):
        return AtributoBase(self.JP + self.DES.modificador)

    @property
    def JPS(self):
        return AtributoBase(self.JP + self.SAB.modificador)

    
    @property
    def movimento(self):
        return self.raca.movimento


    #! Métodos inicializadores ou privados
    def _ajustar_raca(self):
        if type(self._raca) is str:
            self._raca = buscar_raca(self._raca)

        self._raca = Raca(self._raca)

    def _ajustar_classe(self):
        if type(self._classe) is str:
            self._classe = buscar_classe(self._classe)

        self._classe = Classe(self._classe)

