print('\033[36;40mExercício Python #091​ - Jogo de Dados em Python\033[m')

from random import randint
from operator import itemgetter

jogo = dict()
ranking = list()

for i in range(0, 4):
    jogo[f'jogador {i}'] = randint(1, 6)
    print('JOGADOR {}: {} pontos'.format(i+1, jogo[f'jogador {i}']))

print('=-=' * 20)                                                        

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for num, v in enumerate(ranking):
    print(f'{num+1} lugar: {v[0]} com {v[1]}')
