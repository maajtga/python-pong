import pygame

class Ball():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('gfx/ball.png')
        self.rect = self.image.get_rect()

    def render(self, win):
        win.blit(self.image, (self.y, self.x))