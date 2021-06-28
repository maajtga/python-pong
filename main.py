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

ballspeedx = 0.5
ballspeedy = 0.5

while running:
    
    win.fill(0)

    Player1.render(win)
    Player2.render(win)
    Ball.render(win)
    
    Ball.x += ballspeedx
    Ball.y += ballspeedy

    if Ball.x > 486 or Ball.x < 0:
        ballspeedx *= -1

    if Ball.y > 836 or Ball.y < 0:
        ballspeedy *= -1

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w:
                Player1.y -= 20

            if event.key == pygame.K_s:
                Player1.y += 20

            if event.key == pygame.K_UP:
                Player2.y -= 20

            if event.key == pygame.K_DOWN:
                Player2.y += 20

        
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_w:
                Player1.y -= 20


    pygame.display.flip()