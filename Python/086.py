print('\033[36;40mExercício Python #086 - Matriz em Python\033[m')

matriz = [[], [], []]

for i in range(0, 3):
    print('=-=' * 10)
    for j in range(0, 3):
        matriz[i].append(int(input(f'[{i}/{j}] Digite um valor: ')))

print('=-=' * 10)
for valor in matriz:
    print(f'|{valor[0]:^5} | {valor[1]:^5} | {valor[2]:^5}|')
print('=-=' * 10)
