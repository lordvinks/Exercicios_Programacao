def isNumber(valor):
    try:
        int(valor)
    except ValueError:
        return False
    return True


def ficha(nome='(nome não definido)', gols=0):

    if nome == '':
        nome = '(nome não definido)'

    validarValor = isNumber(gols)

    if (validarValor == False):
        gols = 0
    
    
    print(f'O jogador {nome} fez {gols} no campeonato') 


print('\033[36;40mExercício Python #103​ - Ficha do Jogador\033[m')

while True:
    print('=-=' * 15)
    ficha(str(input('Nome do jogador: ').strip().capitalize()), str(input('Quantidade de gol(s): ')).strip())

    escolha = ''
    while True:
        escolha = str(input('Deseja sair? [s/n]: ')).lower()[0]

        if escolha != 's' and escolha != 'n':
            print('\nValor inválido. Tente novamente!', end=' ')
        else:
            break

    if escolha == 's':
        break
