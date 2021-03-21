from utilidadesCeV import moeda

print('\033[36;40mExercício Python #111​ - Transformando módulos em pacotes\033[m\n')

escolhaMoeda = False
while True:
    escolha = str(input('Ele devera ser formatado como moeda? [s/n]: ')).strip().lower()[0]
    if escolha == 's' or escolha == 'n':
        if escolha == 's':
            escolhaMoeda = True
        break
    else:
        print('\nVALOR INVÁLIDO. TENTE NOVAMENTE!\n')


moeda.resumo(float(input('Digite o valor: R$' if escolhaMoeda == True else 'Digite o valor: ')),
 int(input('Qual será a procentagem de aumento? ')),
  int(input('E qual a porcentagem de redução? ')), escolhaMoeda)