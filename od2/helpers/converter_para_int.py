def _checar_conversao(texto: str):
    try:
        int(texto)
        return True
    except (ValueError, TypeError):
        return False
    
def converter_para_numero(texto):
    if _checar_conversao(texto):
        return int(texto)
    return texto
