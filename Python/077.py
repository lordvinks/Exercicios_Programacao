print('Exercício Python #077 - Contando vogais em Tupla\n')

# Tuplas
vogais = ('A', 'E', 'I', 'O', 'U')
palavras = ('CASA', 'PROGRAMAR', 'TREM', 'PYTHON', 'FUTURO', 'CARRO', 'LIXO')

# Loop FOR para as palavras
for palavra in palavras:
    vogaisEncontradas = ''
    cont = 0

    # Loop FOR para as vogais
    for vogal in vogais:
        cont = palavra.count(vogal)
        
        #Loop FOR para concatenar as vogais encontradas
        for i in range(0, cont):
            vogaisEncontradas += vogal + ', '

    #output  
    print(f'Na palavra {palavra} foram encontradas as seguintes vogais: {vogaisEncontradas.strip()[:len(vogaisEncontradas)-2]}')

