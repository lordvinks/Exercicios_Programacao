pessoas = list()
totPessoas = mediaIdade = 0

while True:
    dados = dict()

    print('=-=' * 20)
    dados['nome'] = (str(input('Nome: '))).strip().capitalize()

    while True:
        dados['sexo'] = str(input('Sexo [m/f]: ')).strip()[0].lower()
        if dados['sexo'] in ['m', 'f']:
            break
        else:
            print('\nValor inválido. Tente novamente!\n\n')
    
    dados['idade'] = int(input('Idade: '))

    print('=-=' * 10)

    continuar = ''
    while True:
        continuar = str(input('Quer continuar? [s/n]: ')).strip().lower()[0]
        if continuar in ['s', 'n']:
            pessoas.append(dados)
            totPessoas += 1
            mediaIdade += dados['idade']
            break
        else:
            print('\nValor inválido. Tente novamente!\n\n')

    if continuar == 'n':
        mediaIdade /= totPessoas
        break


mediaMaior =  totMulher = ''

for i in pessoas:
    if i['sexo'] == 'f':
        totMulher += '{}; '.format(i['nome'])

    if i['idade'] > mediaIdade:
        mediaMaior += '{}, com {}; '.format(i['nome'], i['idade'])

if mediaMaior == '':
    mediaMaior = 'N/A'
if totMulher == '':
    totMulher = 'N/A'

print('=-=' * 10)
print(f'Ao todo foram {totPessoas} cadastrada(s)')
print(f'Com uma média de idade de {mediaIdade:.1f}')
print(f'\nAs mulheres cadastradas são: {totMulher}')
print(f'As pessoas com uma idade acima da média são: {mediaMaior}')
print('=-=' * 10)
