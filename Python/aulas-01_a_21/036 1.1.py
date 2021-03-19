from time import sleep
print(('Exercício Python #036 - Aprovando Empréstimo'))
print('=-=' * 18)
# Troca de moedas
p = str(input('Deseja trocar de moeda (sim ou não)? ').strip().title())
# Se sim
if p == 'Sim':
    nm = str(input('Qual moeda deseja (simbolo)? Se for dollar digite 1. Se for euro 2: '.strip().upper()))
    if nm == '2':
        m = '€'
    elif nm == '1':
        m = '$'
# Se não
else:
    print('A moeda padrão do sistema é o Real')
    m = 'R$'
# Perguntas
vcasa = float(input('Qual o valor da casa que deseja comprar? '))
vsal = float(input('Qual o valor do salário? '))
pmes = str(input('Você prefere dar o valor em ano ou mês? ').lower().strip())
# Escolher mês
if pmes == 'mês':
    apag = float(input('Em quantos meses quer dividir o pagamento? '))
    #Calculo em mês
    mes = vcasa / apag
    sa = (mes * 100) / vsal
    if apag > 1:
        t = 'meses'
    else:
        t = 'mês'
elif pmes == 'ano':
    apag = float(input('Em quantos anos quer dividir o pagamento? '))
    # Calculo em ano
    mes = vcasa / (apag * 12)
    sa = (mes * 100) / vsal
    if pmes > 1:
        t = 'anos'
    else:
        t = 'ano'
print('AGUARDE...')
sleep(2)
# Empres. sucedido
if sa < 30:
    print('Parabéns, o seu empréstimo no valor de `{}{:.1f} foi aprovado!'.format(m, vcasa))
    sleep(1)
    print('Ele custará {}{:.1f}/més, o valor corresponde a {:.1f}% de seu salário/més.'.format(m, mes, sa))
    print('=-=' * 20)
else:
    print('Desculpa, mas o valor de {}{:.1f}/més corresponde a {:.1f}% a mais que 30%'.format(m, mes, sa))
sleep(3)
print('=-=' * 20)
print('The End')
print('=-=' * 20)

