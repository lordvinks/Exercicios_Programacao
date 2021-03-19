print('Exercício Python #029 - Radar eletrônico')
print('-=-' * 20)
v = float(input('Por favor, me informe a velocidade (em Km/h): '))
if v <= 80:
    print('O carro está respeitando o limide')
else:
    m = (v - 80) * 7
    print('O carro não está respeitando o limite, por isso será multado no valor de R${:.1f}!'.format(m))
