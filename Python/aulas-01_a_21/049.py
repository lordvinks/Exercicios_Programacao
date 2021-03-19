print(' \033[36;40mExercício Python #049 - Tabuada v.2.0\033[m')
print('=' * 39)
s = 0
t = 0
ml = 0
m = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    s = s + 1
    ml = m * s
    print('{} x {} = {}'.format(m, s, ml))
print('=' * 39)
# Uma outra Estação
num = int(input('Digite um número para ver sua tabuada: '))
for l in range(1, 11):
    print('{} x {:2} = {}'.format(num, l, num*l))
