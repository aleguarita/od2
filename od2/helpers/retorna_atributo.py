from ..data import MOD_ATRIBUTOS

def retorna_mod_atributo(valor: int):
    lista = MOD_ATRIBUTOS.keys()

    return next((MOD_ATRIBUTOS[x] for x in lista if x >= valor), None)
