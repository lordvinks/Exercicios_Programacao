def leiaDinheiro(v=''):
    if v.isnumeric() == False:
        print(f'\n\033[1;31mERRO: "{v}" é um valor inválido\033[m')
        return False
    else:
        return True