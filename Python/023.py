print('Exercício Python #023 - Separando dígitos de um número')
n = int(input('Diga um Número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Possui {} unidade(s)'.format(u))
print('Possui {} Dezena(s)'.format(d))
print('Possui {} Centena(s)'.format(c))
print('Possui {} Milhar(es)'.format(m))
