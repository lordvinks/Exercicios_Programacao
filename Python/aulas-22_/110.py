from pacotes import ex110

print('\033[36;40mExercício Python #110​ - Reduzindo ainda mais seu programa\033[m\n')

v = float(input('Digite o preço: R$'))
porcentagemAumento = int(input('Qual será a procentagem de aumento? '))
porcentagemReducao = int(input('E qual a porcentagem de redução? '))

print('')

ex110.resumo(v, porcentagemAumento, porcentagemReducao)
