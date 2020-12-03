print(' \033[36;40mExercício Python #061 - Progressão Aritmética v2.0\033[m')

print('-=' * 10)

from time import sleep

primeiro = int(input(' PRIMEIRO TERMO: '))
razao = int(input(' RAZÃO DA PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    print(' {} '.format(termo), end='')
    sleep(0.5)
    print('->', end='')
    sleep(0.5)
    termo = termo + razao
    cont += 1
print(' FIM')
