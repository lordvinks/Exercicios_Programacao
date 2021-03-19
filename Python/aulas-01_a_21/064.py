print(' \033[36;40mExercício Python #064 - Tratando vários valores v1.0\033[m')
print('')
print('~~' * 20)

d = 0
cal = 0
quant = 0

while d == 0:
    num = int(input(' \033[33mDigite um número [999 PARA PARAR]:\033[m ').strip())
    print('~~' * 20)
    if num != 999:

        cal += num
        quant += 1

    elif num == 999:
        d = 1

print('')
print('\033[32mVocê digitou {} números, a soma deles é {}.\033[m'.format(quant, cal))