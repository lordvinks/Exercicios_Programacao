import requests


def verSiteOnline(link=''):
    if link == '':
        link = 'http://pudim.com.br/'
    
    print('')

    try:
        requisicao = requests.get(link)
    except:
        print(f'\033[1;31mERRO: o site "{link}" está fora do ar\033[m\n')
    else:
        print(f'\033[1;32mO site "{link}" está online\033[m\n')


print('\033[36;40mExercício Python #113​ - Funções aprofundadas em Python\033[m\n')

verSiteOnline(str(input('Digite o link do site: ')).strip())

