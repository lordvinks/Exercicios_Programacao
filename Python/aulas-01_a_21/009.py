print('\033[36;40mExercício Python #009 - Tabuada\033[m')
from time import sleep
a4 = int(input('\033[31mNumero: '))
print('=-=' * 20)
print('CALCULANDO...')
sleep(1)
print('=-=' *20)
n1 = a4 * 1
n2 = a4 * 2
n3 = a4 * 3
n4 = a4 * 4
n5 = a4 * 5
n6 = a4 * 6
n7 = a4 * 7
n8 = a4 * 8
n9 = a4 * 9
n10 = a4 * 10
print('\033[33m|         ={}=       '.format(n1))
print('|        =={}== '.format(n2))
print('|       ==={}=== '.format(n3))
print('|      ===={}===='.format(n4))
print('|     ====={}=====  '.format(n5))
print('|    ======{}====== '.format(n6))
print('|   ======={}======= '.format(n7))
print('|  ========{}======== '.format(n8))
print('| ========={}========= '.format(n9))
print('|=========={}=========='.format(n10))
