print('Exercício Python #019 - Sorteando um item na lista')
import random
a = str(input('Name: '))
b = str(input('Name: '))
c = str(input('Name: '))
d = str(input('Name: '))
list = [a, b, c, d]
s = random.choice(list)
print('O sorteado foi {}'.format(s))