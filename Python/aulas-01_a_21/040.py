print('\033[36;40m Exercício Python #040 - Aquele clássico da Média\033[m')
print('')
nota1 = float(input('\033[33m Primeira nota: '))
nota2 = float(input(' Segunda nota: \033[m'))
media = (nota1 + nota2) / 2
print('')
# Aprovado
if media > 7.0:
    print('\033[32m Tirando {} e {}, a média é {}. O aluno está aprovado!\033[m'.format(nota1, nota2, media))
elif 7 > media >= 5.0:
    print('\033[34m Tirando {} e {}, a média é {}. O aluno está de Recuperação!\033[m'.format(nota1, nota2, media))
else:
    print('\033[31m Tirando {} e {}, a média é {}. O aluno está de Recuperação!\033[m'.format(nota1, nota2, media))
