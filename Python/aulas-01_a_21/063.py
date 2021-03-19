print(' \033[36;40mExercício Python #063 - Sequência de Fibonacci v1.0\033[m')
print('__' * 19)

seq = int(input(' Quantos termos você quer mostrar? '))
seq = seq - 2

print('__' * 19)

cont = 0
t1 = 0
t2 = 1
t3 = 0

if seq == -1:
    print(t1, end=' -> ')

elif seq == 0:
    print(' {} -> {}'.format(t1, t2), end=' -> ')

elif seq != 0 or seq != -1:
    print('{} -> {} '.format(t1, t2), end='->')

    while cont < seq:
        t = t1 + t2
        print(' {} '.format(t), end='->')
        t1 = t2
        t2 = t
        cont += 1

print(' FIM')
