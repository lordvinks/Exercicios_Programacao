print('Exercício Python #027 - Primeiro e último nome de uma pessoa')
nome = str(input('Digite o Seu nome: ')).title()
list = nome.split()
print('Olá Sr(a) {}'.format(nome))
print('Seu primeiro nome é {}'.format(list[0]))
print('Seu ultimo nome é {}'.format(list[len(list)-1]))