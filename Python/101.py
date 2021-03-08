def voto(anoNascimento):
    idade = datetime.now().year - anoNascimento
    print('=-=' * 15)
    print(f'\nVocê tem {idade} ano(s)')

    if idade < 16:
        return 'NEGADO'
    elif 16 <= idade < 18 or idade >= 70:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'


from datetime import datetime

print('\033[36;40mExercício Python #101​ - Funções para votação\033[m\n')


print('=-=' * 15)
situação = voto(int(input('Em que ano você nasceu? ')))

print(f'Situação em relação ao voto: {situação}\n')
print('=-=' * 15)

