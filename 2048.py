import random

import pygame

pygame.init()

win = pygame.display.set_mode((400, 400))

running = True

pygame.display.set_caption('2048')

grid = {'a1':2,'b1':0,'c1':0,'d1':128,
        'a2':0,'b2':4,'c2':64,'d2':0,
        'a3':0,'b3':0,'c3':8,'d3':0,
        'a4':32,'b4':0,'c4':0,'d4':16,}
# choices = random.sample(grid.keys(),2)
# grid[choices[0]] = 2
# grid[choices[1]] = 2

colors = {2:(255, 154, 162), 4:(255, 183, 178), 8:(255, 218, 193),
        16:(205, 238, 150), 32:(181, 234, 215), 64:(199, 206, 234),
        128:(234, 199, 228)}

position = {'a1':(0,0),'b1':(100,0),'c1':(200,0),'d1':(300,0),
        'a2':(0,100),'b2':(100,100),'c2':(200,100),'d2':(300,100),
        'a3':(0,200),'b3':(100,200),'c3':(200,200),'d3':(300,200),
        'a4':(0,300),'b4':(100,300),'c4':(200,300),'d4':(300,300)}

def update(direction):
    if direction != '':
        if direction[1] == 'x':
            if direction[0] == '-':
                clms = 'bcd'
                d = -1
            else:
                clms = 'cba'
                d = 1
            for i in range(4):
                for c in clms:
                    for r in '1234':
                        if grid[c+r]:
                            if grid[chr(ord(c)+d)+r] == 0:
                                grid[chr(ord(c)+d)+r] = grid[c+r]
                                grid[c+r] = 0
                            elif i == 3 and grid[chr(ord(c)+d)+r] == grid[c+r]:
                                grid[chr(ord(c)+d)+r] += grid[c+r]
                                grid[c+r] = 0
        elif direction[1] == 'y':
            if direction[0] == '-':
                rows = '234'
                d = -1
            else:
                rows = '321'
                d = 1
            for i in range(4):
                for r in rows:
                    for c in 'abcd':
                        if grid[c+r]:
                            if grid[c+str(int(r)+d)] == 0:
                                grid[c+str(int(r)+d)] = grid[c+r]
                                grid[c+r] = 0
                            elif i == 3 and grid[c+str(int(r)+d)] == grid[c+r]:
                                grid[c+str(int(r)+d)] += grid[c+r]
                                grid[c+r] = 0
        empty = [cell for cell in grid.keys() if grid[cell] == 0]
        grid[random.choice(empty)] = random.choices([2,4],weights=[10,1])[0]
    return grid

font = pygame.font.SysFont('data\\font.ttf',40)

lst = ''
while running:
    pygame.time.wait(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    direction = ''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        direction = '-x'
    elif keys[pygame.K_RIGHT]:
        direction = '+x'
    elif keys[pygame.K_UP]:
        direction = '-y'
    elif keys[pygame.K_DOWN]:
        direction = '+y'
    
    if direction != lst:
        lst = direction
        grid_new = update(direction)
        if grid_new == grid:
            continue
    win.fill((255,255,255))
    for cell,val in grid.items():
        if val:
            rec = pygame.Rect(position[cell],(100,100))
            text = font.render(str(val), True, (255,255,255))
            textrect = text.get_rect(center=rec.center)
            while val>128:
                val = val//128
            pygame.draw.rect(win, colors[val], rec,50,10)
            win.blit(text,textrect)
    pygame.display.flip()

pygame.quit()
