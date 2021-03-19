print('\033[36;40mExercício Python #069 - Análise de dados do grupo\033[m') 

maioresIdade = 0
homens = 0
mulheresMenos20 = 0

while True:
    sexo = ''

    print('=-=' * 20)
    idade = int(input('Idade: '))
    
    while True:
        
        sexo = str(input('Sexo (m/f): ')).strip().lower()
        
        if sexo == 'm' or sexo == 'f':
            
            if idade > 18:
                maioresIdade += 1
            if sexo == 'm':
                homens += 1
            if idade < 20 and sexo == 'f':
                mulheresMenos20 += 1               
            break
        else:
            
            print('=-=' * 20)
            print('Valor inválido! Tente novamente.')


    continuar = ''
    while True:
        print('=-=' * 20)
        continuar = str(input('Deseja continuar (s/n): ')).strip().lower()

        if continuar == 's' or continuar == 'n' or continuar == 'sim' or continuar == 'não':
            break

        else:
            print('=-=' * 20)
            print('Valor inválido! Tente novamente,')

    if continuar == 'n' or continuar == 'não':
        break

print('=-=' * 20)
print(f'Há {maioresIdade} pessoa(s) com mais de 18 anos.')
print(f'Tem {homens} homens cadastrados')
print(f'Possui {mulheresMenos20} mulher(es) com menos de 20 anos')
print('=-=' * 20)
        
        
