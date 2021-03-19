print('\033[36;40mExercício Python #079 - Valores únicos em uma Lista\033[m')


# DECLARAÇÃO DE VARIÁVEIS
numeros = list()

while True:
    print('=-=' * 10)
    valor = int(input('Digite um valor: '))

    print('=-=' * 10)

    if valor not in numeros:
        numeros.append(valor)
        print(' --VALOR ADD COM SUCESSO--')
    else:
        print(' --VALOR DUPLICADO - NÃO SERÁ ADD--')

    print('=-=' * 10)

    escolha = ''
    while escolha not in ('s', 'n'):
        escolha = str(input('Deseja continuar (s/n)? ')).strip().lower()[0]

        if escolha != 's' and escolha != 'n':
            print('VALOR INVÁLIDO. TENTE NOVAMENTE!\n')

    if escolha == 'n':
        break

# output
numeros.sort()

print('==='*10)
for cont, numero in enumerate(numeros):
    print(f'Na posição {cont} há o número {numero}')
print('==='*10)