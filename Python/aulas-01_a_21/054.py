print(' \033[36;40mExercício Python #054 - Grupo da Maioridade\033[m')
import datetime
print('')

year = datetime.date.today().year

# Grandezas = 0
maior = 0
menor = 0

for c in range(1, 8):
    a = int(input('Em que ano a {}ª pessoa? '.format(c)))
    ano = year - a
    if ano >= 18:
        maior += 1
    elif ano < 18:
        menor += 1

print(' Ao todo temos {} pessoas maiores de idade!'.format(maior))
print(' E também {} pessoas menores de idade!'.format(menor))

