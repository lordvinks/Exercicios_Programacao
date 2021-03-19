print(' \033[36;40mExercício Python #057 - Validação de Dados\033[m')
print('')
from time import sleep
sexo = ''
while sexo != 'm' and sexo != 'f':
    print(' \033[1;31mQual é o seu sexo?\033[m')
    print(' \033[35m|M| : Para masculino!\033[m')
    print(' \033[34m|F| : Para feminino!\033[m')
    sleep(1)
    sexo = str(input(' \033[32mR: \033[m').strip().lower())
    print('')
    if sexo != 'm' and sexo != 'f':
        sleep(1)
        print(' \033[31m Atenção!! Apenas as opções \033[35mM\033[31m ou \033[34mF\033[31m são validas!!\033[m')
        print('')
        sleep(1)
sleep(1)
if sexo == 'm':
    print(' \033[35mVocê é do sexo MASCULINO!!\033[m')
elif sexo == 'f':
    print(' \033[34mVocê é do sexo FEMININO!!\033[m')
