print(' \033[36;40mExercício Python #071 - Simulador de Caixa Eletrônico\033[m')

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
        numSaque = valorSacado
        cedula = 50
        totCedula = 0
        
        while True:
            if numSaque >= cedula:
                numSaque -= cedula
                totCedula += 1
            else:
                if totCedula > 0:
                    print(f' Retirando {totCedula} nota(s) de R${cedula}')
                    totCedula = 0
                    
                if cedula == 50:
                    cedula = 20
                    
                elif cedula == 20:
                    cedula = 10
                    
                elif cedula == 10:
                    cedula = 5
                    
                elif cedula == 5:
                    cedula = 1
                else:
                    break
            
