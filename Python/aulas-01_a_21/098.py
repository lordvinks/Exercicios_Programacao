def contador(inicio, fim, passo):

    print(f'De {inicio} até {fim}, de {abs(passo)} em {abs(passo)}')
    for a in range(inicio, fim+1, passo):
        print(f'{a}', end=' -> ')

    print('FIM')
    print('=-=' * 15)



print('\033[36;40mExercício Python #098​ - Função de Contador\033[m\n')
print('=-=' * 15)

contador(1, 10, 1)
contador(10, -2, -2)

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

if inicio > fim:
    passo *= -1
    fim -= 2
if passo == 0:
    passo = 1

contador(inicio, fim, passo)
