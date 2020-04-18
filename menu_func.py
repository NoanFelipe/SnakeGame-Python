import pygame, sys
from file_func import *

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Snake')
screen = pygame.display.set_mode((600, 600),0,32)
 
font = pygame.font.SysFont('comicsans', 75)
font1 = pygame.font.SysFont('comicsans', 25)

snake_image_blue = pygame.image.load('blue.png')
snake_image_blue = pygame.transform.scale(snake_image_blue, (100, 100))

snake_image_green = pygame.image.load('green.png')
snake_image_green = pygame.transform.scale(snake_image_green, (100, 100))

snake_image_br = pygame.image.load('br.png')
snake_image_br = pygame.transform.scale(snake_image_br, (100, 100))

snake_image_usa = pygame.image.load('usa.png')
snake_image_usa = pygame.transform.scale(snake_image_usa, (100, 100))

def create_buttom(rect, surface, color, text, font, ColorTxt, x, y):
    pygame.draw.rect(surface, color, rect)
    draw_text(text, font, ColorTxt, surface, x, y)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu(func):
    click = False
    while True:
        screen.fill((0,0,0))

        json_read = ReadJsonFile('player_info.json')
        player_info = []
        player_info.append(json_read)

        draw_text('THE SNAKE GAME', font, (25, 255, 25), screen, 60, 160)
        draw_text('Press Esc to quit', font1, (255,255,255), screen, 425, 30)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(200, 320, 200, 60)
        button_2 = pygame.Rect(200, 400, 200, 60)

        if button_1.collidepoint((mx, my)):
            if click:
                init_gold = player_info[0][0]['gold']
                func()
                lose_screen(init_gold)
                
        create_buttom(button_1, screen, (255, 255, 255), 'Play', font, (0, 0, 0), 245, 325)

        if button_2.collidepoint((mx, my)):
            if click:
                shop()
        create_buttom(button_2, screen, (255,255,255), 'Shop', font, (0,0,0), 235, 407)

        gold = player_info[0][0]['gold']
        draw_text(f'${gold}', font, (255, 255, 0), screen, 30, 30)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        del player_info

        pygame.display.update()
        mainClock.tick(60)


def shop():
    running = True
    click = False
    show_bought_text = False
    c = 0
    buy_button = False
    x = 0
    is_buying = -1

    json_read = ReadJsonFile('player_info.json')
    player_info = []
    player_info.append(json_read)

    is_equip = 0

    equip_button = False
    while running:
        test_button = pygame.Rect(x, 484, 85, 40)
        font2 = pygame.font.SysFont('comicsans', 35)
        screen.fill((0,0,0))
        draw_text('Press Esc to quit', font1, (255,255,255), screen, 425, 30)
        
        if c > 0:
            draw_text('You dont have enough gold!', font2, (255, 255, 255), screen, 135, 550)
            if c > 60:
                c = 60
            c -= 1

        if buy_button:
            create_buttom(test_button, screen, (255, 255, 255), 'Buy', font2, (0,0,0), x + 17, 491)
            if is_buying == 1 or is_buying == 2:
                draw_text('R$1000', font2, (255, 255, 0), screen, x, 455)
            else:
                draw_text('R$2000', font2, (255, 255, 0), screen, x, 455)

        if equip_button:
            create_buttom(test_button, screen, (255, 255, 255), 'Equip', font2, (0,0,0), x + 7, 491)

        json_read = ReadJsonFile('player_info.json')
        player_info = []
        player_info.append(json_read)
        gold = player_info[0][0]['gold']

        mx, my = pygame.mouse.get_pos()
        
        test_button_1 = pygame.Rect(175, 350, 100, 100)
        test_button_2 = pygame.Rect(325, 350, 100, 100)
        test_button_3 = pygame.Rect(35, 350, 100, 100)
        test_button_4 = pygame.Rect(465, 350, 100, 100)

        if test_button_1.collidepoint((mx, my)):
            if click:
                if not player_info[0][0]['green']:
                    is_buying = 1
                    buy_button = True
                    equip_button = False
                    x = 183
                else:
                    x = 183
                    is_equip = 1
                    equip_button = True
                    buy_button = False
        
        if buy_button:
            if test_button.collidepoint((mx,my)):
                if click:
                    if not player_info[0][0]['green']:
                        if is_buying == 1:
                            if player_info[0][0]['gold'] >= 1000:
                                player_info[0][0]['gold'] -= 1000
                                player_info[0][0]['green'] = True
                                buy_button = False
                                WriteOnJsonFile(player_info[0], 'player_info.json')
                            else:
                                c += 60
        
        
        if equip_button:
            if test_button.collidepoint((mx,my)):
                if click:
                    if player_info[0][0]['green']:
                        if is_equip == 1:
                            player_info[0][0]['equiped'] = 1
                            equip_button = False
                            WriteOnJsonFile(player_info[0], 'player_info.json')
        
        screen.blit(snake_image_green, (175, 350))

        if test_button_2.collidepoint((mx, my)):
            if click:
                if not player_info[0][0]['blue']:
                    is_buying = 2
                    buy_button = True
                    equip_button = False
                    x = 332
                else:
                    x = 332
                    is_equip = 2
                    equip_button = True  
                    buy_button = False
                        
            
        if buy_button:
            if test_button.collidepoint((mx,my)):
                if click:
                    if not player_info[0][0]['blue']:
                        if is_buying == 2:
                            if player_info[0][0]['gold'] >= 1000:
                                player_info[0][0]['gold'] -= 1000
                                buy_button = False
                                WriteOnJsonFile(player_info[0], 'player_info.json')
                                player_info[0][0]['blue'] = True
                            else:
                                c += 60
                    
        if equip_button:
            if test_button.collidepoint((mx,my)):
                if click:
                    if player_info[0][0]['blue']:
                        if is_equip == 2:
                            player_info[0][0]['equiped'] = 2
                            equip_button = False
                            WriteOnJsonFile(player_info[0], 'player_info.json')

        screen.blit(snake_image_blue, (325, 350))

        if test_button_3.collidepoint((mx, my)):
            if click:
                if not player_info[0][0]['br']:
                    is_buying = 3
                    buy_button = True
                    equip_button = False
                    x = 42
                else:
                    x = 42
                    is_equip = 3
                    equip_button = True
                    buy_button = False
            
        if buy_button:
            if test_button.collidepoint((mx,my)):
                if click:
                    if not player_info[0][0]['br']:
                        if is_buying == 3:
                            if player_info[0][0]['gold'] >= 2000:
                                player_info[0][0]['gold'] -= 2000
                                player_info[0][0]['br'] = True
                                buy_button = False
                                WriteOnJsonFile(player_info[0], 'player_info.json')
                            else:
                                c += 60
        
        if equip_button:
            if test_button.collidepoint((mx,my)):
                if click:
                    if player_info[0][0]['br']:
                        if is_equip == 3:
                            player_info[0][0]['equiped'] = 3
                            equip_button = False
                            WriteOnJsonFile(player_info[0], 'player_info.json')

        screen.blit(snake_image_br, (35, 350))

        if test_button_4.collidepoint((mx, my)):
            if click:
                if not player_info[0][0]['usa']:
                    is_buying = 4
                    buy_button = True
                    equip_button = False
                    x = 472
                else:
                    x = 472
                    is_equip = 4
                    equip_button = True
                    buy_button = False
            
        if buy_button:
            if test_button.collidepoint((mx,my)):
                if click:
                    if not player_info[0][0]['usa']:
                        if is_buying == 4:
                            if player_info[0][0]['gold'] >= 2000:
                                player_info[0][0]['gold'] -= 2000
                                player_info[0][0]['usa'] = True
                                buy_button = False
                                WriteOnJsonFile(player_info[0], 'player_info.json')
                            else:
                                c += 60
        
        if equip_button:
            if test_button.collidepoint((mx,my)):
                if click:
                    if player_info[0][0]['usa']:
                        if is_equip == 4:
                            player_info[0][0]['equiped'] = 4
                            equip_button = False
                            WriteOnJsonFile(player_info[0], 'player_info.json')

        screen.blit(snake_image_usa, (465, 350))

        if click:
            if not test_button.collidepoint((mx, my)):
                if not test_button_1.collidepoint((mx, my)):
                    if not test_button_2.collidepoint((mx, my)):
                        if not test_button_3.collidepoint((mx, my)):
                            if not test_button_4.collidepoint((mx, my)):
                                buy_button = False
                                equip_button = False


        draw_text('Shop', font, (255, 255, 255), screen, 235, 150)
        draw_text(f'${gold}', font, (255, 255, 0), screen, 30, 30)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
       
        pygame.display.update()
        mainClock.tick(60)
        WriteOnJsonFile(player_info[0], 'player_info.json')
        del player_info

def lose_screen(initial_gold):
    run = True
    json_read = ReadJsonFile('player_info.json')
    player_info = []
    player_info.append(json_read)
    font2 = pygame.font.SysFont('comicsans', 50)
    font3 = pygame.font.SysFont('comicsans', 130)
    while run:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
        
        draw_text('Press Esc to quit', font1, (255,255,255), screen, 425, 30)
        draw_text(f'Gold Earned: {player_info[0][0]["gold"] - initial_gold}', font2, (255, 255, 255), screen, 160, 370)
        draw_text(f'Your Size Was: {((player_info[0][0]["gold"] - initial_gold) / 5) + 1:.0f}', font2, (255,255,255), screen, 160, 430)
        draw_text(f'You Lost!', font3, (255, 0, 0), screen, 95, 170)
        draw_text(f'Highscore: {player_info[0][0]["highscore"]}', font2, (255,255,255), screen, 160, 490)

        pygame.display.update()
        mainClock.tick(60)
