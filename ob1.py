#!/usr/bin/env python
#_*_coding:utf-8-*-

import pygame, sys
from pygame.locals import *

Altura=480
Ancho= 640

class dialog():
    def __init__(self):
        dialog=pygame.display.set_mode((50,50))
        pygame.display.set_caption("Dialogo")

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()


class Bola(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("ball.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = Ancho / 2
        self.rect.centery = Altura / 2
        self.speed = [0.2, -0.2]

    def Actualizar(self, time):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time
        if self.rect.left <= 0 or self.rect.right >= Ancho:
            self.speed[0] = -self.speed[0]
            self.rect.centery += self.speed[0]*time
        if self.rect.top <= 0 or self.rect.bottom >= Altura:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1]*time

def load_image(name, transparent = False):
    try:
        image = pygame.image.load(name)
    except pygame.error, message:
        raise SystemExit, message
    image = image.convert()
    if transparent:
        color = image.get_at((0,0))
        image.set_colorkey(color, RLEACCEL)
    return image

def keys_press():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        sys.exit(0)


def event():
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)

def main():
    screen = pygame.display.set_mode((Ancho,Altura))
    pygame.display.set_caption("Juego")
    pygame.display.set_icon(pygame.image.load('camara.gif'))
    background_image = pygame.image.load("textura.jpg")
    bola = Bola()

    clock =pygame.time.Clock()

    while True:
        time = clock.tick(60)
        keys_press()
        event()
        bola.Actualizar(time)
        screen.blit(background_image, (0,0))
        screen.blit(bola.image, bola.rect)
        pygame.display.flip()
    return 0

if __name__ == "__main__":
    pygame.init()
    main()
