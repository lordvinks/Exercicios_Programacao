print('{}Exercício Python #002 - Respondendo ao Usuário{}'.format('\033[0;31;40m', '\033[m'))
nome = str(input('{}Qual é o seu nome? {}'.format('\033[33m', '\033[m'))).title().strip()
print('{}É um prazer lhe conhecer,{} {}{}{}.'.format('\033[33m', '\033[m', '\033[4;35m', nome, '\033[m'))
