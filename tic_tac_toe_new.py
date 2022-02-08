#modules
import pygame, random
import sys


#DIMENSIONS
WIDTH = 600
HEIGHT = 600

ROWS = 3
COLS = 3
SQSIZE = WIDTH // COLS

LINE_WIDTH = 15
CIRC_WIDTH = 15
CROSS_WIDTH = 20

RADIUS = SQSIZE // 4

OFFSET = 50


#COLORS
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRC_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)


#pygame initialisation
pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Tic Tac Toe')
screen.fill( BG_COLOR )

class Game:

    def __init__(self):
        self.show_lines()
        pass
    def show_lines(self):
        #verti line 1
        pygame.draw.line( screen, LINE_COLOUR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        #verti line 2
        pygame.draw.line( screen, LINE_COLOUR, (SQSIZE*2, 0), (SQSIZE*2, HEIGHT), LINE_WIDTH)
        #hori line 1
        pygame.draw.line( screen, LINE_COLOUR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        #verti line 1
        pygame.draw.line( screen, LINE_COLOUR, (0, SQSIZE*2), (WIDTH, SQSIZE*2), LINE_WIDTH)
        
                
#designing main loop
def main_loop():

    #object
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update

main_loop()
    

