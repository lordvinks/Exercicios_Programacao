print('\033[36;40 Exercício Python #043 - Índice de Massa Corporal\033[m')
from time import sleep
peso = float(input('\033[33mQual é o seu peso? '))
altura = float(input('Qual é a sua altura? \033[m'))
print('')
imc = peso / (altura * altura)
if 0.0 < imc < 18.5:
    print('\033[34m O seu peso é {}Kg. Você está ABAIXO DO PESO, pois o seu IMC = {}!!\033[m'.format(peso, imc))
if 18.5 <= imc < 25:
    print('\033[34m O seu peso é {}Kg. Você está no PESO IDEAL, pois o seu IMC = {}!!\033[m'.format(peso, imc))
if 25 <= imc < 30:
    print('\033[34m O seu peso é {}Kg. Você está SOBREPESO!, pois o seu IMC = {}!!\033[m'.format(peso, imc))
if 30 <= imc < 40:
    print('\033[34m O seu peso é {}Kg. Você está com OBESIDADE, pois o seu IMC = {}!!\033[m'.format(peso, imc))
if 40 <= imc:
    print('\033[34m Seu peso é {}Kg. Você está com OBESIDADE MÓBIDA, pois o seu IMC = {:.1f}!!\033[m'.format(peso, imc))
if imc <= 0:
    print('\033[31mVocê tem certeza que digitou o valor correto?\033[m')