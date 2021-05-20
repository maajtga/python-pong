import pygame

from data import paddle
from data import ball

pygame.init()

winsize = [900, 550]

win = pygame.display.set_mode(winsize)
pygame.display.set_caption('Pong')
icon = pygame.image.load('gfx/icon.png')
pygame.display.set_icon(icon)

running = True

Player1 = paddle.Paddle(70, 225)
Player2 = paddle.Paddle(800, 225)
Ball = ball.Ball(270, 400)

ballspeedx = 0.1
ballspeedy = 0.1

while running:
    
    win.fill(0)

    Player1.render(win)
    Player2.render(win)
    Ball.render(win)

    Ball.x += ballspeedx
    Ball.y += ballspeedy

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            pass

    pygame.display.flip()