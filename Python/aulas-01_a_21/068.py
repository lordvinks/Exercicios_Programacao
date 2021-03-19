print(' \033[36;40mExercício Python #068 - Jogo do Par ou Ímpar\033[m')

from random import randint

quantVitorias = 0

while True:
    #Iniciando variáveis
    escolhaUser = 0
    escolhaPc = 0
    tipo = ''

    #Obtendo valores
    print('=-=' * 10)
    numUser = int(input('Digite um número: '))

    while True:
        print('=-=' * 10)
        escolhaUser = str(input('Escolha par ou impar (I/P): ')).strip().lower()

        #SetParImpar
        if escolhaUser == 'i' or escolhaUser == 'impar':
            escolhaUser = 1
            break
        elif escolhaUser == 'p' or escolhaUser == 'par':
            escolhaUser = 0
            escolhaPc = 1
            break
        else:
            print('Valor inválido. Tente novamente\n')

    #Jogada do Bot & soma
    numBot = randint(0, 500)
    
    print('=-=' * 10)
    print(f'0 computador escolheu o valor {numBot}!')
    
    soma = numBot + numUser

    #Vendo quem ganhou
    if (soma) % 2 == 0:
        tipo = 'par'
    else:
        tipo = 'impar'

   # Mensagem
    print('=-=' * 10)
    
    if escolhaUser == soma % 2:
       print(f'Parabéns! Você ganhou!\nO valor total é igual a {soma}, ou seja, um número {tipo}.')
       quantVitorias += 1
    else:
       print(f'Você perdeu! O valor total é igual a {soma}, ou seja, um número {tipo}')
       break

    print('=-=' * 10)
    
print(f'\nVocê ganhou um total de {quantVitorias} rodada(s)!')
print('=-=' * 10)
       
    
        
