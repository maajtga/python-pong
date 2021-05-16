import pygame

pygame.init()

winsize = [900, 550]

win = pygame.display.set_mode(winsize)
pygame.display.set_caption('Pong')
icon = pygame.image.load('gfx/icon.png')
pygame.display.set_icon(icon)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()