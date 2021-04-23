def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    for cont, item in enumerate(lista):
        print(f'{cont+1} - {item}')
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um valor válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsúario prefiriu não digitar algo!\033[m')
            continue
        else:
            return n