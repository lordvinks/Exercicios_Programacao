print(' \033[36;40mExercício Python #056 - Analisador completo\033[m')
print('')
# import
from time import sleep
# Grandezas
maior = 0
nameup = ''
m = 0
f = 0
n = 0
# Repetição
for c in range(1, 5):
    print('-' * 5, end='{}ª Pessoa'.format(c))
    print('-' * 5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: ').strip())
    sexo = str(input('Sexo[M/F]: ').strip().upper())
    # Total idade
    n += idade
# Maior idade
    if idade > maior:
        maior = idade
        nameup = nome
# Sexo total
    if sexo == 'M':
        if idade < 20:
            m += 1
    if sexo == 'F':
        if idade < 20:
            f += 1
print('')
print('---' * 20)
sleep(1)
print('Processando...')
sleep(1)
# Calculo da média
media = n / 4
# média do grupo
print(' A média de idade do grupo é de {} anos'.format(media))
print('_+_' * 20)
sleep(1)
# Mais velho
print(' A pessoa mais velha possui {} anos e se chama {}'.format(maior, nameup))
print('_+_' * 20)
sleep(1)
# T = masculino com menos de 20 anos
if m == 1:
    print(' Ao todo tem {} pessoa do sexo masculino com menos de 20 anos! '.format(m))
    #
    print('_+_' * 20)
    #
    sleep(1)
elif m > 1:
    print(' Ao todo são {} pessoas do sexo masculino com menos de 20 anos!'.format(m))
    #
    print('_+_' * 20)
    sleep(1)
    #
    # T = feminino com menos de 20 anos
if m == 1:
    print(' Temos {} pessoa do sexo feminino com menos de 20 anos'.format(f))
    #
    print('_+_' * 20)
    sleep(1)
    #
elif f > 1:
    print(' São {} pessoas do sexo feminino com menos de 20 anos!'.format(f))
    #
    print('_+_' * 20)
    sleep(1)
    #
# Não há pessoas com menos de 20
if f > 20:
    print(' Não temos pessoas com menos de 20 anos!')
    #
    print('_+_' * 20)
    sleep(4)
    #
print('')
print('-_- The End -_-')
