while True:
    print('\033[1;42m~~~' * 10)
    print('\033[1;42m  SISTEMA DE AJUDA PyHELP     ')
    print('~~~' * 10)

    escolhaUser = str(input('\033[mFunção ou Biblioteca > ')).strip()

    if escolhaUser.lower() == 'fim':
        print('\033[1;41m~~~' * 10)
        print('           Até logo           ')
        print('\033[1;41m~~~' * 10)
        print('\033[m')
        break
