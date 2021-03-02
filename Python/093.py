print('\033[36;40mExercício Python #093​ - Cadastro de Jogador de Futebol\033[m\n')

jogador = dict()

jogador['Nome'] = str(input('Nome: ')).capitalize().strip()
jogador['Número de partidas'] = int(input('Número de partidas jogadas: '))
jogador['Total de gols'] = 0

print('')

for a in range(1, jogador['Número de partidas'] + 1):
    jogador[f'Partida {a}'] = int(input(f'Quantidade de gol(s) na partida {a}: '))
    jogador['Total de gols'] += jogador[f'Partida {a}']

print('')
print('=-=' * 20)

print('\n\nO jogador {} jogou {} partidas.\n'.format(jogador['Nome'], jogador['Número de partidas']))

contJog = 1
for k, v in jogador.items():
    if k == f'Partida {contJog}':
        print(f'>> Na {k}, ele fez {v} gol(s)')
        contJog += 1
    
print('Foi um total de {} gol(s)'.format(jogador['Total de gols']))