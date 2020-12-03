print('Exercício Python #018 - Seno, Cosseno e Tangente')
import math
a = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(a))
print('Sen = {:.2f}'.format(sen))
cos = math.cos(math.radians(a))
print('Cos = {:.2f}'.format(cos))
tg = math.tan(math.radians(a))
print('Tg = {:.2f}'.format(tg))