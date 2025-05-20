from ..helpers import converter_para_numero
from .entidade import EntidadeBase

class Monstro(EntidadeBase):
    def __init__(self, dados: dict):
        # Identificação
        self.nome = dados.get('name')
        self.conceito = dados.get('concept')
        self.alinhamento = dados.get('alignment')
        self.tamanho = dados.get('size')
        self.variante_modificadores = dados.get('variant_modifications')
        self.habitats = dados.get('habitats')
        self.descricao = dados.get('description')
        self.flavor = dados.get('flavor')
        self.tipo = dados.get('type')
        self.variacao = dados.get('variant')

        # Estatísticas
        self.xp = converter_para_numero(dados.get('xp'))
        self.dv = self._retornar_dv(dados.get('dv'))
        self.dv_bonus = self._retornar_dv(dados.get('dv_bonus'))
        self.pv = converter_para_numero(dados.get('pv'))
        self.ca = dados.get('ca')
        self.jp = dados.get('jp')
        self.movimento = dados.get('mv')
        self.moral = dados.get('mo')
        self.ataques = dados.get('attacks')

        # Dados de encontro
        self.tesouro = dados.get('treasure')
        self.tesouro_covil = dados.get('treasure_lair')
        self.encontros = dados.get('encounters')
        self.encontros_covil = dados.get('encounters_lair')

        # Tipos de movimento adicional
        self.movimento_cavando = dados.get('mvc')
        self.movimento_escalando = dados.get('mve')
        self.movimento_nadando = dados.get('mvn')
        self.movimento_outros = dados.get('mvo')
        self.movimento_voo = dados.get('mvv')

        # Informações técnicas
        self.id = dados.get('id')
        self.url = dados.get('url')
        self.imagem = dados.get('picture')
        self.miniatura = dados.get('thumb_picture')
        self.fontes = dados.get('fontes')

        # Propriedades para alteração privada
        super().__init__(self.pv)


    #? Propriedades


    def __repr__(self):
        return f"<Monstro(nome={self.nome})>"

    def __str__(self):
        ataques_str = 'Nenhum ataque'
        mod_dv = '' if not self.dv_bonus else self.dv_bonus
        mod_dv = f'+{mod_dv}' if mod_dv and mod_dv > 0 else mod_dv

        if self.ataques:
            ataques_str = ', '.join(
                a.get('text', 'Ataque desconhecido') for a in self.ataques)

        return (
            f"{self.nome} ({self.xp} xp). "
            f"DV {self.dv}{mod_dv} ({self.pv} pv), "
            f"CA {self.ca}, JP {self.jp}, "
            f"MV {self.movimento}, MO {self.moral}. "
            f"Ataques: {ataques_str}"
        )
    
    
    #? Métodos privados
    def _retornar_dv(self, dv_original: str):
        if dv_original == '½':
            return 0.5
        return converter_para_numero(dv_original)

    def _retornar_mod_dv(self, dv_original: str):
        if not dv_original:
            return 0
        return converter_para_numero(dv_original)
    
    def _retornar_ac(self):
        pass

    #? Métodos públicos
    def calcular_vida(self):
        """Recalcula a vida, para o caso de mudar o HD da criatura
        """
        vida_base = 5 * self.dv
        
        self.pv = vida_base + self.dv_bonus

    

