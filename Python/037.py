print('\033[35;40mExercício Python #037 - Conversor de Bases Numéricas\033[m')
from time import sleep
print('-=-' * 20)
# Perguntar o número
num0 = int(input('\033[33mDigite um número decimal inteiro: ').strip())
sleep(2)
# Escolher o formato que o user quer converter
c = str(input('''\033[37mDigite...
 \033[35m|1| Binário: 
 \033[32m|2| Octal: 
 \033[34m|3| Hexadedecimal:
 \033[36mR:\033[m ''').strip())
print('=-=' * 20)
sleep(2)
# Binario
if c == '1':
    print('\035[33m O número {} convertido para binário é igual a {}'.format(num0, bin(num0)[2:]))
# octal
elif c == '2':
    print('\033[32m O número {} convertido para octal é igual a {}'.format(num0, oct(num0)[2:]))
# Hexadedecimal
elif c == '3':
    print('\033[34m O número {} convertido para Hexadedecimal é igual a {}'.format(num0, hex(num0)[2:]))
# Doente mental
else:
    print('\033[31mOpção invalida. Tente novamente!!!')