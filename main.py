import pygame
from os import listdir
from os.path import isfile, join
from random import randint

def next_sprite(sprite, position_x, position_y ):
    mypath = 'Minotaur_01/PNG Sequences/Attacking/'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    sprite = sprite + 1
    if sprite >= len(onlyfiles):
        sprite=0
    img = pygame.image.load(join(mypath, onlyfiles[sprite]))
    img = pygame.transform.scale(img, (int(img.get_width() * 0.2), int(img.get_height() * 0.2)))
    rect = img.get_rect()
    rect.center = (position_x, position_y )
    return (img, rect, sprite)

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Tim's shooter")
pos_x = 200
pos_y = 200
x1 = 0
run=True
while run:
    pos_x = pos_x + (randint(-5, 5))
    pos_y = pos_y + (randint(-5, 5))
    if (pos_x > 800):  pos_x = 800
    if (pos_x < 0):  pos_x = 0
    if (pos_y > 800): pos_y = 800
    if (pos_y < 0): pos_y = 0

    (img2, rect2, x1) = next_sprite(x1, pos_x, pos_y)
    screen.blit(img2, rect2)
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run= False
    pygame.display.update()