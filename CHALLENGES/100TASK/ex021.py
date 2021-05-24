#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame


print('-*-'*30)
print('PLAYER DE MÚSICA')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

pygame.init()
pygame.mixer.music.load('ex021.mp3')