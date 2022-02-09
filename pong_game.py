# Import's

import pygame, sys, random, time, turtle
from pygame import mixer

# 🤔🤔🤔 General Requirments 🤔🤔🤔

pygame.init()
clock = pygame.time.Clock()

choose = True
window = pygame.display.set_mode((400,400))
single_player = pygame.image.load(r'data\singleplay.png').convert_alpha()
sp_rect = single_player.get_rect()
sp_rect.center = (200,100)
multi_player = pygame.image.load(r'data\multiplay.png').convert_alpha()
mp_rect = multi_player.get_rect()
mp_rect.center = (200,300)
window.blit(single_player,sp_rect)
window.blit(multi_player,mp_rect)
pygame.display.flip()
while choose:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pos = pygame.mouse.get_pos()
    if sp_rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            multi = False
            choose = False
    if mp_rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            multi = True
            choose = False
    clock.tick(80)
pygame.quit()

pygame.init()
clock = pygame.time.Clock()
pygame.mixer.pre_init(44100,-16,2,512)

# 😒😒😒 Layout Of Main Window 😒😒😒

screen_width = 1280
screen_height = 720
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PONG')

Backround_sound = mixer.Sound(r'data\2019-12-11_-_Retro_Platforming_-_David_Fesliyan.mp3')
Backround_sound.set_volume(0.3)
Backround_sound.play()
pong_hit_sound = mixer.Sound(r'data\pong hit sound.mp3')
pong_score_sound = mixer.Sound(r'data\score.mp3')

#  😀😀😀 Game Rectangles 😀😀😀

ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player1 = pygame.Rect(screen_width - 20 , screen_height / 2 - 70, 10 , 140)
player2 = pygame.Rect(10, screen_height / 2 - 70, 10  , 140)

def ball_animation():
    global ball_speed_x, ball_speed_y, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0:
        global player1_score
        player1_score += 1
        score_time = pygame.time.get_ticks()
        pygame.mixer.Sound.play(pong_score_sound)
        pong_score_sound.set_volume(0.3)

    if ball.right >= screen_width:
        global player2_score
        player2_score += 1
        score_time = pygame.time.get_ticks()
        pygame.mixer.Sound.play(pong_score_sound)
        pong_score_sound.set_volume(0.3)

    if ball.colliderect(player1) and ball_speed_x > 0 :
        pygame.mixer.Sound.play(pong_hit_sound)
        pong_hit_sound.set_volume(1.0)
        if abs(ball.right - player1.left ) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player1.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player1.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
    if ball.colliderect(player2) and ball_speed_x < 0 :
        pygame.mixer.Sound.play(pong_hit_sound)
        pong_hit_sound.set_volume(1.0)
        if abs(ball.left - player2.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player2.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player2.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1

def player1_animation():
    player1.y += player1_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height

def player2_animation():
    player2.y += player2_speed
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height:
        player2.bottom = screen_height

def bot():
    if player2.top < ball.y:
        player2.top += player2_speed
    if player2.top > ball.y:
        player2.bottom -= player2_speed
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height:
        player2.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y, score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width / 2, screen_height / 2)

    if (current_time - score_time) < 700:
        number_three = game_font.render("3", False, light_grey)
        window.blit(number_three, (screen_width / 2 - 10, screen_height / 2 + 20))

    if 700 < (current_time - score_time) < 1400:
        number_two = game_font.render("2", False, light_grey)
        window.blit(number_two, (screen_width / 2 - 10, screen_height / 2 + 20))

    if 1400 < (current_time - score_time) < 2100:
        number_one = game_font.render("1", False, light_grey)
        window.blit(number_one, (screen_width / 2 - 10, screen_height / 2 + 20))

    if current_time - score_time < 2100:
        ball_speed_x = 0
        ball_speed_y = 0
    else:
        ball_speed_y = 7 * random.choice((1, -1))
        ball_speed_x = 7 * random.choice((1, -1))
        score_time = None

# 🧑🏿🧑🏿🧑🏿 Colours 🧑🏿🧑🏿🧑🏿
bg_color = pygame.Color('#2F373F')
light_grey = (200, 200, 200)
red = (255, 0, 0)

#
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

player1_speed = 0
if multi:
    player2_speed = 0
else:
    player2_speed = 7

player1_score = 0
player2_score = 0

game_font = pygame.font.Font("freesansbold.ttf", 32)

score_time = None

while True:
    for event in pygame.event.get():

        # 😭😭😭 Game Quit 😭😭😭

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if multi:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    player2_speed += 7
                if event.key == pygame.K_w:
                    player2_speed -= 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    player2_speed -= 7
                if event.key == pygame.K_w:
                    player2_speed += 7
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed += 7
            if event.key == pygame.K_UP:
                player1_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed -= 7
            if event.key == pygame.K_UP:
                player1_speed += 7

    ball_animation()
    player1_animation()
    if multi:
        player2_animation()
    else:
        bot()

    # 🥴🥴🥴 Visuals 🥴🥴🥴
    window.fill(bg_color)
    pygame.draw.rect(window, red, player1)
    pygame.draw.rect(window, red, player2)
    pygame.draw.ellipse(window, light_grey, ball)
    pygame.draw.aaline(window, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    text1 = game_font.render(f"{player1_score}", True, light_grey)
    text2 = game_font.render(f"{player2_score}", True, light_grey)
    window.blit(text1, (660, 350))
    window.blit(text2, (600, 350))

    if score_time:
        ball_restart()

    # 😒😒😒 Screen Update 😒😒😒
    pygame.display.flip()

    # 🤑🤑🤑 FPS 🤑🤑🤑
    clock.tick(80)
