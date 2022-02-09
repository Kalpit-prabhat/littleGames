import pygame, random

pygame.init()
win = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
pygame.display.set_caption('2048')

pygame.mixer.init()
pygame.mixer.music.load(r"data\C418_-_Sweden_-_Minecraft_Volume_A_(getmp3.pro).mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

data = open(r'data\data.txt','r+')
FPS=60
TIME = 0.15
ALPHA = 100
Highscore = int(data.readline())
data.truncate(0)
data.seek(0)

score = 0
pressed = False
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
        if self.val>128:
            color = colors[128]
        else:
            color = colors[self.val]
        pygame.draw.rect(win, color, self.rec,50,10)
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

def game_over():
    if 0 not in grid.values():
        for cell, block in grid.items():
            adjacent = []
            if cell[0]>0:
                adjacent.append(grid[(cell[0]-1,cell[1])].val)
            if cell[0]<3:
                adjacent.append(grid[(cell[0]+1,cell[1])].val)
            if cell[1]>0:
                adjacent.append(grid[(cell[0],cell[1]-1)].val)
            if cell[1]<3:
                adjacent.append(grid[(cell[0],cell[1]+1)].val)
            if block.val in adjacent:
                return False
        else:
            return True

def restart():
    global score, grid, score_rect
    score = 0
    grid = {(0,0):0,(1,0):0,(2,0):0,(3,0):0,
        (0,1):0,(1,1):0,(2,1):0,(3,1):0,
        (0,2):0,(1,2):0,(2,2):0,(3,2):0,
        (0,3):0,(1,3):0,(2,3):0,(3,3):0,}
    pygame.draw.rect(win, (0,0,0), score_rect)
    score_text = font.render(str(score), True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(500,100))
    win.blit(score_text,score_rect)
    win.blit(bg,(0,0))
    choices = random.sample(grid.keys(),2)
    for choice in choices:
        grid[choice] = Blocks(2,choice)
        grid[choice].draw((choice[0]*100,choice[1]*100))

choices = random.sample(grid.keys(),2)
for choice in choices:
    grid[choice] = Blocks(2,choice)

font = pygame.font.SysFont('data\\font.ttf',40)
font2 = pygame.font.SysFont('data\\font.ttf',60)
bg = pygame.image.load(r'data\2048_bg.png')
rs = pygame.image.load(r'data\restart.png')
rs_rect = rs.get_rect()
rs_rect.center = (500,300)
frames_needed = int(FPS*TIME)

text1 = font.render('Score:', True, (255,255,255))
textrect1 = text1.get_rect(center=(500,50))
text2 = font.render('Highscore:', True, (255,255,255))
textrect2 = text2.get_rect(center=(500,150))
score_text = font.render(str(score), True, (255, 255, 255))
score_rect = score_text.get_rect(center=(500,100))
high_text = font.render(str(Highscore), True, (255, 255, 255))
high_rect = high_text.get_rect(center=(500,200))
win.blit(text1,textrect1)
win.blit(text2,textrect2)
win.blit(score_text,score_rect)
win.blit(high_text,high_rect)
win.blit(rs,rs_rect)

win.blit(bg,(0,0))
for cell, block in grid.items():
    if block:
        block.draw((cell[0]*100,cell[1]*100))

running = True
while running:
    pos = pygame.mouse.get_pos()
    if rs_rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1 and pressed == False:
            pressed = True
            restart()
    if pygame.mouse.get_pressed()[0] == 0 and pressed:
        pressed = False
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
            win.blit(bg,(0,0))
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
        score_text = font.render(str(score), True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(500,100))
        pygame.draw.rect(win, (0,0,0), score_rect)
        win.blit(score_text,score_rect)
        if game_over():
            for a in range(ALPHA//4):
                clock.tick(FPS)
                s = pygame.Surface((400,400),pygame.SRCALPHA)
                s.fill((255,255,255,1))
                win.blit(s,(0,0))
                pygame.display.flip()
            text = font2.render('Game Over!', True, (82, 34, 0))
            textrect = text.get_rect(center=(200,200))
            win.blit(text,textrect)
            pygame.display.flip()
            if score > Highscore:
                Highscore = score
                pygame.draw.rect(win, (0,0,0), high_rect)
                high_text = font.render(str(Highscore), True, (255, 255, 255))
                high_rect = high_text.get_rect(center=(500,200))
                win.blit(score_text,high_rect)
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
data.write(str(Highscore))
data.close()