import pygame
from os import listdir
from os.path import isfile, join
from random import randint

class sprite:
    def __init__(self, path, x, y, xmin, xmax, ymin, ymax, scaleing):
        self.path = path
        self.x = x
        self.y = y
        (self.xmin, self.xmax, self.ymin, self.ymax) = (xmin, xmax, ymin, ymax)
        self.onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        img = pygame.image.load(join(path, self.onlyfiles[0]))
        img = pygame.transform.scale(img, (int(img.get_width() * 0.2), int(img.get_height() * 0.2)))
        rect = img.get_rect()
        rect.center = (x, y)
        self.img = img
        self.rect = rect
        self.sprite = 0

    def defineboundaries (xmin, xmax, ymin, ymax):
        (xmin, xmax, ymin, ymax) = (xmin, xmax, ymin, ymax)

    def setposition(x,y):
        pass
    def iteratesprite(self):
        self.sprite += 1
        if self.sprite >= len(self.onlyfiles):
            self.sprite = 0
        #onlyfiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        img = pygame.image.load(join(self.path, self.onlyfiles[self.sprite]))
        img = pygame.transform.scale(img, (int(img.get_width() * 0.2), int(img.get_height() * 0.2)))
        rect = img.get_rect()
        rect.center = (self.x, self.y)
        self.img = img
        self.rect = rect

   def move(self,  delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y
        if (self.x > self.xmax):  self.x = self.xmax
        if (self.y > self.ymax):  self.y = self.ymax
        if (self.x < self.xmin):  self.x = self.xmin
        if (self.y < self.ymin):  self.y = self.ymin


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
Minotaur = sprite('Minotaur_01/PNG Sequences/Attacking/', 200, 200, 0, 800, 0, 800, 1)




while run:
    #pos_x = pos_x + (randint(-5, 5))
    #pos_y = pos_y + (randint(-5, 5))
    #if (pos_x > 800):  pos_x = 800
    #if (pos_x < 0):  pos_x = 0
    #if (pos_y > 800): pos_y = 800
    #if (pos_y < 0): pos_y = 0
    #screen.blit(img2, rect2)
    #(img2, rect2, x1) = next_sprite(x1, pos_x, pos_y)
    Minotaur.iteratesprite()
    Minotaur.move(randint(-5, 5), randint(-5, 5))
    screen.blit(Minotaur.img, Minotaur.rect)
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run= False
    pygame.display.update()