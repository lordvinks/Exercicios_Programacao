def msg(v):
    print(f'\033[1;32mO valor digitado foi {v}\033[m')

def leiaInt():
    while True:
        try:
            n = str(input('Digite um valor inteiro: ')).strip()
            int(n)
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor, digite um número inteiro valido.\033[m\n')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mERRO: entrada de dados interrompida pelo usuário\033[m\n')
            continue
        else:
            msg(n)
            break

def leiaFloat():
    while True:
        try:
            n = str(input('Digite um valor real: ')).strip()
            float(n)
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor, digite um número inteiro valido.\033[m\n')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mERRO: entrada de dados interrompida pelo usuário\033[m\n')
            continue
        else:
            msg(n)
            break



print('\033[36;40mExercício Python #113​ - Funções aprofundadas em Python\033[m')
leiaInt()
leiaFloat()
