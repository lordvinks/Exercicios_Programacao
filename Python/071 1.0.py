print(' \033[36;40mExercício Python #071 - Simulador de Caixa Eletrônico\033[m')

from math import floor

while True:
    #Iniciando variáveis
    unidade = dezena = centena = milhar = 0
    
    print('=-=' * 20)
    valorSacado = int(input('Valor que será sacado (0 para sair): '))
    print('=-=' * 20)

    if valorSacado < 0 or valorSacado > 1000:
        print('Valor inválido. Tente novamente.')
        
    elif valorSacado == 0:
        break
    
    else:
        num = valorSacado
        
        if valorSacado >= 1000:
            
            unidade = num % 10
            num = (num - unidade) / 10
            dezena = int(num % 10)
            num = (num - dezena) / 10
            centena = int(num % 10)
            milhar = int((num - centena) / 10)


        elif valorSacado >= 100 and valorSacado < 1000:

            unidade = num % 10
            num = (num - unidade) / 10
            dezena = int(num % 10)
            centena = int((num - dezena) / 10)

        elif valorSacado < 100 and valorSacado >= 10:
            
            unidade = num % 10
            dezena = int((num - unidade) / 10)

        else:
            unidade = num


        #Separando cédulas
        quant50 = 0
        quant20 = 0
        quant10 = 0
        quant5 = 0
        quant1 = 0

        #notas de 50
        if milhar > 0:
            quant50 = milhar * 20 
        if centena > 0:
            quant50 += centena * 2            
        if dezena >= 5:
            quant50 += 1
            dezena -= 5
            
        #notas de 20    
        if dezena >= 2:
            quant20 += floor(dezena / 2)
            dezena -= floor(dezena / 2) * 2
        if dezena == 1:
            quant10 += 1

        #notas de 5
        if unidade >= 5:
            quant5 += floor(unidade / 5)
            unidade -= floor(unidade / 5) * 5

        #notas de 1
        if unidade > 0:
            quant1 =+ unidade
            
        
        print('=-=' * 20, end='')
        print(f'\n Retirando {quant1} nota(s) de R$1,00' if quant1>0 else '', end='')
        print(f'\n Retirando {quant5} nota(s) de R$5,00' if quant5>0 else '', end='')
        print(f'\n Retirando {quant10} nota(s) de R$10,00' if quant10>0 else '', end='')
        print(f'\n Retirando {quant20} nota(s) de R$20,00' if quant20>0 else '', end='')
        print(f'\n Retirando {quant50} nota(s) de R$50,00' if quant50>0 else '', end='\n')
        
        


