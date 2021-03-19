print('\033[36;40mExercício Python #087 - Mais sobre Matriz em Python\033[m')

matriz = [[], [], []]
somaPares = somaTerceiraColuna = somaSegundaLinha = 0

for i in range(0, 3):
    print('=-=' * 10)
    for j in range(0, 3):
        matriz[i].append(int(input(f'[{i}/{j}] Digite um valor: ')))
        if matriz[i][j] % 2 == 0:
            somaPares += matriz[i][j]
        if i == 2:
            somaTerceiraColuna += matriz[i][j]
        if j == 1:
            somaSegundaLinha += matriz[i][j]

print('=-=' * 10)
for valor in matriz:
    print(f'|{valor[0]:^5} | {valor[1]:^5} | {valor[2]:^5}|')
print('=-=' * 15)
print(f'A soma dos valores pares: {somaPares}')
print(f'Soma dos valores da terceira coluna: {somaTerceiraColuna}')
print(f'A soma dos valores da segunda linha: {somaSegundaLinha}')
print('=-=' * 15)
