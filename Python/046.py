print('\033[36;40mExercício Python #046 - Contagem regressiva\033[m')
print('=' * 43)
from time import sleep
print('O foguete será lançado em...')
sleep(0.5)
for c in range(10, -1, -1):
    sleep(1)
    print('   {}'.format(c))
sleep(0.5)
print('')
print('Lançando o foguete')
