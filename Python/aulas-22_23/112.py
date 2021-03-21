def dadosValor(txt='', dinheiro=False):
    valor = ''
    while True:
        valor = str(input(f'\nDigite {txt}: R$' if dinheiro == True else f'Digite {txt}: '))
        sit = dados.leiaDinheiro(valor)
        if sit == True:
            break

    return float(valor) if txt == 'o valor' else int(valor)



from utilidadesCeV import dados, moeda

print('\033[36;40mExercício Python #112​ - Entrada de dados monetários\033[m\n')

escolhaMoeda = False
while True:
    escolha = str(input('Ele devera ser formatado como moeda? [s/n]: ')).strip().lower()[0]
    if escolha == 's' or escolha == 'n':
        if escolha == 's':
            escolhaMoeda = True
        break
    else:
        print('\nVALOR INVÁLIDO. TENTE NOVAMENTE!\n')

moeda.resumo(
    dadosValor('o valor', escolhaMoeda),
    dadosValor('o quanto(s) porcento(s) aumentará'),
    dadosValor('o quanto(s) porcento(s) diminuirá'),
    escolhaMoeda
    )
