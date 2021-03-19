from time import sleep
d = float(input('Qual a distância (em km) que vai viajar? '))
print('PROCESSANDO...')
sleep(1)
if d <= 200:
    s = d * 0.50
    print('A sua viagem é de {:.1f}Km, por isso custará R${:.1f}'.format(d, s))
else:
    s1 = d * 0.45
    print('A sua viagem é de {:.1f}, por isso custara R${:.1f}'.format(d, s1))
