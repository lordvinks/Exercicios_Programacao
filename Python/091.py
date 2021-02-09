from random import randint

numPlayer = dict()
ordem = [[], [], [], [] ]

print('=-=' * 20)

for i in range(0, 4):
    ordem[i].append(randint(1, 100))
    ordem[i].append('jogador {}'.format(i+1))

    print('JOGADOR 0{}: {}'.format(i+1, ordem[i][0]))

ordem.sort(reverse=True)

print('=-=' * 20)

for j in range(0, 4):
    numPlayer[ordem[j][1]] = ordem[j][0]
    print(f'{j+1}: {ordem[j][1]} com {ordem[j][0]} pontos')
