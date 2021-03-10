def leiaInt(num):
    if num.isnumeric() == True:
        print(f'\033[1;32mVocẽ digitou o número {int(num)}\033[m')
    else:
        print(f'\033[1;31mO Valor que digitou não é um número\033[m')


print('\033[36;40mExercício Python #104​ - Validando entrada de dados em Python\033[m')

while True:
    print('=-=' * 15)
    valor = str(input('\nDigite um valor (/ para sair): '))

    if valor == '/':
        break
    else:
        leiaInt(valor)
