import pygame

class Paddle():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('gfx/paddle.png')

    def render(self, win):
        win.blit(self.image, (self.x, self.y))