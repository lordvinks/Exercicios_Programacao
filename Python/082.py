print('\033[36;40mExercício Python #082 - Dividindo valores em várias listas\033[m')

numeros = list()
pares = list()
impares = list()
escolha = 's'

while escolha == 's':
    print('=-=' * 20)
    num = int(input('Digite um valor: '))
    numeros.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    while True:
        escolha = str(input('Deseja continuar (s/n)? ')).strip().lower()
        if escolha in ['s', 'n']:
            break
        else:
            print('Valor inválido. Tente novamente!\n')

print('=-=' * 20)
print(f'VALOR(ES) DA LISTA: {numeros}')
print(f'VALOR(ES) ÍMPAR(ES): {impares}')
print(f'VALOR(ES) PAR(ES): {pares}')
