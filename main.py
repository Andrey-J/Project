import pygame
import os
import random


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
size = x, y = 800, 600
count = 0
running = True
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))


class Space(pygame.sprite.Sprite):
    image = load_image("space.jpg")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Space.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = y

    def background(self):
        if count == 1000:
            image = load_image("space1.jpg")


clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
space = Space()


class Spacecraft(pygame.sprite.Sprite):
    image = load_image("spacecraft.jpg", -1)

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = Spacecraft.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos1[0]
        self.rect.y = pos1[1]

    def update(self):
        self.rect = self.rect.move(0, -1)
        if not pygame.sprite.collide_mask(self, space):
            self.rect = self.rect.move(1, 1)

    def sgip(self):
        if count == 500:
            image = load_image("spacecraft1.jpg")
        if count == 1500:
            image = load_image("spacecraft3.jpg")

            
class Meteor(pygame.sprite.Sprite):
    image = load_image("meteor.jpg", -1)
    
    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = Meteor.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos2[]
        self.rect.y = pos2[]

    def asteroid(self):
        if count == 1500:
            image = load_image("meteor1.jpg")


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Spacecraft(event.pos)
        if x.pos1[] and y.pos1[] == x.pos2[] and y.pos2[]:
            count += 1
            meteor.pop
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(100)
pygame.quit()