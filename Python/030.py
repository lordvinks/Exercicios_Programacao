print('Exercício Python #030 - Par ou Ímpar?')
from time import sleep
n = int(input('Digite um número: '))
ip = n % 2
print('-=-'*20)
if ip <= 0:
    print('{} é um número par'.format(n))
else:
    print('{} é número impar'.format(n))
sleep(1)
print('-=-'*20)
print(ip)