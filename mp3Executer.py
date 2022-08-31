import pygame

pygame.init()
pygame.mixer.music.load('undertale.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.08)
pygame.event.wait()
input()