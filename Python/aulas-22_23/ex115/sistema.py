from lib.interface import *
from time import sleep

while True:
    resposta = menu(['Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        print()
    elif resposta == 2:
        print()
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
    else:       
        print('\033[31mERRO: por favor, digite um valor válido!\033[m')
    sleep(2)