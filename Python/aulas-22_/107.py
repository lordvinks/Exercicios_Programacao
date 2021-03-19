from pacotes import ex107


print('\033[36;40mExercício Python #107​ - Exercitando módulos em Python\033[m\n')

v = float(input('Digite o preço: R$'))

print(f'\nA metade de {v} é R${ex107.metade(v)}')
print(f'O dobro de {v} é R${ex107.dobro(v)}')
print(f'Aumentando 10%, temos R${ex107.aumentar(v, 10)}')
print(f'Reduzindo 13%, temos R${ex107.diminuir(v, 13)}')