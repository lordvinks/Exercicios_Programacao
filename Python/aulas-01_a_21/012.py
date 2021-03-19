print('Exercício Python #012 - Calculando Descontos')
a6 = float(input('Preço: '))
b6 = int(input('Desconto:'))
c6 = a6 * b6 / 100
d6 = a6 - c6
print(' O valor com o desconto de {} % é de {} Reais '.format(b6, d6))