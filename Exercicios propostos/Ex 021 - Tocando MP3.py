import pygame

pygame.init()
pygame.mixer.music.load('Ex021.mp3.mp3')
pygame.mixer.music.play()
stop = ''
print('Pressione uma tecla para parar')
while stop == '' :
    stop = input()

pygame.event.wait()
