print('\033[36;40mExercício Python #084 - Lista composta e análise de dados\033[m')

continua = maiorMassa = menorMassa = ''
pessoas = list()

while continua != 'n':
    print('=-=' * 20)
    dados = list()

    nome = str(input('Nome: ')).strip().capitalize()
    dados.append(float(input('Massa: ')))
    dados.append(nome)
    pessoas.append(dados[:])

    while True:
        userEscolha = str(input('Deseja continuar [s/n]? '))
        if userEscolha in ['s', 'n']:
            continua = userEscolha
            break
        else:
            print('Valor inválido. Tente novamente!\n')

    print('=-=' * 20)

pessoas.sort()

for c, pessoa in enumerate(pessoas):
    if pessoa[0] == pessoas[-1][0]:
        maiorMassa += pessoas[c][1] + ', '
    if pessoa[0] == pessoas[0][0]:
        menorMassa += pessoas[c][1] + ', '

print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'A maior massa é {pessoas[-1][0]}Kg. {maiorMassa}são as pessoa(s) com essa massa!')
print(f'A menor massa é {pessoas[0][0]}Kg. {menorMassa}são as pessoa(s) com essa massa!')
