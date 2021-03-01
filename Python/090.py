print('\033[36;40mExercício Python #090 - Dicionário em Python\033[m')


aluno = dict()
print('=-=' * 10)

aluno['nome'] = str(input('Nome: ')).capitalize().strip()
aluno['nota 01'] = float(input('Nota 01: '))
aluno['nota 02'] = float(input('Nota 02: '))

print('=-=' * 10)

aluno['media'] = (aluno['nota 01'] + aluno['nota 02']) / 2
if aluno['media'] >= 7:
    aluno['situação'] = 'aprovado'
else:
    aluno['situação'] = 'reprovado'

for keys, values in aluno.items():
    print(f'{keys.capitalize()}: {values}')
