#modules
import pygame, random, sys, numpy


#---dimensions---
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


#---colours---
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRC_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)


#---pygame initialisation---
pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Tic Tac Toe')
screen.fill( BG_COLOR )

class Board:

    def __init__(self):
        self.squares = numpy.zeros( (ROWS, COLS) )
        self.empty_sqrs = self.squares
        self.marked_sqrs = 0

    def final_state(self):

        #---checking for vertical win---
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                return self.squares[0][col]

        #---checking for horizontal win---
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][0] == self.squares[row][0] != 0:
                return self.squares[0][col]

        #---checking for desc diag win---  
        for col in range(COLS):
            if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
                return self.squares[1][1]

        #---checking for asc diag win---    
        for col in range(COLS):
            if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
                return self.squares[1][1]

        #---if there is no win yet---
        return 0
            
    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0

    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqr(row, col):
                    empty_sqrs.append( (row, col) )
        return empty_sqrs
    
    def is_full(self):
        return self.marked_sq == 9

    def is_empty(self):
        return self.marked_sqr == 0
        
class AI:

    def __init__(self, level = 0, player = 2):
        self.level = level
        self.player = player

    def rnd(self, board):
        empty_sqrs = board.get_empty_sqrs()
        idx = random.randrange(0, len(empty_sqrs))
        return empty_sqrs[idx]

    def eval(self, main_board):
        if self.level == 0:
            move = self.rnd(main_board)
        else:
            pass
        return move

class Game:

    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.gamemode = 'ai'
        self.running = True
        self.player = 1
        self.show_lines()
        
    def show_lines(self):
        #verti line 1
        pygame.draw.line( screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        #verti line 2
        pygame.draw.line( screen, LINE_COLOR, (SQSIZE*2, 0), (SQSIZE*2, HEIGHT), LINE_WIDTH)
        #hori line 1
        pygame.draw.line( screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        #verti line 1
        pygame.draw.line( screen, LINE_COLOR, (0, SQSIZE*2), (WIDTH, SQSIZE*2), LINE_WIDTH)

    def draw_fig(self, row, col):
        if self.player == 1:
            #decs line
            start_desc = ( col * SQSIZE + OFFSET, row * SQSIZE + OFFSET ) 
            end_desc = ( col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET )
            pygame.draw.line( screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH )
            #asc line
            start_asc = ( col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET )
            end_asc = ( col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET )
            pygame.draw.line( screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH )
            
        elif self.player == 2:
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle( screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH )
            
    def next_turn(self):
        self.player = self.player % 2 + 1


#designing main loop
def main_loop():

    #object
    game = Game()
    board = game.board
    ai = game.ai
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE  #or 200
                col = pos[0] // SQSIZE
 
                if board.empty_sqr(row, col):
                    board.mark_sqr(row, col, game.player)
                    game.draw_fig(row, col)
                    game.next_turn()
        if game.gamemode == 'ai' and game.player == ai.player:
            pygame.display.update()
            row, col = ai.eval(board)
            board.mark_sqr(row, col, game.player)
            game.draw_fig(row, col)
            game.next_turn()
        pygame.display.update()
main_loop()
    

