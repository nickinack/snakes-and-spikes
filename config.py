import pygame
import time


pygame.init()


#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (124,252,0)
BLUE = (0,0,255)
BROWN = (218,165,32)

#UserEvents
create_mobs = pygame.USEREVENT + 1
player_turn = pygame.USEREVENT + 2
score_down = pygame.USEREVENT + 3

#Music
pygame.mixer.music.load('subway.mp3')
pygame.mixer.music.play(-1)

#font
myfont = pygame.font.SysFont('comicsans', 18)

#Text Surfaces (Remain COnstant entire time)
textsurface_1 = myfont.render('Player1s turn', False, (255, 255, 255))
textsurface_2 = myfont.render('Player2s turn', False, (255, 255, 255))
