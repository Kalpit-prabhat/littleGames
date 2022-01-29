#Import's

import pygame , sys

#🤔🤔🤔 General Requirments 🤔🤔🤔

pygame.init()
clock = pygame.time.Clock()\

#😒😒😒 Layout Of Main Window 😒😒😒

screen_width = 1280
screen_height = 960
window = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('PONG')

#  😀😀😀 Game Rectangles 😀😀😀

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15 , 30 ,30 )
player1 = pygame.Rect(screen_width - 20 , screen_height/2 - 70 , 10 , 140 )
player2 = pygame.Rect(10 , screen_height/2 - 70 , 10 , 140 )

bg_color = (128,128,128)
light_grey = (200,200,200)

while True:
    for event in pygame.event.get():
        
        # 😭😭😭 Game Quit 😭😭😭
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #🥴🥴🥴 Visuals 🥴🥴🥴 
    window.fill(bg_color)        
    pygame.draw.rect( window , light_grey , player1 )
    pygame.draw.rect( window , light_grey , player2 )
    pygame.draw.ellipse( window , light_grey , ball )
    pygame.draw.aaline(window , light_grey , (screen_width/2,0), (screen_width/2,screen_height))

    # 😒😒😒 Screen Update 😒😒😒
    pygame.display.flip()
    
    # 🤑🤑🤑 FPS 🤑🤑🤑
    clock.tick(120)