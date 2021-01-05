print('\033[36;40mExercício Python #078 - Maior e Menor valores na Lista\033[m')


# Iniciando variáveis
    # Compostas
nomeNumeros = ('primeiro', 'segundo', 'terceiro', 'quarto', 'quinto')
numeros = list()
    # Simples
maior = ''
menor = ''
posicaoMaior = ''
posicaoMenor = ''

for i in range(0, 5):
    numeros.append(int(input(f'Digite o {nomeNumeros[i]} valor: ')))
    #maior e menor
    if i == 0:
        maior = numeros[i]
        menor = numeros[i]
        posicaoMaior = i
        posicaoMenor = i

    elif numeros[i] > maior:
        maior = numeros[i]
        posicaoMaior = i
    elif numeros[i] < menor:
        menor = numeros[i]
        posicaoMenor = i

#output
print('\n{}MAIOR E MENOR VALOR{}'.format(6*'--', 6*'--'))
print(f'O número {maior} é o maior valor, na posição {posicaoMaior}')
print(f'Já o {menor} é o menor valor, na posição {posicaoMenor}\n')

