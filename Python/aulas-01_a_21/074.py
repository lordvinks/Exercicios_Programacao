print('\033[36;40mExercício Python #074 - Maior e menor valores em Tupla\033[m')

from random import randint
numeros = ((randint(10, 100)), (randint(10, 100)), (randint(10, 100)), (randint(10, 100)), (randint(10, 100)))
maior = menor = 0

print('\nNÚMEROS SORTEADOS:')
for cont, num in enumerate(numeros):
    print(f'{cont+1} número: {num}')

(f'\n{min(numeros)} é o menor número\n{max(numeros)} é o maior número')
