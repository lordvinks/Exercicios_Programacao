print('\033[36;40mExercício Python #080 - Lista ordenada sem repetições\033[m')

numeros = list()

for i in range(0, 5):
    num = int(input('DIGITE UM VALOR: '))

    if i == 0 or num > numeros[-1]:
        numeros.append(num)
        print(f'{num} foi adicionado a última posição!\n')
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                print(f'{num} foi adicionado a posição {pos}\n')
                break
            pos += 1

print(f' Os valores em ordem: {numeros}')
