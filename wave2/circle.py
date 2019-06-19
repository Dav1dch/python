import pygame
import threading
import time
from pygame.locals import *

lock = threading.Lock()
class circle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('/image/circle.png')
        self.image2 = self.image
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
            self.image = pygame.transform.scale(self.image, (int(orign_size), int(orign_size)))
            orign_size += 6
            clock.tick(20)
            print(self.image2.get_alpha())
            screen.blit(self.image, (x, y))
            x -= 3
            y -= 3

