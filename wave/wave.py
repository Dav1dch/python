import pygame
import sys
import time
import random
from draw import *
from pygame.locals import *


# init pygame
pygame.init()
# set background color
BACKGROUNDCOLOR = (57, 148, 213)
# set background size
BACKGOUNDSIZE = width, height = (1000, 1000)
# set background
pygame.display.set_mode(BACKGOUNDSIZE)
# set window's title
pygame.display.set_caption("Wave Game")
# get surface to screen
screen = pygame.display.get_surface()
# load circle image
clock = pygame.time.Clock()



def run_mouse():
    screen.fill(BACKGROUNDCOLOR)
    image_array = []
    mouse_text = pygame.image.load('python/wave/image/mouse.png')
    random_text = pygame.image.load('python/wave/image/random.png')
    for i in range(10):
        image_array.append(draw())
    image = pygame.image.load('python/wave/image/circle3.png')
    while True:
        clock.tick(60)
        screen.blit(mouse_text, (800, 800))
        screen.blit(random_text, (800, 900))
        # print(pygame.event.get())
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if(951 > x > 800) and (976 > y > 900):
                    print('random')
                    run_random()
                for index, object in enumerate(image_array):
                    if(object.life == 0):
                        object.set_position(x, y)
                        break

        for index, object in enumerate(image_array):

            if object.life > 80:
                object.tscale(3)
                screen.blit(object.image, (object.x, object.y))
                object.life -= 1
                continue

            elif object.life > 70:
                object.tscale(2)
                screen.blit(object.image, (object.x, object.y))
                object.life -= 1
                continue
            elif object.life > 45:
                object.tscale(1)
                object.tscale2(3)
                screen.blit(object.image, (object.x, object.y))
                screen.blit(object.image2, (object.x2, object.y2))
                object.life -= 1
                continue

            elif object.life > 40:
                object.tscale(1)
                object.tscale2(2)
                object.tscale3(3)
                screen.blit(object.image, (object.x, object.y))
                screen.blit(object.image2, (object.x2, object.y2))
                screen.blit(object.image3, (object.x3, object.y3))
                object.life -= 1
                continue

            elif object.life > 1:
                object.tscale(1)
                object.tscale3(2)
                object.tscale2(1)
                screen.blit(object.image, (object.x, object.y))
                screen.blit(object.image2, (object.x2, object.y2))
                screen.blit(object.image3, (object.x3, object.y3))
                object.life -= 1
                continue

            if object.life == 1:
                object.reset()

        pygame.display.update()
        screen.fill(BACKGROUNDCOLOR)


def run_random():
    screen.fill(BACKGROUNDCOLOR)
    image_array = []
    mouse_text = pygame.image.load('python/wave/image/mouse.png')
    random_text = pygame.image.load('python/wave/image/random.png')
    for i in range(10):
        image_array.append(draw())
    image = pygame.image.load('python/wave/image/circle3.png')
    while True:
        clock.tick(30)
        screen.blit(mouse_text, (800, 800))
        screen.blit(random_text, (800, 900))
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if(951 > x > 800) and (876 > y > 800):
                    print('mouse')
                    run_mouse()
        flag = random.randint(0, 100)
        if(flag % 10 == 0):
            x = random.randint(0, 1000)
            y = random.randint(0, 1000)
            for index, object in enumerate(image_array):
                if(object.life == 0):
                    object.set_position(x, y)
                    break

        for index, object in enumerate(image_array):

            if object.life > 80:
                object.tscale(3)
                screen.blit(object.image, (object.x, object.y))
                object.life -= 1
                continue

            elif object.life > 70:
                object.tscale(2)
                screen.blit(object.image, (object.x, object.y))
                object.life -= 1
                continue
            elif object.life > 45:
                object.tscale(1)
                object.tscale2(3)
                screen.blit(object.image, (object.x, object.y))
                screen.blit(object.image2, (object.x2, object.y2))
                object.life -= 1
                continue

            elif object.life > 40:
                object.tscale(1)
                object.tscale2(2)
                object.tscale3(3)
                screen.blit(object.image, (object.x, object.y))
                screen.blit(object.image2, (object.x2, object.y2))
                screen.blit(object.image3, (object.x3, object.y3))
                object.life -= 1
                continue

            elif object.life > 1:
                object.tscale(1)
                object.tscale3(2)
                object.tscale2(1)
                screen.blit(object.image, (object.x, object.y))
                screen.blit(object.image2, (object.x2, object.y2))
                screen.blit(object.image3, (object.x3, object.y3))
                object.life -= 1
                continue

            if object.life == 1:
                object.reset()

        pygame.display.update()
        screen.fill(BACKGROUNDCOLOR)


if __name__ == "__main__":
    run_mouse()
