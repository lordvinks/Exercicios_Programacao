print('\033[36;40mExercício Python #089 - Boletim com listas compostas\033[m')
alunos = list()

while True:
    print('=-=' * 20)
    print('\nO QUE DESEJA FAZER?\n')
    print('[1] CADASTRAR UM ALUNO')
    print('[2] ACESSAR INFORMAÇÕES DE UM ALUNO')
    print('[3] SAIR')
    escolha = str(input('R: ')).strip()

    if escolha == '1':
        escolha = ''
        while escolha != 'n':
            escolha = ''
            info = list()

            print('=-=' * 20)
            print(f'Número do aluno {len(alunos)+1}')
            info.append(str(input('Nome: ')).strip().capitalize())
            nota01 = float(input('Primeira Nota: '))
            nota02 = float(input('Segunda Nota: '))

            info.append(nota01)
            info.append(nota02)
            info.append((nota01+nota02)/2)
            alunos.append(info[:])

            while escolha not in ['s', 'n']:
                escolha = str(input('Deseja continuar [s/n]? ')).strip().lower()
                if escolha not in ['s', 'n']:
                    print('Valor inválido. Tente novamente!\n')

    elif escolha == '2':
        while True:
            print('=-=' * 20)
            print('ACESSAR NOTA DE UM ALUNO')
            escolha = int(input('Número do aluno (0 para sair): '))
            if escolha == 0:
                break
            elif escolha <= len(alunos):
                print('=-=' * 20)
                print(f'Aluno: {alunos[escolha-1][0]}')
                print(f'Nota 01: {alunos[escolha-1][1]}')
                print(f'Nota 02: {alunos[escolha-1][2]}')
                print(f'Média: {alunos[escolha-1][3]}')
            else:
                print('\nValor inválido. Tente novamente!\n')

    elif escolha == '3':
        break
    else:
        print('\nVALOR INVÁLIDO. TENTE NOVAMENTE!')
