print('\033[36;40mExercício Python #073 - Tuplas com Times de Futebol\033[m')

brasileirao = ('São Paulo', 'Atlético-MG', 'Flamengo', 'Internacional', 'Grêmio', 'Palmeiras', 'Fluminense', 'Santos', 'Corinthians', 'Ceará',
               'Athletico-PR', 'Atlético-GO', 'Bragantino', 'Fortaleza', 'Sport Recife', 'Bahia',
               'Vasco da Gama', 'Goiás', 'Botafogo', 'Coritiba')

print('\nOs cinco primeiros colocados do Brasileirão 2020-21'.upper())
for cont in range(0, 5):
    print(f'{cont+1}ª: {brasileirao[cont]:-^49}')

print('=-=' * 18)

print('\nOS QUATRO ÚLTIMOS COLOCADOS DO BRASILEIRÃO 2020-21')
for cont in range(16, len(brasileirao)):
    print(f'{cont+1}ª: {brasileirao[cont]:-^49}')

print('=-=' * 18)

print('\nCLASSIFICAÇÃO DOS TIMES DO BRASILEIRÃO 2020-21')
timesOrg = sorted(brasileirao)

for cont, time in enumerate(timesOrg):
    print(f'{cont+1}ª: {brasileirao[cont]:-^49}')

