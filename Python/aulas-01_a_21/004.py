print('Exercício Python #004 - Dissecando uma Variável')
from time import sleep
cores = {'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'azulc': '\033[36m',
         'cinza': '\033[37m'}
a = input('{}Digite algo: '.format(cores['amarelo']))
print('Processando...')
sleep(2)
print('{}O timo primitivo desse valor é? {}'.format(cores['vermelho'], type(a)))
print('{}Só tem espaços? {}'.format(cores['verde'], a.isspace()))
sleep(1)
print('{}É um número? '.format(a.isnumeric(), cores['azul']))
print('{}É alfabético? {}'.format(cores['roxo'], a.isalpha()))
sleep(1)
print('{}É alfanúmerico? {}'.format(cores['azulc'], a.isalnum()))
print('{}Está em maiúsculo? {}'.format(cores['cinza'], a.isupper()))
sleep(1)
print('{}Está em minúsculo? {}'.format(cores['amarelo'], a.islower()))
print('Está capitalizada? {}'.format(a.istitle()))
