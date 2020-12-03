print('Exercício Python #034 - Aumentos múltiplos')
from time import sleep
#Perguntar o salário
s = float(input('Qual é o seu salário? ').strip())
print('Processando...')
sleep(1)
print('=-=' * 20)
#Caso seja maior que R$1250
if s > 1250.00:
    regra3 = (10 * s) / 100
    aumento1 = s + regra3
    print('O funcionario terá um aumento de R${:.1f}, por isso passará a ganhar R${:.1f}'.format(regra3, aumento1))
#se menor que R51250
else:
    REGRA3 = (15 * s) / 100
    aumento2 = s + REGRA3
    print("O funcionario terá um aumento de R${:.1f}, por isso passará a ganhar R${:.1f}".format(REGRA3, aumento2))
sleep(5)
print('--'*20)
print('Tenha um Bom Dia')
sleep(1)
print('<><>' * 20)