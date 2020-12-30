print(' \033[36;40mExercício Python #072 - Número por Extenso\033[m')

nomesNumero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
escolha = 0

print('=-=' * 20)

while True:
    escolha = int(input('Digite um número inteiro de 0 a 20: '))
    print('=-=' * 20)
    
    if escolha < 0 or escolha > 20:
        print('Valor inválido! Tente novamente ')
    else:
        break


print(f'Você digitou o número {nomesNumero[escolha]}!')
print('=-=' * 20)
