print('\033[36;40mExercício Python #088 - Palpites para a Mega Sena\033[m')
# Não se usou listas compostas, pois não foi necessario
escolhaUser = -1

while escolhaUser != 0:
    from random import randint

    print('=-='*20)
    while True:
        escolhaUser = int(input('Quantos jogos deseja que eu sorteie (0 para sair)? '))
        if escolhaUser < 0:
            print('Valor inválido. Tente novamente!\n')
        else:
            break
    print('=-=' * 20)
    for i in range(0, escolhaUser):
        valores = list()
        for j in range(0, 6):
            valores.append(randint(1, 60))
        print(f'Jogo {i+1}: {valores}')
    