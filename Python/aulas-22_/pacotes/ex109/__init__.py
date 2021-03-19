def dobro(v, moeda=False):
    v *= 2
    return analiseMoeda(moeda, v)

def metade(v, moeda=False):
    v /= 2
    return analiseMoeda(moeda, v)

def aumentar(v, p=0, moeda=False):
    v += (v * p) / 100
    return analiseMoeda(moeda, v)

def diminuir(v, p=0, moeda=False):
    v -= (v * p) / 100
    return analiseMoeda(moeda, v)

def moeda(v):
    return f'R${v:.2f}'.replace('.', ',')

def analiseMoeda(escolha, v):
    if escolha == True:
        return moeda(v)
    else:
        return v
