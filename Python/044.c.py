print('\033[36:40mExercício Python #044 - Gerenciador de Pagamentos\033[m')

print('')

from time import sleep

print('\033[34m|', end='_' * 31)
print('|')
print(' |', end='=-=' * 3)
print('<Loja Vizu>', end='=-=' * 3)
print('|')
print('|', end='-' * 31)
print('|')

sleep(2)

print('')

valor = float(input('\033[32m Digite o valor do produto: R$'))

print('')

sleep(1.5)

formapag = str(input('''Qual será a forma de pagamento?\033[m
\033[34m|1| : à vista dinheiro/cheque: 10% de desconto.
|2| : à vista no cartão: 5% de desconto.
|3| : em até 2x no cartão: preço normal.
|4| : 3x ou mais no cartão: 20% de juros.

\033[35mMétodo desejado: \033[m''').strip())
print('')

sleep(2)

# Opcão 1
if formapag == '1':
    formapage = 'à vista no dinheiro/cheque'
    d1 = (valor * 10) / 100
    desconto = valor - d1
    print('''\033[34m Preço original do Produto: R${} 
 10% do valor = R${}
 Forma de pagamento: {}

\033[32m O produto passará a custar R${:.1f}'''.format(valor, d1, formapage, desconto))

    sleep(10)

# Opcão 2
elif formapag == '2':
    formapage = 'à vista no cartão'
    d1 = (valor * 5) / 100
    desconto = valor - d1
    print('''\033[34m Preço original do Produto: R${} 
 10% do valor = R${}
 Forma de pagamento: {}


\033[32m O produto passará a custar R${:.1f}\033[m'''.format(valor, d1, formapage, desconto))
    sleep(10)

# Opção 3
elif formapag == '3':
    formapage = 'preço normal'
    print('''\033[34m Forma de Pagamento: {}
 0% do valor = R$0,00

 Preço do Produto: R${}  \033[m'''.format(formapage, valor))
    sleep(10)

# Opção 4
elif formapag == '4':
    formapage = '3x ou mais no cartão'
    d1 = (valor * 20) / 100
    desconto = valor + d1
    print('''\033[34m Preço original do Produto: R${} 
 Adição : R${}
 Forma de pagamento: {}

\033[32m O produto passará a custar R${:.1f}\033[m'''.format(valor, d1, formapage, desconto))
    sleep(10)

# Deu ruim
elif formapag != '1' and '2' and '3' and '4':
    print('''\033[31m Acho que você digitou a forma de pagamento errada!
Lembrando, é um número de \033[4:31m1 a 4\033[m''')
    sleep(10)

print('_' * 31)
