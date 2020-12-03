print('Exercício Python #028 - Jogo da Adivinhação v.1.0')
import random
from time import sleep
r = random.randint(1, 5) #Faz o computador "PENSAR"
print('-=-' * 20)
u = int(input('Escreva um número de 1 a 5? ')) #Jogador tenta adivinhar
print('-=-' * 20)
print('Processando...')
sleep(1)
if u == r:
    print('Parabéns! Você acertou!')
else:
    print('Você errou! Talvez na proxima')
if u >= 6:
    print('É uma número de 1 a 5, amigo!')
print('-=-' * 20)