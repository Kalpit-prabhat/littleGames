import pygame, os
running = True
FPS = 120

pygame.init()
win = pygame.display.set_mode((600, 150))
clock = pygame.time.Clock()
pygame.display.set_caption('littleGames')

class Button(object):
    def __init__(self,pos,text,size,text_color,file_path):
        self.rect = pygame.Rect(pos,size)
        self.text = font.render(text, True, text_color)
        self.textrect = self.text.get_rect(center=self.rect.center)
        self.file = file_path
    
    def draw(self,color):
        pygame.draw.rect(win, color, self.rect,25,10)
        win.blit(self.text,self.textrect)

font = pygame.font.SysFont('data\\font.ttf',40)
butts = []
butts.append(Button((25,50),'Tic-Tac-Toe',(150,50),(230,230,230),r'tic_tac_toe.pyw'))
butts.append(Button((225,50),'2048',(150,50),(230,230,230),r'2048.pyw'))
butts.append(Button((425,50),'Pong',(150,50),(230,230,230),r'pong_game.pyw'))

while running:
    clock.tick(FPS)
    win.fill((141, 223, 240))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pos = pygame.mouse.get_pos()

    for button in butts:
        if button.rect.collidepoint(pos):
            button.draw((40, 55, 199))
            if pygame.mouse.get_pressed()[0] == 1 :
                os.startfile(button.file)
                running = False
        else:
            button.draw((40, 121, 153))
    
    pygame.display.flip()
pygame.quit()
