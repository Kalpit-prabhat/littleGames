import pygame, random

pygame.init()
win = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
pygame.display.set_caption('2048')

FPS=60
TIME = 0.15

score = 0
grid = {(0,0):0,(1,0):0,(2,0):0,(3,0):0,
        (0,1):0,(1,1):0,(2,1):0,(3,1):0,
        (0,2):0,(1,2):0,(2,2):0,(3,2):0,
        (0,3):0,(1,3):0,(2,3):0,(3,3):0,}

colors = {2:(255, 154, 162), 4:(255, 183, 178), 8:(255, 218, 193),
        16:(205, 238, 150), 32:(181, 234, 215), 64:(199, 206, 234),
        128:(234, 199, 228)}

class Blocks(object):
    def __init__(self,val,pos):
        self.val = val
        self.pos = pos
    
    def __bool__(self):
        return True
    
    def __len__(self):
        return 0
    
    def draw(self,position:tuple):
        self.rec = pygame.Rect(position,(100,100))
        text = font.render(str(self.val), True, (255,255,255))
        textrect = text.get_rect(center=self.rec.center)
        value = self.val
        while value>128:
            value = value//128
        pygame.draw.rect(win, colors[value], self.rec,50,10)
        win.blit(text,textrect)

def update(direction):
    grid_new = grid.copy()
    if direction[0] == '+':
        cond = '<3'
        reverse=True
    else:
        cond = '>0'
        reverse = False
    d = int(f'{direction[0]}1')
    if direction[1] == 'y':
        y_sort = sorted(grid_new.keys(),key= lambda x: (x[1],x[0]),reverse=reverse)
        for cell in y_sort:
            block = grid_new[cell]
            if block != 0 and eval(f'cell[1]{cond}'):
                new = cell[1]
                while eval(f'new{cond}') and grid_new[(cell[0],new+d)] == 0:
                    new += d
                if eval(f'new{cond}') and (len(grid_new[(cell[0],new+d)]) == 0 and grid_new[(cell[0],new+d)].val == grid_new[cell].val):
                    grid_new[(cell[0],new+d)] = [grid_new[(cell[0],new+d)],grid_new[cell]]
                    grid_new[cell] = 0
                elif new != cell[1]:
                    grid_new[(cell[0],new)] = block
                    grid_new[cell] = 0
    elif direction[1] == 'x':
        x_sort = sorted(grid_new.keys(),key= lambda x: (x[0],x[1]),reverse=reverse)
        for cell in x_sort:
            block = grid_new[cell]
            if block != 0 and eval(f'cell[0]{cond}'):
                new = cell[0]
                while eval(f'new{cond}') and grid_new[(new+d,cell[1])] == 0:
                    new += d
                if eval(f'new{cond}') and (len(grid_new[(new+d,cell[1])]) == 0 and grid_new[(new+d,cell[1])].val == grid_new[cell].val):
                    grid_new[(new+d,cell[1])] = [grid_new[(new+d,cell[1])],grid_new[cell]]
                    grid_new[cell] = 0
                elif new != cell[0]:
                    grid_new[(new,cell[1])] = block
                    grid_new[cell] = 0
    return grid_new

def frame_pos(cell,block,frame):
    if cell[0] == block.pos[0]:
        y = block.pos[1] + (cell[1]-block.pos[1])*(frame+1)/frames_needed
        new = (cell[0],y)
    else:
        x = block.pos[0] + (cell[0]-block.pos[0])*(frame+1)/frames_needed
        new = (x,cell[1])
    return new

choices = random.sample(grid.keys(),2)
for choice in choices:
    grid[choice] = Blocks(2,choice)

font = pygame.font.SysFont('data\\font.ttf',40)
frames_needed = int(FPS*TIME)

win.fill((255,255,255))
for cell, block in grid.items():
    if block:
        block.draw((cell[0]*100,cell[1]*100))

running = True
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
        change = []
        grid_new = update(direction)
        if grid_new == grid:
            continue
        grid = grid_new.copy()
        for frame in range(frames_needed):
            clock.tick(FPS)
            win.fill((255,255,255))
            for cell, block in grid.items():
                if block:
                    if len(block):
                        new = frame_pos(cell,block[0],frame)
                        block[0].draw((new[0]*100,new[1]*100))
                        block = block[1]
                        if frame == frames_needed-1:
                            grid[cell] = block
                            block.val *= 2
                            score += block.val
                    if block.pos == cell:
                        block.draw((cell[0]*100,cell[1]*100))
                    else:
                        new = frame_pos(cell,block,frame)
                        block.draw((new[0]*100,new[1]*100))
                        if frame == frames_needed-1:
                            block.pos = cell
            pygame.display.flip()
        rand_pos = random.choice([key for key in grid.keys() if grid[key]==0])
        grid[rand_pos] = Blocks(random.choices([2,4],weights=[10,1])[0],rand_pos)
        grid[rand_pos].draw((rand_pos[0]*100,rand_pos[1]*100))
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
