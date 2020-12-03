print('\033[36;40mExercício Python #006 - Dobro, Triplo, Raiz Quadrada\033[m')
num = int(input('\033[33mDigite um número: ').strip())
d = num * 2
t = num * 3
r = num ** (1/2)
print('\033[34mO dobro de {} é {}'.format(num, d))
print('\033[35mO triplo de {} é {}'.format(num, t))
print('\033[36mA raiz quadrada de {} é {}'.format(num, r))
