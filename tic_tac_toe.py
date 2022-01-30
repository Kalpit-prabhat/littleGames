import pygame, sys

pygame.init()#initialising mod
running = True

#screen
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )

#mainloop 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
