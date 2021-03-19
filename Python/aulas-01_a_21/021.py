print('Exercício Python #021 - Tocando um MP3')
import pygame
a = input('NomeDaMúsica: ')
pygame.mixer.init()
pygame.base.init()
pygame.mixer.music.load('add\músicas\{}.mp3'.format(a))
pygame.mixer.music.play()
pygame.event.wait()