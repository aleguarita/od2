import string
from collections import Counter
from RPG import rolar_dado_notacao, rolar_tabela, d6

from ..helpers import x_em_d6
from ..data import DATA

tesouro_aleatorio = DATA.TESOURO_ALEATORIO
equipamento_raridade = DATA.TESOURO_EQUIPAMENTOS_RARIDADE
equipamento_tipo = DATA.TESOURO_EQUIPAMENTOS



class TesouroAleatorio:
    def __init__(self, tipo_tesouro: str):
        """Gera um tesouro aleatório baseado no tipo, na tabela 9.5.\n
        O tesouro é rolado automaticamente, bastando criar um objeto com a classe,
        mas é possível rolar novamente caso queira rolar mais de um tesouro do mesmo tipo
        através do método .rolar()

        Args:
            tipo_tesouro (str): qual o tipo do tesouro rolado

        Raises:
            ValueError: Levanta um erro no caso do tipo do tesouro não existir

        Returns:
            .tesouro: os dados do tesouro rolado
            .tesouro_rapido: o conteúdo do tesouro rápido
        """

        self._tipo = self._retornar_tipo(tipo_tesouro)
        self._rapido = Counter(self.tabela.get('tesouro_rapido'))
        self._tesouro = Counter()
        self.rolar()


    #? Propriedades
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo_tesouro: str):
        self._tipo = self._retornar_tipo(tipo_tesouro)
        self.rolar()

    @property
    def tabela(self):
        return [i for i in tesouro_aleatorio if i.get('tipo') == self.tipo][0]

    @property
    def tesouro_rapido(self):
        """O tesouro rápido de apenas moedas, pegando a média das chances (primeiro item da tabela 9.5)"""
        return self._rapido

    @tesouro_rapido.setter
    def tesouro_rapido(self, valor: dict | Counter):
        valor = valor if isinstance(valor, Counter) else Counter(valor)
        self._rapido = valor

    @property
    def tesouro(self):
        return self._tesouro


    #? Métodos privados
    def _retornar_tipo(self, tipo: str):
        tipo = tipo.upper()

        if tipo not in string.ascii_uppercase[:string.ascii_uppercase.index('V') + 1]:
            raise ValueError(
                f'O tipo "{tipo}" não existe na tabela de tesouro. Escolha entre "A" até "V"')

        return tipo

    def _verificar_se_tem_item(self, tabela: dict):
        return x_em_d6(tabela.get('chance', 0)).sucesso if tabela else False

    def _retornar_moedas(self, chave: str):
        base = self.tabela.get(chave)
        tem_item_valor = self._verificar_se_tem_item(base)

        if not tem_item_valor:
            return 0
        
        return rolar_dado_notacao(base.get('rolamento'))

    def _retornar_gema(self):
        base = self.tabela.get('gemas')
        tem_gema = self._verificar_se_tem_item(base)
        # TODO
        pass

    def _retornar_obj_valor(self):
        base = self.tabela.get('objetos_de_valor')
        tem_obj_valor = self._verificar_se_tem_item(base)
        # TODO
        pass

    def _retornar_equipamentos(self):
        base = self.tabela.get('equipamentos')
        tem_equipamento = self._verificar_se_tem_item(base)
        equipamentos = []

        if tem_equipamento:
            qtd_equipamentos = base.get('rolamento')
            qtd_equipamentos = rolar_dado_notacao(qtd_equipamentos) if isinstance(qtd_equipamentos, str) else int(qtd_equipamentos)

            for _ in range(qtd_equipamentos):
                raridade = rolar_tabela(equipamento_raridade, d6(2))
                item = rolar_tabela(equipamento_tipo, d6(2), raridade, rolar_dados=True)

                equipamentos.append(item)


        return equipamentos


    def _retornar_tesouro(self):
        self._tesouro['po'] = self._retornar_moedas('po')
        self._tesouro['pp'] = self._retornar_moedas('pp')
        self._tesouro['pc'] = self._retornar_moedas('pc')
        self._tesouro['gemas'] = self._retornar_gema()
        self._tesouro['objetos de valor'] = self._retornar_obj_valor()
        self._tesouro['equipamentos'] = self._retornar_equipamentos()

    #? Métodos públicos
    def rolar(self):
        """Rola o tesouro (rolado automaticamente na criação da classe, pode ser rolado novamente)
        """
        self._retornar_tesouro()