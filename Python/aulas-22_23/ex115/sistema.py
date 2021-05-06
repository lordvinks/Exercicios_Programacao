from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'ex115.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair do Sistema']) 
    if resposta == 1:
        # Opção de listar conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))    
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
    else:       
        print('\033[31mERRO: por favor, digite um valor válido!\033[m')
    sleep(2)