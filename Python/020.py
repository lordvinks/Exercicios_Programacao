print('Exercício Python #020 - Sorteando uma ordem na lista')
import random
a = str(input('1: '))
b = str(input('2: '))
c = str(input('3: '))
d = str(input('4: '))
list = [a, b, c, d]
random.shuffle(list)
print('Ordem de apresentação será...')
print(list)