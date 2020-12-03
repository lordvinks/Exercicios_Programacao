from datetime import date
a = int(input('Diga um ano. Aperte 0 caso queira análisar o ano atual: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 !=0 or a % 400 == 0:
    print('O ano {} é BISSEXTO'.format(a))
else:
    print('O ano {} não é BISSEXTO'.format(a))
