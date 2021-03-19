from pacotes import ex108


print('\033[36;40mExercício Python #108​ - Formatando Moedas em Python\033[m\n')

v = float(input('Digite o preço: R$'))

print(f'\nA metade de {v} é {ex108.metade(v)}')
print(f'O dobro de {v} é {ex108.dobro(v)}')
print(f'Aumentando 10%, temos {ex108.aumentar(v, 10)}')
print(f'Reduzindo 13%, temos {ex108.diminuir(v, 13)}')