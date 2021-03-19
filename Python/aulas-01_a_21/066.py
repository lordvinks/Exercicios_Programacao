print(' \033[36;40mExercício Python #065 - Vários números com flag\033[m') 

soma = cont = 0

while True:
    n  = int(input('Digite um número (999 PARA SAIR): '))
    
    if n==999:
        break
    else:
        cont += 1
        soma += n

print(f'Foram somados {cont} números. Nessa soma obtemos um valor igual a {soma}!')
    
