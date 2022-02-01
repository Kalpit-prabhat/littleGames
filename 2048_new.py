import random

import pygame

pygame.init()

win = pygame.display.set_mode((400, 400))

FPS=30
clock = pygame.time.Clock()

running = True

pygame.display.set_caption('2048')

colors = {2:(255, 154, 162), 4:(255, 183, 178), 8:(255, 218, 193),
        16:(205, 238, 150), 32:(181, 234, 215), 64:(199, 206, 234),
        128:(234, 199, 228)}

class Blocks(object):
    def __init__(self,val,pos):
        self.val = val
        self.pos = pos
    
    def draw(self,position:tuple):
        self.rec = pygame.Rect(position,(100,100))
        text = font.render(str(self.val), True, (255,255,255))
        textrect = text.get_rect(center=self.rec.center)
        value = self.val
        while value>128:
            value = value//128
        pygame.draw.rect(win, colors[value], self.rec,50,10)
        win.blit(text,textrect)

grid = {(0,0):0,(1,0):0,(2,0):0,(3,0):0,
        (0,1):0,(1,1):0,(2,1):0,(3,1):0,
        (0,2):0,(1,2):0,(2,2):0,(3,2):0,
        (0,3):0,(1,3):0,(2,3):0,(3,3):0,}
# choices = random.sample(grid.keys(),2)
choices = [(1,1),(2,1),(1,3)]
for choice in choices:
    grid[choice] = Blocks(2,choice)

def update(direction):
    global grid
    if direction[0] == '+':
        cond = '<3'
        reverse=True
    else:
        cond = '>0'
        reverse = False
    d = int(f'{direction[0]}1')
    if direction[1] == 'y':
        y_sort = sorted(grid.keys(),key= lambda x: x[1],reverse=reverse)
        for cell in y_sort:
            block = grid[cell]
            if block != 0 and eval(f'cell[1]{cond}'):
                new = cell[1]+d
                while grid[(cell[0],new)] == 0 and eval(f'(new+d){cond}'):
                    new += d
                grid[(cell[0],new-d)] = block
                grid[cell] = 0
    elif direction[1] == 'x':
        x_sort = sorted(grid.keys(),key= lambda x: x[0],reverse=reverse)
        for cell in x_sort:
            block = grid[cell]
            if block != 0 and eval(f'cell[0]{cond}'):
                new = cell[0]+d
                while grid[(new,cell[1])] == 0 and eval(f'(new+d){cond}'):
                    new += d
                grid[(new-d,cell[1])] = block
                grid[cell] = 0
    return grid

font = pygame.font.SysFont('data\\font.ttf',40)

win.fill((255,255,255))
for cell, block in grid.items():
    if block:
        block.draw((cell[0]*100,cell[1]*100))

while running:
    direction = ''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                direction = '-x'
            elif event.key == pygame.K_RIGHT:
                direction = '+x'
            elif event.key == pygame.K_UP:
                direction = '-y'
            elif event.key == pygame.K_DOWN:
                direction = '+y'
    if direction != '':
        win.fill((255,255,255))
        grid = update(direction)
        for cell, block in grid.items():
            if block:
                block.draw((cell[0]*100,cell[1]*100))
        rand_pos = random.choice([key for key in grid.keys() if grid[key]==0])
        grid[rand_pos] = Blocks(random.choices([2,4],weights=[10,1])[0],rand_pos)
        grid[rand_pos].draw((rand_pos[0]*100,rand_pos[1]*100))
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
