print('\033[36m='*12, '\033[31mPlayer de Musicas', '\033[36m='*12)
'''import playsound
playsound.playsound('musica.mp3')'''

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('loc.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()):pass
