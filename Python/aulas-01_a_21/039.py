print('\033[36;40mExercício Python #039 - Alistamento Militar\033[m')
from time import sleep
import datetime
ano = datetime.date.today().year
#Pergunta01
datan = int(input('\033[33mEm que ano você nasceu? \033[m').strip())
print('\033[32mAGUARDE...\033[m')
sleep(1)
print('')
#CalculosAno
c1 = ano - datan
# 18 anos
if c1 == 18:
    print('\033[34m Quem nasceu em {} tem {} anos em {}. '.format(datan, c1, ano))
    print(' O seu alistamento é nesse ano de {}!'.format(ano))
# Menor que 18
elif c1 < 18:
    c2 = 18 - c1
    c3 = ano + c2
    print('\033[34m Quem nasceu em {} tem {} anos em {}. '.format(datan, c1, ano))
    if c2 == 1:
        print(' Ainda falta {} ano para o alistamento'.format(c2))
    elif c2 > 1:
        print(' Ainda faltam {} anos para o alistamento'.format(c2))
    print(' Seu alistamento será em {}'.format(c3))
# Maior que 18
else:
    c4 = c1 - 18
    c5 = ano - c4
    print(' Quem nasceu em {} tem {} anos. '.format(datan, c1))
    if c4 == 1:
        print(' Você já deveria ter se alistado há {} ano '.format(c4))
    elif c4 > 1:
        print(' Você já deveria ter se alistado há {} anos '.format(c4))
    print(' O seu alistaento foi em {}'.format(c5))
print('-=-' * 8, end='The End')
print('-=-' * 8)
