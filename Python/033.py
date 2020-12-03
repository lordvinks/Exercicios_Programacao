a = float(input('Diga um número: ').strip())
b = float(input('Diga mais um: ').strip())
c = float(input('Diga outro: ').strip())
# Verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c4
# Verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor é digitado foi {}'.format(maior))
print('O menor digitado foi {}'.format(menor))