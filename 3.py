import pygame
import os
import random

pygame.init()
size = x, y = 1280, 720
running = True
count = 0
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))


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


class Space(pygame.sprite.Sprite):
    image = load_image("space1.jpg")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Space.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = y

    def background(self):
        if count == 750:
            image = load_image("space2.jpg")
        if count == 1500:
            image = load_image("space3.jpg")
        if count == 2250:
            image = load_image("space4.jpg")


clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
space = Space()


class Laser(pygame.sprite.Sprite):
    image = load_image("laser.png", -1)

    def __init__(self, pos1):
        super().__init__(all_sprites)
        self.image = Laser.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos1[0]
        self.rect.y = pos1[1]

    def update(self):
        self.rect = self.rect.move(0, -1)
        if not pygame.sprite.collide_mask(self, space):
            self.rect = self.rect.move(1, 1)


class Meteor(pygame.sprite.Sprite):
    image = load_image("meteor.jpg", -1)

    def __init__(self, pos2):
        super().__init__(all_sprites)
        self.image = Meteor.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos2[1280]
        self.rect.y = pos2[720]

    def asteroid(self):
        if count == 1500:
            image = load_image("meteor1.jpg")


meteor = Meteor()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Laser(event.pos)
        if x.pos1[0] and y.pos1[1] == x.pos2[1280] and y.pos2[720]:
            count += 1
            image = load_image("boom.png")
            meteor.pop
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(100)
pygame.quit()