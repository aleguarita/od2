import string
import re
from collections import Counter
from RPG import rolar_dado_notacao, rolar_tabela, d6

from ..helpers import x_em_d6
from ..data import DATA

tesouro_aleatorio = DATA.TESOURO_ALEATORIO
equipamento_raridade = DATA.TESOURO_EQUIPAMENTOS_RARIDADE
equipamento_tipo = DATA.TESOURO_EQUIPAMENTOS
objetos_valor_raridade = DATA.TESOURO_OBJ_VALOR_RARIDADE
objetos_valor_tipo = DATA.TESOURO_OBJ_VALOR



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

    def _retornar_lista_bens(self, tabela: str, tabela_raridade: list, tabela_tipo: list):
        base = self.tabela.get(tabela)
        tem_item = self._verificar_se_tem_item(base)
        resultado = []

        if tem_item:
            qtd_itens = base.get('rolamento')
            qtd_itens = rolar_dado_notacao(qtd_itens) if isinstance(qtd_itens, str) else int(qtd_itens)

            for _ in range(qtd_itens):
                raridade = rolar_tabela(tabela_raridade, d6(2))
                item = rolar_tabela(tabela_tipo, d6(2), raridade, rolar_dados=True)
                resultado.append(item)

        return resultado

    def _substituir_notacao_dado(self, texto: str):
        regex = r'\d*d\d+(?:[-+*/]\d+)?'
        dado = re.search(regex, texto)
        dado = str(rolar_dado_notacao(dado.group())) if dado else ''

        return re.sub(regex, dado, texto)

    def _retornar_moedas(self, chave: str):
        base = self.tabela.get(chave)
        tem_item_valor = self._verificar_se_tem_item(base)

        if not tem_item_valor:
            return 0
        
        return rolar_dado_notacao(base.get('rolamento'))

    def _retornar_gema(self):
        base = self.tabela.get('gemas')
        tem_gema = self._verificar_se_tem_item(base)
        gemas = []

        if tem_gema:
            qtd_gemas = base.get('rolamento')
            qtd_gemas = rolar_dado_notacao(qtd_gemas) if isinstance(qtd_gemas, str) else int(qtd_gemas)

            for _ in range(qtd_gemas):
                gema = rolar_tabela(DATA.TESOURO_GEMA, d6(2))
                qualidade = rolar_tabela(DATA.TESOURO_GEMA_QUALIDADE, d6())
                nome = f'{gema['categoria']} {qualidade['qualidade']}'
                valor = int(gema['valor'] * qualidade['modificador'])

                gemas.append({
                    'categoria': nome,
                    'valor': valor,
                    'descrição': f'{nome}, valor {valor} PO'
                })

        return gemas

    def _retornar_obj_valor(self):
        objetos_valor = self._retornar_lista_bens(
            'objetos_de_valor',
            objetos_valor_raridade, 
            objetos_valor_tipo)
        
        for i, objeto in enumerate(objetos_valor):
            valor = d6(2) * 100
            peso = 1 if objeto[-1] == '*' else 0
            texto = objeto.replace(' *', '')
            objetos_valor[i] = {
                'objeto': texto,
                'valor': valor,
                'carga': peso,
                'descrição': f'{texto}, {valor} PO (carga: {peso})'
            }
        
        return objetos_valor

    def _retornar_equipamentos(self):
        equipamentos = self._retornar_lista_bens(
            'equipamentos',
            equipamento_raridade,
            equipamento_tipo)
        return [self._substituir_notacao_dado(item) for item in equipamentos]

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