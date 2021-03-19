print('\033[36;40mExercício Python #081 - Extraindo dados de uma Lista\033[m')

numeros = list()
escolha = 's'

while escolha == 's':
    print('=-=' * 20)
    numeros.append(int(input('Digite um valor: ')))

    while True:
        escolha = str(input('Deseja continuar (s/n)? ')).strip().lower()
        if escolha in ['s', 'n']:
            break
        else:
            print('Valor inválido. Tente novamente!\n')

numeros.sort(reverse=True)
print('=-=' * 20)
print(f'Foi digitato {len(numeros)} número(s)')
print(f'Lista em ordem decrescente: {numeros}')
print('Possui o valor cinco? Sim' if 5 in numeros else 'Possui valor o cinco? Não')