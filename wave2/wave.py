import pygame
import sys
import time
import threading
import random
import os
import circle
from pygame.locals import *


# init pygame
pygame.init()
# set background color
BACKGROUNDCOLOR = (255, 200, 255)
# set background size
BACKGOUNDSIZE = width, height = (800, 600)
# set background
pygame.display.set_mode(BACKGOUNDSIZE)
# set window's title
pygame.display.set_caption("Wave Game")
# get surface to screen
screen = pygame.display.get_surface()
# load circle image
clock = pygame.time.Clock()


def run():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        # mouse click
        mouse_press = pygame.mouse.get_pressed()
        # keboard click
        key_press = pygame.key.get_pressed()
        screen.fill((255, 0, 255))
        if mouse_press[0]:
            if threading.active_count() < 20:
                thread_circle = threading.Thread(
                    target=circle(screen), args=(screen,))
                thread_circle.start()
        # set clock
        clock.tick(20)
        pygame.display.update()


lock = threading.Lock()


class circle(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r"/Users/david/Documents/code/python/wave/circle.png")
        self.image2 = self.image
        orign_size = 200
        x, y = pygame.mouse.get_pos()
        x -= orign_size / 2
        y -= orign_size / 2
        image_alpha = 255
        clock = pygame.time.Clock()
        while image_alpha > 1:
            self.image = self.image2
            image_alpha *= 0.95
            self.image.set_alpha(image_alpha)
            self.image = pygame.transform.scale(
                self.image, (int(orign_size), int(orign_size)))
            orign_size += 6
            clock.tick(20)
            print(self.image2.get_alpha())
            screen.blit(self.image, (x, y))
            x -= 3
            y -= 3

    def draw_image(self, screen):
        orign_size = 200
        x, y = pygame.mouse.get_pos()
        x -= orign_size / 2
        y -= orign_size / 2
        image_alpha = 255
        clock = pygame.time.Clock()
        while image_alpha > 1:
            self.image = self.image2
            image_alpha *= 0.95
            self.image.set_alpha(image_alpha)
            self.image = pygame.transform.scale(
                self.image, (int(orign_size), int(orign_size)))
            orign_size += 6
            clock.tick(20)
            print(self.image2.get_alpha())
            screen.blit(self.image, (x, y))
            x -= 3
            y -= 3


run()
