print('\033[36;40mExercício Python #076 - Lista de Preços com Tupla\033[m \n')

#Tuplas
produtos = ('Lápis', 'Borracha', 'Caderno', 'Estojo', 'Transferidor', 'Compasso', 'Mochila', 'Caneta', 'Livro')
precos = (1.75, 2.0, 15.90, 25.00, 4.20, 99.99, 120.22, 22.30, 34.90)

# output
for cont in range(0, len(produtos)):
    print(f'{produtos[cont]:.<30}', end='R$')
    print(f'{precos[cont]}')
