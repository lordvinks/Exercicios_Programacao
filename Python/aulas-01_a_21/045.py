print('\033[36;40mExercício Python #045 - GAME: Pedra Papel e Tesoura\033[m')
import random
from time import sleep
escolher = str(input('''Escolha...
 |1| Pedra
 |2| Papel
 |3| Tesoura
 Sua escolha: '''))
if escolher == '1':
    escolha = '\033[36mPEDRA\033[m'
elif escolher == '2':
    escolha = '\033[36mPAPEL\033[m'
elif escolher == '3':
    escolha = '\033[36mTESOURA\033[m'
else:
    escolha = '\033[31mTente novamente. É preciso de um número de 1 a 3!!\033[m'
print('')
sleep(0.5)
print('\033[36m  JO')
sleep(1)
print('  KEN')
sleep(1)
print('  PÔ\033[m')
print('')
sleep(1)
pedra = '\033[36mPEDRA\033[m'
papel = '\033[36mPAPEL\033[m'
tesoura = '\033[36mTESOURA\033[m'
list = [pedra, papel, tesoura]
r = random.choice(list)
if escolha == r:
    print('''\033[32m Computador: {}
    \033[32m Você: {}
    \033[32m Parabéns! Você conseguiu!!!\033[m'''.format(r, escolha))
elif escolha != r:
    print('''\033[33m Computador: {}
        \033[33m Você: {}
        \033[33m Tente Outra vez! Você consegue!!!\033[m'''.format(r, escolha))
sleep(10)
print('=-=' * 5, end=' The End ')
print('=-=' * 5)
