from time import sleep
# cod de cores
endc = '\033[m'
cor = {'end': '\033´m',
       'titled': '\033[35;40m',
       'red': '\033[31m',
       'green': '\033[32m',
       'yellow': '\033[33m',
       'blue': '\033[34m',
       'Purple': '\033[35m',
       'lblue': '\033[36m',
       'gray': '\033[37m'}
print(('{} Exercício Python #036 - Aprovando Empréstimo{}'.format(cor['titled'], endc)))
print('=-=' * 18)
# Começo
vcasa = float(input('\033[33mQual o valor da casa que deseja comprar? '))
vsal = float(input('\033[33mQual o valor do salário? '))
apag = float(input('\033[33mEm quantos anos quer dividir o pagamento? '))
print('\033[31mAGUARDE...')
sleep(2)
# Calculo salário
mes = vcasa / (12 * apag)
sa = (mes * 100) / vsal
# Empres. sucedido
if sa < 30:
    print('\033[34mParabéns, o seu empréstimo no valor de {:.1f} foi aprovado!'.format(vcasa))
    sleep(1)
    print('\033[34mEle custará R${:.1f}/més, o valor corresponde a {:.1f}% de seu salário/més.'.format(mes, sa))
    print('=-=' * 20)
# Empres. mal sucedido
else:
    print('\033[31mDesculpa, mas o valor de R${:.1f}/més corresponde a {:.1f}% a mais que 30% de seu salário!'.format(mes, (sa - 30)))
print('')
sleep(10)
print('\033[36m=-=' * 20)
print('\033[35mThe End')
print('\033[36m=-=\033[m' * 20)

