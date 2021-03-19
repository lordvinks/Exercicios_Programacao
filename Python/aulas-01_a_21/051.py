print(' \033[36;40mExercício Python #051 - Progressão Aritmética\033[m')
print('=' * 47)
pt = int(input(' Primeiro Termo: '))
r = int(input(' A Razão: '))
d = pt + (10 - 1) * r
s = 0
for c in range(pt, d + r, r):
    print(c, end=' -> ')
print('The end')
