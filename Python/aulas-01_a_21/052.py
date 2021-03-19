print('\033[36;40m Exercício Python #052 - Números primos\033[m')
from time import sleep
num = int(input('Digite um número: '))
t = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' -> ')
        t += 1
    else:
        print('\033[31m', end=' -> ')
    print('{}'.format(c), end='')
sleep(1)
print('\n\033[m O número {} foi divisivel {} vezes'.format(num, t))
if t == 2:
    print('Portanto ele é um número primo!')
else:
    print('Portanto ele não é um número primo!!')