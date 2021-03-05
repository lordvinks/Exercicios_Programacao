from time import sleep

def maiorValor(* num):
    print('=-=' * 15)

    maior = cont = 0
    for valor in num:
        print(valor, end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1

    print(f'\nForam informados {cont} ao todo\nO maior deles é o valor {maior}')

        
maiorValor(2, 9, 4, 5, 7, 1)
maiorValor(4, 7, 0)
maiorValor(1, 2)
maiorValor(6)
maiorValor()