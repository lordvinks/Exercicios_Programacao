print('\033[36;40m Python Exercício #041 - Classificando Atletas\033[m')
import datetime
from time import sleep
print('')
# Pergunta o ano do nascimento
anolife = int(input('\033[36m Ano de Nascimento: \033[m'))
# Calculos
anohj = datetime.date.today().year
idade = anohj - anolife
print('')
print('Aguarde...')
sleep(1.5)
print('')
# mirim
if idade <= 9:
    print('''\033[31m O atleta tem {} anos
    Classificação: Mirim\033[m'''.format(idade))
    print('')
# infantil
elif 9 < idade <= 14:
    print('''\033[32m O atleta tem {} anos
        Classificação: Infantil\032[m'''.format(idade))
# Junior
elif 14 < idade <= 19:
    print('''\033[33m O atleta tem {} anos
        Classificação: Junior\033[m'''.format(idade))
# Sênior
elif 19 < idade <= 25:
    print('''\033[34m O atleta tem {} anos
        Classificação: Sênior\0334[m'''.format(idade))
# Mastwe
else:
    print('''\033[35m O atleta tem {} anos
        Classificação: Master\033[m'''.format(idade))
sleep(10)
print('\033[37m=-=' * 5, end=' The End ')
print('=-=\033[m' * 5)
