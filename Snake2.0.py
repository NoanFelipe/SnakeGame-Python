import pygame
import random
from menu_func import *
from file_func import *

if not fileExists('player_info.json'):
    createFile('player_info.json')

screen_width = 600
screen_height = 600
pixels_list = {}
grid_width = 20
grid_height = 20
block_size = screen_width / grid_width
clock = pygame.time.Clock()
fruit_color = 0

class Food:
    def __init__(self):
        self.change = True
        self.r = random.randint(0, 399)
    
    def create(self, surface):
        if self.change:
            self.r = random.randint(0, 399)
            pixels_list[self.r][2] = 1
            self.change = False
        for c in range(0, 19):
            if self.r == c:
                self.change = True
                pixels_list[self.r][2] = 0
        for c1 in range(20, 400, 20):
            if self.r == c1:
                self.change = True
                pixels_list[self.r][2] = 0 
        for c2 in range(19, 419, 20):
            if self.r == c2:
                self.change = True
                pixels_list[self.r][2] = 0 
        for c3 in range(380, 400):
            if self.r == c3:
                self.change = True
                pixels_list[self.r][2] = 0 

        for k, v in enumerate(Snake):
            if Snake[k][0] == pixels_list[self.r][0] and Snake[k][1] == pixels_list[self.r][1]:
                self.change = True
                pixels_list[self.r][2] = 0 

def start():
    pygame.init()
    pygame.display.set_caption('Snake')
    create_grid()

def draw_game_window(surface):
    win.fill((0,0,0))
    c = 0
    json_read = ReadJsonFile('player_info.json')
    player_info = []
    player_info.append(json_read)
    global fruit_color
    for k, v in enumerate(pixels_list):
        if pixels_list[k][2] == 1:
            if fruit_color == 0:
                pygame.draw.rect(surface, (255, 50, 50), (pixels_list[k][0], pixels_list[k][1], block_size, block_size))
            else:
                pygame.draw.rect(surface, (255, 255, 50), (pixels_list[k][0], pixels_list[k][1], block_size, block_size))
    
    for k, v in enumerate(Snake):
        if player_info[0][0]['equiped'] == 0:
            pygame.draw.rect(surface, (255, 255, 255), (Snake[k][0], Snake[k][1], block_size, block_size))
            fruit_color = 0
        elif player_info[0][0]['equiped'] == 1:
            pygame.draw.rect(surface, (0, 255, 0), (Snake[k][0], Snake[k][1], block_size, block_size))
            fruit_color = 0
        elif player_info[0][0]['equiped'] == 2:
            pygame.draw.rect(surface, (50, 50, 255), (Snake[k][0], Snake[k][1], block_size, block_size))
            fruit_color = 0
        elif player_info[0][0]['equiped'] == 3:
            if c == 0:
                pygame.draw.rect(surface, (0, 255, 0), (Snake[k][0], Snake[k][1], block_size, block_size))
            if c == 1:
                pygame.draw.rect(surface, (255, 255, 0), (Snake[k][0], Snake[k][1], block_size, block_size))
            c += 1
            if c == 2:
                c = 0
            fruit_color = 0
        elif player_info[0][0]['equiped'] == 4:
            c += 1
            if c == 1:
                pygame.draw.rect(surface, (50, 50, 255), (Snake[k][0], Snake[k][1], block_size, block_size))
            elif c == 2:
                pygame.draw.rect(surface, (255, 50, 50), (Snake[k][0], Snake[k][1], block_size, block_size))
            elif c == 3:
                pygame.draw.rect(surface, (255, 255, 255), (Snake[k][0], Snake[k][1], block_size, block_size))
                c = 0
            fruit_color = 1
        
    text = font.render(f'Size: {len(Snake)}', 1, (255, 255, 255))
    surface.blit(text, (400, 7))
    draw_grid(surface)
    pygame.display.update()

def create_grid():
    global pixels_list
    
    x = 0
    y = 0
    numberOfPixels = grid_width * grid_height
    
    for i in range(0, numberOfPixels):
        pixels_list[i] = [x, y, 0]
        if x < screen_width - block_size:
            x += block_size
        else:
            y += block_size
            x = 0

def draw_grid(surface):
    x = 0
    y = 0
    for row in range(0, grid_width + 1):
        pygame.draw.line(surface, (128,128,128), (x, y), (x, screen_height))
        x += block_size

    x = 0 
    y = 0

    for column in range(0, grid_height + 1):
        pygame.draw.line(surface, (128,128,128), (x, y), (screen_width, y))
        y += block_size

def move():
    global Snake
    global d
    if d == 2:
        Snake[0][0] += block_size

    elif d == 3:
        Snake[0][0] -= block_size

    elif d == 0:
        Snake[0][1] -= block_size

    elif d == 1:
        Snake[0][1] += block_size

    try:
        if len(Snake) >= 2:
            for k, v in enumerate(Snake):
                if Snake.index(v) != 0:
                    if Snake[k][2] == 0:
                        Snake[k][1] -= block_size

                    elif Snake[k][2] == 1:
                        Snake[k][1] += block_size

                    elif Snake[k][2] == 2:
                        Snake[k][0] += block_size

                    elif Snake[k][2] == 3:
                        Snake[k][0] -= block_size

    except:
        print('error')

def test():
    global last_pos
    global Snake
    if len(Snake) >= 2:
        try:
            Snake[1][2] = last_pos[0]
        except:
            print('error')

def check_lost():
    for k, v in enumerate(Snake):
        if Snake.index(v) != 0:
            if Snake[k][0] == Snake[0][0]:
                if Snake[k][1] == Snake[0][1]:
                    return True
    return False

def check_lost1():
    if Snake[0][0] > screen_width - block_size or Snake[0][0] < 0 or Snake[0][1] > screen_height - block_size or Snake[0][1] < 0:
        return True
    return False

def game_loop():
    run = True
    global last_pos
    global size
    global Snake
    global player_info
    while run:
        clock.tick(5)
        
        json_read = ReadJsonFile('player_info.json')

        player_info = []
        player_info.append(json_read)

        global d
        
        r = food.r

        moved = False

        test()

        for k, v in enumerate(Snake):
            if Snake.index(v) != 0 and Snake.index(v) != 1:
                Snake[k][2] = last_pos[k - 1]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                d = -1 #direction
                Snake = [[300, 300]]
                pixels_list[food.r][2] = 0
                food.change = True
                last_pos = []
                size = 1
                WriteOnJsonFile(player_info[0], 'player_info.json')
                
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    d = -1 #direction
                    Snake = [[300, 300]]
                    pixels_list[food.r][2] = 0
                    food.change = True
                    last_pos = []
                    size = 1
                    WriteOnJsonFile(player_info[0], 'player_info.json')
                    
                    run = False

                if event.key == pygame.K_w:
                    if d != 1:
                        if not moved:
                            d = 0
                            moved = True

                elif event.key == pygame.K_s:
                    if d != 0:
                        if not moved:
                            d = 1
                            moved = True
                    
                elif event.key == pygame.K_d:
                    if d != 3:
                        if not moved:
                            d = 2
                            moved = True
                
                elif event.key == pygame.K_a:
                    if d != 2:
                        if not moved:
                            d = 3
                            moved = True

        if Snake[0][0] == pixels_list[r][0] and Snake[0][1] == pixels_list[r][1]:
            pixels_list[r][2] = 0
            food.change = True
            size += 1
            player_info[0][0]['gold'] += 5
            WriteOnJsonFile(player_info[0], 'player_info.json')
            
            if len(Snake) == 1:
                if d == 0:
                    Snake.append([Snake[len(Snake) - 1][0], Snake[len(Snake) - 1][1] + block_size, 0])

                if d == 1:
                    Snake.append([Snake[len(Snake) - 1][0], Snake[len(Snake) - 1][1] - block_size, 1])

                if d == 2:
                    Snake.append([Snake[len(Snake) - 1][0] - block_size, Snake[len(Snake) - 1][1], 2])
                
                if d == 3:
                    Snake.append([Snake[len(Snake) - 1][0] + block_size, Snake[len(Snake) - 1][1], 3])
            else:
                if Snake[len(Snake)-1][2] == 0:
                    Snake.append([Snake[len(Snake) - 1][0], Snake[len(Snake) - 1][1] + block_size, 0])

                if Snake[len(Snake)-1][2] == 1:
                    Snake.append([Snake[len(Snake) - 1][0], Snake[len(Snake) - 1][1] - block_size, 1])

                if Snake[len(Snake)-1][2] == 2:
                    Snake.append([Snake[len(Snake) - 1][0] - block_size, Snake[len(Snake) - 1][1], 2])
                
                if Snake[len(Snake)-1][2] == 3:
                    Snake.append([Snake[len(Snake) - 1][0] + block_size, Snake[len(Snake) - 1][1], 3])

        food.create(win)
        move()

        del last_pos
        last_pos = [d]
        for k, v in enumerate(Snake):
            if Snake.index(v) != 0:
                last_pos.append(Snake[k][2])

        if size > player_info[0][0]['highscore']:
            player_info[0][0]['highscore'] = size

        try:
            draw_game_window(win)
        except:
            print('error')

        WriteOnJsonFile(player_info[0], 'player_info.json')

        if check_lost():
            d = -1 #direction
            Snake = [[300, 300]]
            pixels_list[food.r][2] = 0
            food.change = True
            last_pos = []
            size = 1
            run = False
        
        if check_lost1():
            d = -1 #direction
            Snake = [[300, 300]]
            pixels_list[food.r][2] = 0
            food.change = True
            last_pos = []
            size = 1
            run = False

# main program

win = pygame.display.set_mode((screen_width, screen_height))
food = Food()
start()
d = -1 #direction
Snake = [[300, 300]]
food.change = True
last_pos = []
size = 1
font = pygame.font.SysFont('comicsans', 30, True)

main_menu(game_loop)
pygame.quit()
