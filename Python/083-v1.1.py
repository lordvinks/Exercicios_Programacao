print('\033[36;40mExercício Python #083 - Validando expressões matemáticas 1.1\033[m')

print('=-=' * 20)
expressao = str(input('Digite uma expressão matemática: '))
print('=-=' * 20)

if (expressao.find('(') + expressao.find(')') + 1) >= 0:
    pilha = list()

    for simb in expressao:
        if simb == '(':
            pilha.append('(')
        elif simb == ')':
            if len(pilha) > 0:
                pilha.pop()
        else:
            pilha.append(')')
            break
    if len(pilha) == 0:
        print('Sua expressão está válida!')
    else:
        print('Sua expressão está inválida!')
else:
    print('\nNão há parênteses na expressão digitada!')
