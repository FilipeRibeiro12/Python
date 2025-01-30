import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
'''pygame.event.wait() ----- não funciona'''
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)