
import pygame
import os
import random

pygame.init()
size = x, y = 1280, 720
running = True
count = 0
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))


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


class SpaceCraft(pygame.sprite.Sprite):
    image = load_image('spacecraft.png', - 1)

    def __init__(self, group):
        super().__init__(group_sprites, group)
        self.image = SpaceCraft.image
        self.rect = self.image.get_rect()

    def get_event(self, pos):
        self.update(pos)

    def update(self, coords):
        self.rect.x, self.rect.y = coords


class Space(pygame.sprite.Sprite):
    image = load_image("space1.jpg")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Space.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = y


clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
group_sprites = pygame.sprite.Group()
space = Space()
SpaceCraft(group_sprites)


class Laser(pygame.sprite.Sprite):
    image = load_image("laser.png", -1)

    def __init__(self, pos1):
        super().__init__(all_sprites)
        self.image = Laser.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos1[0] + 73
        self.rect.y = pos1[1] - 50

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
        self.rect.x2 = pos2[1280]
        self.rect.y2 = pos2[720]

    def fall(self):
            for i in range(10):
                (random.random() * x,
                random.random() * y, 1, 1))
                
    def die(self):
        if self.rect.x2 == self.rect.x and self.rect.y2 == self.rect.y:
            os.kill(meteor)
        if self.rect.x2[0] and self.rect.y2[0]:
            os.kill(meteor)
        

    def update(self):
        self.rect = self.rect.move(0, 1)
        if not pygame.sprite.collide_mask(self, space):
            self.rect = self.rect.move(1, 1)


while running:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Laser(event.pos)
        if event.type == pygame.MOUSEMOTION:
            for i in group_sprites:
                if pygame.mouse.get_focused():
                    i.get_event(event.pos)
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    group_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(100)
    clock.tick(10000)

pygame.quit() 
