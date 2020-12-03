print('Exercício Python #025 - Procurando uma string dentro de outra')
print('By Guanabara')
name = str(input('Qual é o seu nome? ')).title().strip()
print('Seu nome tem Silva? {}'.format('Silva' in name))
