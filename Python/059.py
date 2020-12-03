print('\033[36;40mExercício Python #059 - Criando um Menu de Opções\033[m')
from time import sleep
n1 = float(input('    DIGITE UM NÚMERO: '))
n2 = float(input('    DIGITE OUTRO NÚMERO: '))
sleep(1)
print('=-=' * 20)
escolha = 0
t = 0
maior = 0
while escolha != 5:
    print('=-=' * 20)
    print('''    |1| somar
    |2| multiplicar
    |3| maior
    |4| novos números
    |5| sair do programa''')
    sleep(1)
    print('=-=' * 20)
    escolha = str(input('     R: '))
    sleep(1)
    print('=-=' * 20)
    if escolha == '1':
        t = n1 + n2
        print('   A soma dos número é igual a {}'.format(t))
    elif escolha == '2':
        t = n1 * n2
        print('   A multiplicação dos números é igual à {}'.format(t))
    elif escolha == '3':
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        print('   O maior número é {}'.format(maior))
    elif escolha == '4':
        n1 = float(input('    DIGITE UM NÚMERO: '))
        n2 = float(input('    DIGITE OUTRO NÚMERO: '))
    elif escolha == '5':
        print('ENCERRANDO O PROGRAMA...')
        sleep(3)
        escolha = 5
    sleep(2)



