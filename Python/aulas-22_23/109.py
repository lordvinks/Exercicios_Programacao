from pacotes import ex109


print('\033[36;40mExercício Python #109​ - Formatando Moedas em Python\033[m\n')

v = float(input('Digite o valor: '))

escolhaMoeda = False
while True:
    escolha = str(input('Ele devera ser formatado como moeda? [s/n]: ')).strip().lower()[0]
    if escolha == 's' or escolha == 'n':
        if escolha == 's':
            escolhaMoeda = True
        break
    else:
        print('\nVALOR INVÁLIDO. TENTE NOVAMENTE!\n')

print(f'\nA metade de {v} é {ex109.metade(v, escolhaMoeda)}')
print(f'O dobro de {v} é {ex109.dobro(v, escolhaMoeda)}')
print(f'Aumentando 10%, temos {ex109.aumentar(v, 10, escolhaMoeda)}')
print(f'Reduzindo 13%, temos {ex109.diminuir(v, 13, escolhaMoeda)}')