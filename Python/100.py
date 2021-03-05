from random import choice
from time import sleep

def sortearNumero(numeros):
    numerosSorteados = list()
    for a in range(0, 4):
        num = choice(numeros)
        numeros.remove(num)
        numerosSorteados.append(num)

    print('\nOs números sorteados foram {}'.format(numerosSorteados))
    somaPares(numerosSorteados)
    

def somaPares(nums):
    par = 0

    for v in nums:
        if v % 2 == 0:
            par += v

    print(f'A soma dos pares é igual a {par}')


listaNumeros = list()

while True:
    print('=-=' * 15)

    numero = int(input('Digite um número inteiro (0 para sair): '))

    if numero == 0 and len(listaNumeros) >= 4:
        sortearNumero(listaNumeros)
        break
    else:
        listaNumeros.append(numero)
