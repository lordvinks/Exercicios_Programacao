print('\033[36;40mExercício Python #085 - Listas com pares e ímpares\033[m')

valores = [[], []]

for cont in range(0, 7):
    userNum = int(input('Digite um valor: '))

    if userNum % 2 == 0:
        valores[0].append(userNum)
    else:
        valores[1].append(userNum)

    print('=-='*20)

valores[0].sort()
valores[1].sort()

print(f'Valor(es) Par(es): {valores[0]}')
print(f'Valor(es) Ímpar(es): {valores[1]}')
