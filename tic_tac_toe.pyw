import pygame, sys
import numpy 

pygame.init()#initialising mod
running = True
pressed = False

#graphic attributes
WIDTH = 600
HEIGHT = WIDTH
DIV_WIDTH = 15
#colours
SCREEN = (66, 233, 245)
DIV = (0, 0, 0)
CIRCLE_C = (255, 249, 184)
CROSS_C = (48, 48, 48)
CIRCLE_W = 15#thickness
CIRCLE_R = 60#radius
CROSS_W = 25
SPACE = 55

#screen
screen = pygame.display.set_mode( (800, HEIGHT) )
pygame.display.set_caption("Tic Tac Toe")
screen.fill( (SCREEN) )

#creating playing field
field = numpy.zeros( (3,3) )

#drawing tic tac toe divisions
def draw_lines():
    #hori 1
    pygame.draw.line( screen,(DIV), (0, 200), (600, 200), (DIV_WIDTH) )
    pygame.draw.line( screen,(DIV), (0, 0), (600, 0), (DIV_WIDTH) )
    pygame.draw.line( screen,(DIV), (0, 600), (600, 600), (DIV_WIDTH) )
    #hori 2
    pygame.draw.line( screen,(DIV), (0, 400), (600, 400), (DIV_WIDTH) )
    #vert 1
    pygame.draw.line( screen,(DIV), (200, 0), (200, 600), (DIV_WIDTH) )
    #verti 2
    pygame.draw.line( screen,(DIV), (400, 0), (400, 600), (DIV_WIDTH) )
    pygame.draw.line( screen,(DIV), (600, 0), (600, 600), (DIV_WIDTH) )
    pygame.draw.line( screen,(DIV), (0, 0), (0, 600), (DIV_WIDTH) )

#symbol drawer
def draw_marks():
    for row in range(3):
        for col in range(3):
            if field[row][col] == 1:
                pygame.draw.circle( screen, CIRCLE_C, (int(col*200+100), int(row*200+100)), (CIRCLE_R), (CIRCLE_W))

            elif field[row][col] == 2:
                pygame.draw.line( screen, CROSS_C, (col*200+SPACE, row*200+200-SPACE), (col*200+200-SPACE, row*200+SPACE), CROSS_W)
                pygame.draw.line( screen, CROSS_C, (col*200+SPACE, row*200+SPACE), (col*200+200-SPACE, row*200+200-SPACE), CROSS_W)

#are all sq full funcn
def full():
    for row in range(3):
        for col in range(3):
            if field[row, col] == 0:
                return False
    return True

#winning conditions
def win(player):
    for col in range(3):
        if field[0][col] == player and field[1][col] == player and field[2][col] == player:
            verti_win(col, player)
            return True
    for row in range(3):
        if field[row][0] == player and field[row][1] == player and field[row][2] == player:
            hori_win(row, player)
            return True
    if field[2][0] == player and field[1][1] == player and field[0][2] == player:
            asc_diag_win(player)
            return True
    if field[0][0] == player and field[1][1] == player and field[2][2] == player:
            desc_diag_win(player)
            return True

    return False

#win line drawer
def verti_win(col, player):
    posX = col * 200 + 100

    if player == 1:
        color = CIRCLE_C
    elif player == 2:
        color = CROSS_C

    pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), 15)

def hori_win(row, player):
    posY = row * 200 + 100

    if player == 1:
        color = CIRCLE_C
    elif player == 2:
        color = CROSS_C

    pygame.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), 15)

def asc_diag_win(player):
    if player == 1:
        color = CIRCLE_C
    elif player == 2:
        color = CROSS_C

    pygame.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)

def desc_diag_win(player):
    if player == 1:
        color =  CIRCLE_C
    elif player == 2:
        color =  CROSS_C

    pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)

#game restarter
def restart():
    screen.fill( SCREEN )
    draw_lines()
    player = 1
    for row in range(3):
        for col in range(3):
            field[row][col] = 0
    screen.blit(rs,rs_rect)
            
#calling functions
draw_lines() 

#assigning values
player = 1
game_over = False

rs = pygame.image.load(r'data\restart.png')
rs_rect = rs.get_rect()
rs_rect.center = (700,300)
screen.blit(rs,rs_rect)

#mainloop 
while running:
    pos = pygame.mouse.get_pos()
    if rs_rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1 and pressed == False:
            pressed = True
            restart()
            player = 1
            game_over = False
    if pygame.mouse.get_pressed()[0] == 0 and pressed:
        pressed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] # x co-ordinate
            mouseY = event.pos[1] # y co-ordinate
            if mouseX>600:
                break
            # to check which box is clicked
            clickedX = int(mouseX // 200)
            clickedY = int(mouseY // 200)

            if field[clickedY, clickedX] == 0:
                if player == 1:
                    field[clickedY, clickedX] = 1
                    win( player )
                    if win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    field[clickedY, clickedX] = 2
                    win( player )
                    if win(player):
                        game_over = True
                    player = 1
                draw_marks()
    pygame.display.update()
pygame.quit()
