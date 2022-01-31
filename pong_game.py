#Import's

import pygame , sys ,random
from pygame import mixer

#🤔🤔🤔 General Requirments 🤔🤔🤔

pygame.init()
clock = pygame.time.Clock()



#😒😒😒 Layout Of Main Window 😒😒😒

screen_width = 1280
screen_height = 960
window = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('PONG')

mixer.init()
sound1 = mixer.Sound(r'data\2019-12-11_-_Retro_Platforming_-_David_Fesliyan.mp3')
sound1.set_volume(0.3)
sound1.play()
sound2 = mixer.Sound('data\pong hit sound.mp3')


#  😀😀😀 Game Rectangles 😀😀😀

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15 , 30 ,30 )
player1 = pygame.Rect(screen_width - 20 , screen_height/2 - 70 , 10 , 140 )
player2 = pygame.Rect(10 , screen_height/2 - 70 , 10 , 140 )

def ball_animation():
    global ball_speed_x,  ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height :
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1
        
        sound2.play()

def player1_animation():
    player1.y +=player_speed 
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height :
        player1.bottom  = screen_height

def player2_animation():
    player2.y +=player_speed 
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height :
        player2.bottom  = screen_height

def bot():
    if player2.top < ball.y :
        player2.top  += player2_speed_bot 
    if player2.top > ball.y :
        player2.bottom -= player2_speed_bot
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height :
        player2.bottom  = screen_height


def ball_restart():
    global ball_speed_x , ball_speed_y
    ball.center = (screen_width/2 , screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))

# 🧑🏿🧑🏿🧑🏿 Colours 🧑🏿🧑🏿🧑🏿
bg_color = (0,0,0)
light_grey = (200,200,200)

ball_speed_x =  7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))

player_speed = 0
player2_speed_bot = 0



while True:
    for event in pygame.event.get():
        
        # 😭😭😭 Game Quit 😭😭😭
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            
            
            if event.key == pygame.K_s:
                player_speed += 7
            if event.key == pygame.K_w:
                player_speed -=7
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_s:
                player_speed -= 7
            if event.key == pygame.K_w:
                player_speed +=7
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player2_speed_bot += 7
            if event.key == pygame.K_UP:
                player2_speed_bot -=7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player2_speed_bot -= 7
            if event.key == pygame.K_UP:
                player2_speed_bot +=7
            

        
            
        
        

    ball_animation()
    player1_animation()
    player2_animation()

    


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

    