def area(largura, comprimento):
    print(f'\nA área de um terreno de {largura:.1f}x{comprimento:.1f} é de {(largura*comprimento):.2f}m²')
    print('=-=' * 15)


print('\033[36;40mExercício Python #096​ - Função que calcula área\033[m')
print('=-=' * 15)

largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
area(largura, comprimento)
