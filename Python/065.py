print(' \033[36;40mExercício Python #065 - Maior e Menor valores\033[m')
print('')
resp = 's'
soma = quant = media = maior = menor = 0

while resp == 's':
    num = int(input(' Digite um número: '))
    soma += num
    quant += 1
    
    if quant == 1:
         maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input(' Deseja continuar [S/N]: ').strip().lower()[0])

media = soma / quant
print(' Você digitou {} números e a média  foi {} '.format(quant, media))
print(' O maior valor foi {} e o menor foi {}'.format(maior, menor))
