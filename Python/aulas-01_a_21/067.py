print(' \033[36;40mExercício Python #067 - Tabuada v3.0\033[m')

while True:
    print('--' * 10)
    num = int(input('Digite um número (Digite um valor negativo para sair): '))
    print('--' * 10)

    if num<0:
        break
    else:
        for x in range(1, 11):
            print(f'{num} x {x} = {num*x}')

print('--------------\nPrograma encerrado...\n--------------')
