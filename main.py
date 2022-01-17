import pygame
from os import listdir
from os.path import isfile, join

def next_sprite(x):
    mypath = 'Minotaur_01/PNG Sequences/Attacking/'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    x = x + 1
    if x >= len(onlyfiles):
        x=0
    img = pygame.image.load(join(mypath, onlyfiles[x]))
    img = pygame.transform.scale(img, (int(img.get_width() * 0.2), int(img.get_height() * 0.2)))
    rect = img.get_rect()
    rect.center = (100, 100)
    return (img, rect, x)

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Tim's shooter")

x1 = 0
run=True
while run:

    (img2, rect2, x1) = next_sprite(x1)
    screen.blit(img2, rect2)
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run= False
    pygame.display.update()