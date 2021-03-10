def notas(qntNotas=0, situacao=False):
    alunoInfos = dict()

    alunoInfos['Média'] = 0

    for a in range(0, qntNotas):
        nota = float(input(f'Digite a nota {a+1}: '))

        alunoInfos['Média'] += nota

        if a == 0:
            alunoInfos['Maior nota'] = alunoInfos['Menor nota'] = nota
        else:
            if nota > alunoInfos['Maior nota']:
                alunoInfos['Maior nota'] = nota

            if nota > alunoInfos['Maior nota']:
                alunoInfos['Menor nota'] = nota

    alunoInfos['Média'] /= qntNotas

    if situacao == True:
        if alunoInfos['Média'] < 6:
            alunoInfos['Situação'] = 'Ruim'
        elif alunoInfos['Média'] >= 6:
            alunoInfos['Situação'] = 'Boa'


    return alunoInfos


print('\033[36;40mEExercício Python #105​ - Analisando e gerando Dicionários\033[m')

while True:
    qntNotasAlunos = int(input('\nDigite a quantidade de notas [0 para sair]: '))

    if qntNotasAlunos == 0:
        break
    else:
        escolha = ''
        while True:
            escolha = str(input('Deseja saber a situação? [s/n]: ')).strip().lower()[0]

            if 's' != escolha != 'n':
                print('\n\033[1;31mVOCÊ DIGITOU UM VALOR INVÁLIDO. TENTE NOVAMENTE!\033[m\n')
            else:
                break

        print('')

        if escolha == 'n':
            valores = notas(qntNotasAlunos)
        else:
            valores = notas(qntNotasAlunos, situacao=True)

        print(valores)