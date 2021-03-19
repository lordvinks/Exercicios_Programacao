print('\033[36;40mExercício Python #060 - Cálculo do Fatorial\033[m')
print('')
num = int(input('DIGITE UM NÚMERO: '))
c = num
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
