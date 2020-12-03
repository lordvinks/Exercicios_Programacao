print(' \033[36;40mExercício Python #053 - Detector de Palíndromo\033[m ')
print('')
frase = str(input(' 0Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}!'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('A frase digitada não é um Palíndromo!')
