print('Exercício Python #017 - Catetos e Hipotenusa')
co = float(input('Qual o comprimento do C.O? ').strip())
ca = float(input('Qual o comprimeto do C.A? ').strip())
h = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa é {:.2f}'.format(h))

