def fatorial(num, operacao=False):
    s = 1
    if (operacao):
        textoOperacao = ''

    if num > 0:

        while num > 0:

            if (operacao):
                print('{}'.format(num), end='')
                print(' x ' if num > 1 else ' = ', end='')

            s *= num
            num -= 1

        print(s)

    else:
        print(f'\nO valor {num} não possui um fatorial valido\n')



print('\033[36;40mExercício Python #102​ - Função para Fatorial\033[m')

while True:
    print('=-=' * 15)
    num = int(input('Digite um valor (0 para sair): '))
    if num == 0:
        break

    else: 
        mostrarOp = False

        while True:
            escolha = str(input('Deseja que a operação seja mostrada? [s/n]: ')).strip().lower()[0]
            if escolha == 's':
                mostrarOp = True
                break
            elif 's' != escolha != 'n':
                print('\nValor inválido. Tente novamente!\n')
            else:
                break

        print('=-=' * 15)
        fatorial(num, mostrarOp)
