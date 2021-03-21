def metade(num):
    return 'R${}'.format(num / 2)

def dobro(num):
    return 'R${}'.format(num * 2)

def aumentar(num, p=0):
    return 'R${}'.format(num + ((num * p) / 100))

def diminuir(num, p=0):
    return 'R${}'.format(num - ((num * p) / 100))