print(' \033[36;40mExercício Python #058 - Jogo da Adivinhação v2.0\033[m')
# imports
from random import randint
# grandezas
tentativas = 1
escolha = 0
# AI
num = randint(1, 10)
# body
print(''' Estou pensando em um número...
 Será que você consegue advinhar?''')
print('')
# pergunta 1
escolha = int(input(' Claro que sim, é o número... '))
print('')
if escolha > 10 or escolha < 1:
    print('')
    print(' Não prestou atenção, meu caro peralta?')
    print(' É um número de 1 a 10!!')
    tentativas = 0
    print('')
# repetição while
while num != escolha:
    escolha = int(input(' Você errou. Tente novamente! ').strip())
    # Caso escolha um número não requisitado
    if escolha > 10 or escolha < 1:
        print('')
        print(' Não prestou atenção, meu caro peralta?')
        print(' É um número de 1 a 10!!')
        print('')
        tentativas -= 1
    # tentativas
    tentativas += 1
# Acertos
print('')
if tentativas > 5:
    print('Parabéns, você acertou, mas precisou de {} tentativas.'.format(tentativas))
    print('Você está com pouca sorte hoje, hein!!')
elif 5 > tentativas > 1:
    print('Parabéns, você acertou, mas precisou de {} tentativas.'.format(tentativas))
    print(' Até que você é bom, meu amigo!!')
elif tentativas == 1:
    print('Parabéns, você acertou na {}ª tentativa.'.format(tentativas))
    print(' Você tem uma sorte impressionante!!')
else:
    print('Parabéns, você acertou, mas precisou de {} tentativas')
    print(' Isso que eu chamo de azar!!')
