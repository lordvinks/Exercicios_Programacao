def resumo(v=0, pA=0, pR=0, dinheiro=False):
    valorF = v
    if dinheiro == True:
        valorF = moeda(v)

    print('')
    print('--' * 15)
    print(f'        RESUMO DO VALOR')
    print('--' * 15)
    print(f'Valor analisado: {valorF:>11}')
    print(f'Dobro do valor:  {dobro(v, dinheiro):>11}')
    print(f'Metade do valor: {metade(v, dinheiro):>11}')
    print(f'{pA:<3}% de aumento:  {aumentar(v, pA, dinheiro):>10}')
    print(f'{pR:<3}% de redução:  {diminuir(v, pR, dinheiro):>10}')

def dobro(v, dinheiro):
    v *= 2
    return v if dinheiro is False else moeda(v)

def metade(v, dinheiro):
    v /= 2
    return v if dinheiro is False else moeda(v)

def aumentar(v, p, dinheiro):
    v += (v * p) / 100
    return v if dinheiro is False else moeda(v)

def diminuir(v, p, dinheiro):
    v -= (v * p) / 100
    return v if dinheiro is False else moeda(v)

def moeda(v):
    return f'R${v:.2f}'.replace('.', ',')