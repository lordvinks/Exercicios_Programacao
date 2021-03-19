print(' \033[36;40mExercício Python #062 - Super Progressão Aritmética v3.0\033[m')
print('')

termo = int(input(' \033[33mPrimerio Termo: \033[m').strip())
razao = int(input(' \033[33mRazão: \033[m').strip())

cont = 0
numt = 0
quant = 0

while cont <= 10 + quant:
    print(' {} '.format(termo), end='')
    print('->', end='')
    termo = termo + razao
    cont += 1

    if 10 + quant == cont:
        print(' Pausa')
        print('')
        pergunta = str(input(' \033[33mDeseja add mais termos(S/N)?\033[m ').strip().upper())
        print('')

        if pergunta == 'S':
            quant = int(input(' \033[33mQuantos termos deseja add?\033[m ').strip())

        elif pergunta == 'N':
            quant = quant - 1
print('')
print(' \033[33mNo total foram {} termos utilizados\033[m'. format(cont))






