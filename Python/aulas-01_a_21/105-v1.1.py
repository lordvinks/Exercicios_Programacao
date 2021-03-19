def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r[média] >= 6:
            r['situação'] = 'boa'
        else:
            r['situação'] = 'ruim'
    
    return r


print('\033[36;40mEExercício Python #105​ - Analisando e gerando Dicionários\033[m')

resp = notas(5.5, 2.5, 8.5, True)
print(resp)