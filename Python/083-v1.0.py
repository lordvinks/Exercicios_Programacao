print('\033[36;40mExercício Python #083 - Validando expressões matemáticas\033[m')

print('=-=' * 20)
expressao = str(input('Digite uma expressão matemática: '))
print('=-=' * 20)

if (expressao.find('(') + expressao.find(')') + 1) >= 0:
    quantParenteses01 = quantParenteses02 = 0

    for i in range(0, len(expressao)):
        if expressao[i] == ')':
            quantParenteses01 += 1
        elif expressao[i] == '(':
            quantParenteses02 += 1

    if (quantParenteses02+quantParenteses01) % 2 == 0 and quantParenteses02 > 0 and quantParenteses01 > 0:
        print('Os parênteses da expressão estão corretos!')
    else:
        print('Os parênteses da expressão estão incorretos!')

else:
    print('\nNão há parênteses na expressão digitada!')
