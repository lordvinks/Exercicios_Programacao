print('\033[36;40mExercício Python #038 - Comparando números\033[m')
from time import sleep
num1 = float(input('\033[33mDigite um valor: '))
num2 = float(input('Digite outro: \033[m'))
print('\033[31mPROCESSANDO...')
sleep(1)
if num1 < num2:
    print('\033[36m O número {} é maior que o número {}'.format(num2, num1))
elif num1 > num2:
    print('\033[36m O número {} é maior que o número {}'.format(num1, num2))
else:
    print('\033[36m O número {} e {} são iguais'.format(num1, num2))
