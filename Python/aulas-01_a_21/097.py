def mensagem(msg):
    qntCaractes = len(msg) + 2

    print('')

    print('~' * qntCaractes)
    print('{}'.format(msg.center(qntCaractes, ' ')))
    print('~' * qntCaractes)


print('\033[36;40mExercício Python #097​ - Um print especial\033[m\n')

mensagem(str(input('Digite uma mensagem: ')).strip())