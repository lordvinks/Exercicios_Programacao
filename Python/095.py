print('\033[36;40mExercício Python #095​ - Aprimorando os Dicionários\033[m')

from time import sleep

jogadores = list()

while True:
    print('=-=' * 20)
    sleep(2)
    print('O QUE DESEJA FAZER?\n')
    print('1: CADASTRAR UM JOGADOR\n2: ACESSAR O CADASTRO DE UM JOGADOR\n3: SAIR')
    escolha01 = str(input('R: '))
    print('=-=' * 20)

    
    if escolha01 == '1':
        print('\n\nCADASTRAR JOGADOR - NÚMERO DO JOGADOR: {}\n'.format(len(jogadores)))
        
        jogador = dict()

        jogador['nome'] = str(input('Nome: ')).capitalize().strip()
        jogador['partidas jogadas'] = int(input('Quantas partidas o {} jogou? '.format(jogador['nome'])))
        jogador['Total de gols'] = 0

        print('')

        for a in range(1, jogador['partidas jogadas'] + 1):
            jogador[f'Partida {a}'] = int(input(f'Quantidade de gol(s) na partida {a}: '))
            jogador['Total de gols'] += jogador[f'Partida {a}']

        jogadores.append(jogador)


    elif escolha01 == '2':
        print('\n\nACESSAR OS DADOS DE UM JOGADOR\n')
        
        numeroJogador = int(input('Número do jogador: '))

        if numeroJogador > len(jogadores):
            print('\nJOGADOR NÃO ENCONTRADO. TENTE NOVAMENTE!')
        else:
            print('NOME: {}'.format(jogadores[numeroJogador]['nome']))
            print('TOTAL DE PARTIDAS JOGADAS: {}'.format(jogadores[numeroJogador]['partidas jogadas']))

            print('\nTOTAL DE GOL(S): {}'.format(jogadores[numeroJogador]['Total de gols']))
            
            for i in range(1, len(jogadores[numeroJogador])-2):
                print('PARTIDA {}: {} GOL(S)'.format(i, jogadores[numeroJogador][f'Partida {i}']))

    
    elif escolha01 == '3':
        print('SAINDO', end='')

        for a in range(0, 3):
            sleep(0.6)
            print('.', end='')
        break

    else:
        print('\nVALOR INVÁLIDO. TENTE NOVAMENTE!\n')
        