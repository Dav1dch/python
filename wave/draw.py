import pygame


class draw():
    def __init__(self, *args, **kwargs):
        self.image = pygame.image.load(
            'python/wave/image/circle3.jpg')
        self.image2 = pygame.image.load(
            'python/wave/image/circle3.jpg')
        self.image3 = pygame.image.load(
            'python/wave/image/circle3.jpg')
        self.size = 0
        self.size2 = 0
        self.size3 = 0
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.image2 = pygame.transform.scale(
            self.image2, (self.size2, self.size2))
        self.image3 = pygame.transform.scale(
            self.image3, (self.size3, self.size3))
        self.x = 100
        self.y = 100
        self.x2 = 100
        self.y2 = 100
        self.x3 = 100
        self.y3 = 100
        self.life = 0
        self.alpha1 = 170
        self.alpha2 = 210
        self.alpha3 = 240
        self.image.set_colorkey((56, 148, 213))
        self.image2.set_colorkey((56, 148, 213))
        self.image3.set_colorkey((56, 148, 213))

    def tscale(self, x):
        self.image = pygame.image.load(
            'python/wave/image/circle3.jpg')
        self.size += x
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.x -= x / 2.0
        self.y -= x / 2.0
        self.image.set_colorkey((56, 148, 213))
        self.alpha1 *= 0.95
        self.image.set_alpha(self.alpha1)

    def tscale2(self, x):
        self.image2 = pygame.image.load(
            'python/wave/image/circle3.jpg')
        self.size2 += x
        self.image2 = pygame.transform.scale(
            self.image2, (self.size2, self.size2))
        self.x2 -= x / 2.0
        self.y2 -= x / 2.0
        self.image2.set_colorkey((56, 148, 213))
        self.alpha2 *= 0.95
        self.image2.set_alpha(self.alpha2)

    def tscale3(self, x):
        self.image3 = pygame.image.load(
            'python/wave/image/circle3.jpg')
        self.size3 += x
        self.image3 = pygame.transform.scale(
            self.image3, (self.size3, self.size3))
        self.x3 -= x / 2.0
        self.y3 -= x / 2.0
        self.image3.set_colorkey((56, 148, 213))
        self.alpha3 *= 0.95
        self.image3.set_alpha(self.alpha3)

    def reset(self):
        self.life = 0
        self.size = 0
        self.size2 = 0
        self.size3 = 0
        self.alpha1 = 170
        self.alpha2 = 210
        self.alpha3 = 240

    def set_position(self, x, y):
        self.life = 100
        self.x = x - self.size/2
        self.y = y - self.size/2
        self.x2 = x - self.size2/2
        self.y2 = y - self.size2/2
        self.x3 = x - self.size2/2
        self.y3 = y - self.size2/2
