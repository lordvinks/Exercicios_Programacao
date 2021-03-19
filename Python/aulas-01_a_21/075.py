print('\033[36;40mExercício Python #075 - Análise de dados em uma Tupla\033[m')
print('=-=' * 20)
#tupla input
numeros = ( int(input('Digite um número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite o último número: ')))

#variáveis simples
QuntVzNove = numeros.count(9)
numPares = ''
posicaoTres = 'N/A'

#Vendo quantas vezes o 3 aparece
if numeros.count(3) > 0:
    posicaoTres = numeros.index(3) + 1

#Verificando se número é par
for num in numeros:
    if num % 2 == 0:
        numPares += '{}, '.format(num)

#output
print('=-=' * 20)
print(f'O NOVE APARECE {QuntVzNove} VEZ(ES)')
print(f'POSIÇÃO DO PRIMEIRO NÚMERO TRÊS: {posicaoTres}')
print(f'NÚMERO(S) PAR(ES) DIGITADO(S): {numPares[ 0:len(numPares)-2 ]}' if numPares != '' else 'NÚMERO(S) PAR(ES): N/A')
print('=-=' * 20)
