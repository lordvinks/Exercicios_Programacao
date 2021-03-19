def resumo(v=0, pA=0, pR=0):
    print('--' * 15)
    print(f'        RESUMO DO VALOR')
    print('--' * 15)
    print(f'Preço analisado: {moeda(v):>10}')
    print(f'Dobro do preço:  {dobro(v):>10}')
    print(f'Metade do preço: {metade(v):>10}')
    print(f'{pA}% de aumento:  {aumentar(v, pA):>10}')
    print(f'{pR}% de redução:  {diminuir(v, pR):>10}')

def dobro(v):
    v *= 2
    return moeda(v)

def metade(v):
    v /= 2
    return moeda(v)

def aumentar(v, p=0):
    v += (v * p) / 100
    return moeda(v)

def diminuir(v, p=0):
    v -= (v * p) / 100
    return moeda(v)

def moeda(v):
    return f'R${v:.2f}'.replace('.', ',')


