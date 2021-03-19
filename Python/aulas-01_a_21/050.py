print('\033[36;40m Exercício Python #050 - Soma dos pares \033[m')
print('=' * 40)
s = 0
quant = 0
for c in range(1, 7):
    num = int(input('\033[33m DIGITE UM VALOR: '))
    if num % 2 == 0:
        s += num
        quant += 1
print(' \033[32m A soma dos {} números pares é igual a {}! \033[m'.format(quant, s))
