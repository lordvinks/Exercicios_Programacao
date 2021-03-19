print(' \033[36;40mExercício Python #070 - Estatísticas em produtos\033[m') 

#Iniciando variáveis
totalGastos = maiorQueMil = menorPreco = cont = 0
nomeProdutoBarato = ""

while True:
    
    print('=-=' * 20)
    nomeProduto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    totalGastos += preco

    #CONDIÇÕES
        #Mais barato
    if cont == 0:
        menorPreco = preco
        nomeProdutoBarato = nomeProduto
        cont = 1
    elif menorPreco > preco:
        menorPreco = preco
        nomeProdutoBarato = nomeProduto

        # Quant. maior que R$1000,00
    if preco > 1000:
        maiorQueMil += 1

    # Ver se o usuario quer continuar
    continuar = str(input('Deseja continuar (S/N): ')).strip().lower()

    if continuar[0:1] == 'n':
        print('=-=' * 20)
        break
    
print(f'O cliente gastou no total R${totalGastos:.2f}')
print(f'O cliente comprou {maiorQueMil} produto(s) com um valor maior que R$1000,00')
print(f'O produto com menor valor foi um(a) {nomeProdutoBarato}. Custando R${menorPreco}')


    
        
    
    
        
    
