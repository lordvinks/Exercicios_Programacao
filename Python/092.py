print('\033[36;40mExercício Python #092​ - Cadastro de Trabalhador em Python\033[m')


from datetime import datetime
pessoa = dict()

# input das infos
pessoa['Nome'] = str(input('Nome: '))
pessoa['Ano do Nascimento'] = int(input('Ano do Nascimento: '))
pessoa['Carteira de Trabalho'] = int(input('Carteira de Trabalho (0 se não tiver): '))
pessoa['Idade'] = (datetime.now().year - pessoa['Ano do Nascimento'])

print('=-=' * 15)

if pessoa['Carteira de Trabalho'] != 0:
    pessoa['Ano da Contratacao'] = int(input('Ano de Contratação: '))
    pessoa['Salario'] = float(input('Salário: R$'))
    pessoa['Idade da Aposentadoria'] = pessoa['Idade'] + ((pessoa['Ano da Contratacao'] + 35) - datetime.now().year)

# output
print('=-=' * 15)
for k, v in pessoa.items():
    print(f'{k}: {v}')
    


