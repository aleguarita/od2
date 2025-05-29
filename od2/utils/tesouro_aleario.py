import string
from collections import Counter
from RPG import rolar_dado_notacao

# from ..helpers import x_em_d6


tesouro_aleatorio = [
    # Covil
    Counter({
        'tipo': 'A',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 12000}),
        'po': Counter({'chance': 2, 'rolamento': '2d6 * 1000'}),
        'pp': Counter({'chance': 2, 'rolamento': '1d6 * 1000'}),
        'pc': Counter({'chance': 1, 'rolamento': '1d6 * 1000'}),
        'gemas': Counter({'chance': 3, 'rolamento': '6d6'}),
        'objetos_de_valor': Counter({'chance': 3, 'rolamento': '6d6'}),
        'itens_magicos': Counter({'chance': 2, 'itens': Counter({'qualquer': 3})}),
    }),
    Counter({
        'tipo': 'B',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 1400}),
        'po': Counter({'chance': 1, 'rolamento': '1d3 * 1000'}),
        'pp': Counter({'chance': 1, 'rolamento': '1d6 * 1000'}),
        'pc': Counter({'chance': 3, 'rolamento': '1d8 * 1000'}),
        'gemas': Counter({'chance': 1, 'rolamento': '1d6'}),
        'objetos_de_valor': Counter({'chance': 1, 'rolamento': '1d6'}),
        'itens_magicos': Counter({'chance': 1, 'itens': Counter({'arma': 1})}),
    }),
    Counter({
        'tipo': 'C',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 650}),
        'pp': Counter({'chance': 2, 'rolamento': '1d4 * 1000'}),
        'pc': Counter({'chance': 2, 'rolamento': '1d12 * 1000'}),
        'gemas': Counter({'chance': 1, 'rolamento': '1d4'}),
        'objetos_de_valor': Counter({'chance': 1, 'rolamento': '1d4'}),
        'itens_magicos': Counter({'chance': 1, 'itens': Counter({'qualquer': 2})}),
    }),
    Counter({
        'tipo': 'D',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 3400}),
        'po': Counter({'chance': 3, 'rolamento': '1d6 * 1000'}),
        'pp': Counter({'chance': 1, 'rolamento': '1d12 * 1000'}),
        'pc': Counter({'chance': 1, 'rolamento': '1d8 * 1000'}),
        'gemas': Counter({'chance': 2, 'rolamento': '1d8'}),
        'objetos_de_valor': Counter({'chance': 2, 'rolamento': '1d8'}),
        'itens_magicos': Counter({'chance': 1, 'itens': Counter({'qualquer': 2, 'poção': 1})}),
    }),
    Counter({
        'tipo': 'E',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 1800}),
        'po': Counter({'chance': 1, 'rolamento': '1d8 * 1000'}),
        'pp': Counter({'chance': 2, 'rolamento': '1d12 * 1000'}),
        'pc': Counter({'chance': 1, 'rolamento': '1d10 * 1000'}),
        'gemas': Counter({'chance': 1, 'rolamento': '1d10'}),
        'objetos_de_valor': Counter({'chance': 1, 'rolamento': '1d10'}),
        'itens_magicos': Counter({'chance': 1, 'itens': Counter({'qualquer': 3, 'pergaminho': 1})}),
    }),
    Counter({
        'tipo': 'F',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 4000}),
        'po': Counter({'chance': 2, 'rolamento': '1d12 * 1000'}),
        'pp': Counter({'chance': 1, 'rolamento': '2d10 * 1000'}),
        'gemas': Counter({'chance': 1, 'rolamento': '2d12'}),
        'objetos_de_valor': Counter({'chance': 1, 'rolamento': '1d12'}),
        'itens_magicos': Counter({'chance': 2, 'itens': Counter({'poção': 1, 'pergaminho': 1, 'não arma': 3})}),
    }),
    Counter({
        'tipo': 'G',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 14000}),
        'po': Counter({'chance': 3, 'rolamento': '10d4 * 1000'}),
        'gemas': Counter({'chance': 1, 'rolamento': '3d6'}),
        'objetos_de_valor': Counter({'chance': 1, 'rolamento': '1d10'}),
        'itens_magicos': Counter({'chance': 2, 'itens': Counter({'qualquer': 4, 'pergaminho': 1})}),
    }),
    Counter({
        'tipo': 'H',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 27000}),
        'po': Counter({'chance': 3, 'rolamento': '10d6 * 1000'}),
        'pp': Counter({'chance': 3, 'rolamento': '1d10 * 1000'}),
        'pc': Counter({'chance': 1, 'rolamento': '3d8 * 1000'}),
        'gemas': Counter({'chance': 3, 'rolamento': '1d10'}),
        'objetos_de_valor': Counter({'chance': 3, 'rolamento': '10d4'}),
        'itens_magicos': Counter({'chance': 1, 'itens': Counter({'qualquer': 4, 'poção': 1, 'pergaminho': 1})}),
    }),
    Counter({
        'tipo': 'I',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 2800}),
        'gemas': Counter({'chance': 3, 'rolamento': '2d6'}),
        'objetos_de_valor': Counter({'chance': 3, 'rolamento': '2d6'}),
        'itens_magicos': Counter({'chance': 1, 'itens': Counter({'qualquer': 1})}),
    }),
    Counter({
        'tipo': 'J',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 25}),
        'pp': Counter({'chance': 1, 'rolamento': '1d3 * 1000'}),
        'pc': Counter({'chance': 1, 'rolamento': '1d4 * 1000'}),
    }),
    Counter({
        'tipo': 'K',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 15}),
        'pp': Counter({'chance': 1, 'rolamento': '1d2 * 1000'}),
    }),
    Counter({
        'tipo': 'L',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 200}),
        'gemas': Counter({'chance': 3, 'rolamento': '1d4'}),
    }),
    Counter({
        'tipo': 'M',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 40000}),
        'po': Counter({'chance': 5, 'rolamento': '8d10 * 1000'}),
        'pp': Counter({'chance': 3, 'rolamento': '10d6 * 1000'}),
        'gemas': Counter({'chance': 3, 'rolamento': '5d4'}),
        'objetos_de_valor': Counter({'chance': 2, 'rolamento': '2d6'}),
    }),
    Counter({
        'tipo': 'N',
        'categoria': 'covil',
        'itens_magicos': Counter({'chance': 2, 'itens': Counter({'poção': '2d4'})}),
    }),
    Counter({
        'tipo': 'O',
        'categoria': 'covil',
        'itens_magicos': Counter({'chance': 3, 'itens': Counter({'poção': '1d4'})}),
    }),
    # Individual
    Counter({
        'tipo': 'P',
        'categoria': 'individual',
        'tesouro_rapido': Counter({'pp': 1}),
        'pc': Counter({'chance': 6, 'rolamento': '3d8'}),
    }),
    Counter({
        'tipo': 'Q',
        'categoria': 'individual',
        'tesouro_rapido': Counter({'po': 1}),
        'pp': Counter({'chance': 6, 'rolamento': '3d6'}),
    }),
    Counter({
        'tipo': 'R',
        'categoria': 'individual',
        'tesouro_rapido': Counter({'po': 3}),
        'po': Counter({'chance': 6, 'rolamento': '1d6'}),
        'equipamentos': Counter({'chance': 2, 'rolamento': 1})
    }),
    Counter({
        'tipo': 'S',
        'categoria': 'individual',
        'tesouro_rapido': Counter({'po': 5}),
        'po': Counter({'chance': 6, 'rolamento': '2d4'}),
        'equipamentos': Counter({'chance': 2, 'rolamento': 1})
    }),
    Counter({
        'tipo': 'T',
        'categoria': 'individual',
        'tesouro_rapido': Counter({'po': 17}),
        'po': Counter({'chance': 6, 'rolamento': '1d6 * 5'}),
        'equipamentos': Counter({'chance': 2, 'rolamento': 2})
    }),
    Counter({
        'tipo': 'U',
        'categoria': 'individual',
        'tesouro_rapido': Counter({'po': 90}),
        'po': Counter({'chance': 1, 'rolamento': '1d10'}),
        'pp': Counter({'chance': 1, 'rolamento': '1d10'}),
        'pc': Counter({'chance': 1, 'rolamento': '1d10'}),
        'objetos_de_valor': Counter({'chance': 1, 'rolamento': '1'}),
        'itens_magicos': Counter({'chance': 1, 'itens': Counter({'qualquer': 1})}),
        'equipamentos': Counter({'chance': 1, 'rolamento': '1d4'})
    }),
    Counter({
        'tipo': 'V',
        'categoria': 'individual',
        'tesouro_rapido': Counter({'po': 175}),
        'po': Counter({'chance': 2, 'rolamento': '1d10'}),
        'pp': Counter({'chance': 2, 'rolamento': '1d10'}),
        'objetos_de_valor': Counter({'chance': 1, 'rolamento': '1d4'}),
        'itens_magicos': Counter({'chance': 2, 'itens': Counter({'qualquer': 1})}),
        'equipamentos': Counter({'chance': 1, 'rolamento': '1d6'})
    })
]

# TODO: entender o que bagunçou depois do Counter
class TesouroAleatorio:
    def __init__(self, tipo_tesouro: str):
        self._tipo = self._retornar_tipo(tipo_tesouro)
        # self._rapido = self.tabela.get('tesouro_rapido')

    #? Propriedades
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo_tesouro: str):
        self._tipo = self._retornar_tipo(tipo_tesouro)

    @property
    def tabela(self):
        return [i for i in tesouro_aleatorio if i.get('tipo') == self.tipo]
    
    @property
    def tesouro_rapido(self):
        return self._rapido
    
    @tesouro_rapido.setter
    def tesouro_rapido(self, valor: dict | Counter):
        valor = valor if isinstance(valor, Counter) else Counter(valor)
        self._rapido = valor


    #? Métodos privados
    def _retornar_tipo(self, tipo: str):
        tipo = tipo.upper()

        if tipo not in string.ascii_uppercase[:string.ascii_uppercase.index('V') + 1]:
            raise ValueError(f'O tipo "{tipo}" não existe na tabela de tesouro. Escolha entre "A" até "V"')

        return tipo


    #? Métodos públicos
    
