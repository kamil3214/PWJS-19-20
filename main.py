import pygame
import random

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
HEIGHT = 1080
WIDTH = 1920
w, h = pygame.display.get_surface().get_size()
#window = pygame.set_mode([user_x, user_y], pygame.FULLSCREEN)
#w = pygame.Surface([1920, 1080])

menu = True
game = False
Scoreboard = False
fontBig = pygame.font.SysFont(None, round(300 * w / WIDTH))
fontScore = pygame.font.SysFont(None, round(30 * w / WIDTH))
fontSmall = pygame.font.SysFont(None, round(200 * w / WIDTH))
fontSmall2 = pygame.font.SysFont(None, round(100 * w / WIDTH))
click = False
pygame.display.set_caption("Space Shooter")
carryOn = True
clock = pygame.time.Clock()
#BACKGROUND
background_image = pygame.image.load("assets/backgroundImg.jpg").convert()
background_image = pygame.transform.scale(background_image, (w, h))
loaded = 0
display_score = 0

def player(x,y,health):
    screen.blit(spaceship, (round(x*w/WIDTH),round(y*h/HEIGHT)))
    pygame.draw.rect(screen, (0, 0, 255), (round((x + 25)*w/WIDTH), round((y+160)*h/HEIGHT), round(100*w/WIDTH), round(10*h/HEIGHT)))
    if health < 0:
        health = 0
    pygame.draw.rect(screen,(0,255,0),(round((x + 25)*w/WIDTH), round((y+160)*h/HEIGHT), round(health*w/WIDTH) , round(10*h/HEIGHT)))

def enemy1(x, y, i, health):
    screen.blit(enemy1_Img[i], (round(x*w/WIDTH), round(y*h/HEIGHT)))
    pygame.draw.rect(screen, (0, 0, 255), (round((x + 11)*w/WIDTH), round((y-20)*h/HEIGHT), round(100*w/WIDTH), round(10*h/HEIGHT)))
    if health < 0:
        health = 0
    pygame.draw.rect(screen, (0, 255, 0), (round(x*w/WIDTH), round((y-20)*h/HEIGHT), round(health*w/WIDTH), round(10*h/HEIGHT)))

def enemy2(x, y, i, health):
    screen.blit(enemy2_Img[i], (round(x*w/WIDTH), round(y*h/HEIGHT)))
    pygame.draw.rect(screen, (0, 0, 255), (round(x*w/WIDTH), round((y-20)*h/HEIGHT), round(100*w/WIDTH), round(10*h/HEIGHT)))
    if health < 0:
        health = 0
    pygame.draw.rect(screen, (0, 255, 0), (round(x*w/WIDTH), round((y-20)*h/HEIGHT), round(health*w/WIDTH), round(10*h/HEIGHT)))

def enemy3(x, y, i, health):
    screen.blit(enemy3_Img[i], (round(x*w/WIDTH), round(y*h/HEIGHT)))
    pygame.draw.rect(screen, (0, 0, 255), (round(x*w/WIDTH), round((y-20)*h/HEIGHT), round(100*w/WIDTH), round(10*h/HEIGHT)))
    if health < 0:
        health = 0
    pygame.draw.rect(screen, (0, 255, 0), (round(x*w/WIDTH), round((y-20)*h/HEIGHT), round(health*w/WIDTH), round(10*h/HEIGHT)))

def enemy4(x, y, i, health):
    screen.blit(enemy4_Img[i], (round(x*w/WIDTH), round(y*h/HEIGHT)))
    pygame.draw.rect(screen, (0, 0, 255), (round(x*w/WIDTH), round((y-20)*h/HEIGHT), round(100*w/WIDTH), round(10*h/HEIGHT)))
    if health < 0:
        health = 0
    pygame.draw.rect(screen, (0, 255, 0), (round(x*w/WIDTH), round((y-20)*h/HEIGHT), round(health*w/WIDTH), round(10*h/HEIGHT)))

def enemy1_fire_bullet(x, y, i):
    global enemy1_bullet_state
    enemy1_bullet_state[i] = "fire"
    screen.blit(enemy1_bulletImg[i], (round((x+55)*w/WIDTH), round((y+80)*h/HEIGHT)))

def enemy2_fire_bullet(x, y, i):
    global enemy1_bullet_state
    enemy2_bullet_state[i] = "fire"
    screen.blit(enemy2_bulletImg[i], (round((x+40)*w/WIDTH), round((y+80)*h/HEIGHT)))

def enemy3_fire_bullet(x, y, i):
    global enemy1_bullet_state
    enemy3_bullet_state[i] = "fire"
    screen.blit(enemy3_bulletImg[i], (round((x+45)*w/WIDTH), round((y+120)*h/HEIGHT)))

def enemy4_fire_bullet(x, y, i):
    global enemy1_bullet_state
    enemy4_bullet_state[i] = "fire"
    screen.blit(enemy4_bulletImg[i], (round((x+40)*w/WIDTH), round((y+140)*h/HEIGHT)))


def fire_bullet1(x, y):
    global bullet1_state
    bullet1_state = "fire"
    screen.blit(bullet1Img, (round((x+15)*w/WIDTH), round((y+30)*h/HEIGHT)))

def fire_bullet2(x, y):
    global bullet2_state
    bullet2_state = "fire"
    screen.blit(bullet2Img, (round((x+120)*w/WIDTH), round((y+30)*h/HEIGHT)))

def fire_big_bullet(x, y):
    global big_bullet_state
    big_bullet_state = "fire"
    screen.blit(big_bulletImg, (round((x+52)*w/WIDTH), round((y-20)*h/HEIGHT)))

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#GAME LOOP
while carryOn:
    if loaded == 0:
        score = 0
        # SHIP
        spaceship = pygame.image.load("assets/spaceship.png").convert_alpha()
        spaceship = pygame.transform.scale(spaceship, (round(150*w/WIDTH), round(150*h/HEIGHT)))
        spaceship_mask = pygame.mask.from_surface(spaceship)
        spaceship_x = 885
        spaceship_y = 800
        move_x_left = 0
        move_x_right = 0
        move_y_up = 0
        move_y_down = 0

        # player
        player_health = 100

        # Enemy1
        enemy1_Img = []
        enemy1_health = []
        enemy1_mask = []
        enemy1_x = []
        enemy1_y = []
        enemy1_x_change = []
        enemy1_y_change = []
        num_of_enemies1 = 2
        enemy1Img = pygame.image.load('assets/enemy1.png').convert_alpha()
        for i in range(num_of_enemies1):
            enemy1_Img.append(pygame.transform.scale(enemy1Img, (round(120 * w / WIDTH), round(95 * h / HEIGHT))))
            enemy1_mask.append(pygame.mask.from_surface(enemy1_Img[i]))
            enemy1_x.append(random.randint(0, 1790))
            enemy1_y.append(random.randint(50, 400))
            enemy1_health.append(100)
            enemy1_x_change.append(4)
            enemy1_y_change.append(50)

        # Enemy2
        enemy2_Img = []
        enemy2_mask = []
        enemy2_x = []
        enemy2_health = []
        enemy2_y = []
        enemy2_x_change = []
        enemy2_y_change = []
        num_of_enemies2 = 2
        enemy2Img = pygame.image.load('assets/enemy2.png').convert_alpha()

        for i in range(num_of_enemies2):
            enemy2_Img.append(pygame.transform.scale(enemy2Img, (round(100 * w / WIDTH), round(101 * h / HEIGHT))))
            enemy2_mask.append(pygame.mask.from_surface(enemy2_Img[i]))
            enemy2_x.append(random.randint(0, 1800))
            enemy2_health.append(100)
            enemy2_y.append(random.randint(50, 500))
            enemy2_x_change.append(-5)
            enemy2_y_change.append(50)

        # Enemy3
        enemy3_Img = []
        enemy3_health = []
        enemy3_mask = []
        enemy3_x = []
        enemy3_y = []
        enemy3_x_change = []
        enemy3_y_change = []
        num_of_enemies3 = 2
        enemy3Img = pygame.image.load('assets/enemy3.png').convert_alpha()

        for i in range(num_of_enemies3):
            enemy3_Img.append(pygame.transform.scale(enemy3Img, (round(100 * w / WIDTH), round(120 * h / HEIGHT))))
            enemy3_mask.append(pygame.mask.from_surface(enemy3_Img[i]))
            enemy3_x.append(random.randint(0, 1790))
            enemy3_y.append(random.randint(50, 400))
            enemy3_health.append(100)
            enemy3_x_change.append(4)
            enemy3_y_change.append(50)

        # Enemy4
        enemy4_Img = []
        enemy4_health = []
        enemy4_mask = []
        enemy4_x = []
        enemy4_y = []
        enemy4_x_change = []
        enemy4_y_change = []
        num_of_enemies4 = 2
        enemy4Img = pygame.image.load('assets/enemy4.png').convert_alpha()
        enemy4Img = pygame.transform.scale(enemy4Img, (round(100 * w / WIDTH), round(153 * h / HEIGHT)))

        for i in range(num_of_enemies4):
            enemy4_Img.append(pygame.transform.scale(enemy4Img, (round(100 * w / WIDTH), round(153 * h / HEIGHT))))
            enemy4_mask.append(pygame.mask.from_surface(enemy4_Img[i]))
            enemy4_x.append(random.randint(0, 1790))
            enemy4_y.append(random.randint(50, 400))
            enemy4_health.append(100)
            enemy4_x_change.append(-3)
            enemy4_y_change.append(50)

        # SHIP BULLET
        big_bulletImg = pygame.image.load('assets/big_bullet.png').convert_alpha()
        big_bulletImg = pygame.transform.scale(big_bulletImg, (round(46 * w / WIDTH), round(95 * h / HEIGHT)))
        big_bullet_x = spaceship_x
        big_bullet_y = spaceship_y
        big_bullet_mask = pygame.mask.from_surface(big_bulletImg)
        big_bullet_x_change = 0
        big_bullet_y_change = 30
        big_bullet_counter = 0
        big_bullet_state = "ready"

        bullet1Img = pygame.image.load('assets/bullet1.png').convert_alpha()
        bullet1Img = pygame.transform.scale(bullet1Img, (round(14 * w / WIDTH), round(60 * h / HEIGHT)))
        bullet1_x = spaceship_x
        bullet1_y = spaceship_y
        bullet1_mask = pygame.mask.from_surface(bullet1Img)
        bullet1_x_change = 0
        bullet1_y_change = 50
        bullet1_counter = 0
        bullet1_state = "ready"

        bullet2Img = pygame.image.load('assets/bullet2.png').convert_alpha()
        bullet2Img = pygame.transform.scale(bullet2Img, (round(14 * w / WIDTH), round(60 * h / HEIGHT)))
        bullet2_x = spaceship_x
        bullet2_y = spaceship_y
        bullet2_mask = pygame.mask.from_surface(bullet2Img)
        bullet2_x_change = 0
        bullet2_y_change = 50
        bullet2_counter = 0
        bullet2_state = "ready"

        # ENEMY1 BULLETS
        enemy1_bulletImg = []
        enemy1_bullet_mask = []
        enemy1_bullet_x = []
        enemy1_bullet_y = []
        enemy1_bullet_x_change = []
        enemy1_bullet_y_change = []
        enemy1_bullet_counter = []
        enemy1_bullet_state = []
        enemy1bulletImg = pygame.image.load('assets/enemy_bullet1.png').convert_alpha()
        enemy1bulletImg = pygame.transform.scale(enemy1bulletImg, (round(16 * w / WIDTH), round(63 * h / HEIGHT)))
        for i in range(num_of_enemies1):
            enemy1_bulletImg.append(enemy1bulletImg)
            enemy1_bullet_mask.append(pygame.mask.from_surface(enemy1_bulletImg[i]))
            enemy1_bullet_x.append(enemy1_x[i])
            enemy1_bullet_y.append(enemy1_y[i])
            enemy1_bullet_x_change.append(0)
            enemy1_bullet_y_change.append(-10)
            enemy1_bullet_counter.append(random.randint(0, 100))
            enemy1_bullet_state.append("")

        # ENEMY2 BULLETS
        enemy2_bulletImg = []
        enemy2_bullet_mask = []
        enemy2_bullet_x = []
        enemy2_bullet_y = []
        enemy2_bullet_x_change = []
        enemy2_bullet_y_change = []
        enemy2_bullet_counter = []
        enemy2_bullet_state = []
        enemy2bulletImg = pygame.image.load('assets/enemy_bullet2.png').convert_alpha()
        enemy2bulletImg = pygame.transform.scale(enemy2bulletImg, (round(25 * w / WIDTH), round(100 * h / HEIGHT)))
        for i in range(num_of_enemies2):
            enemy2_bulletImg.append(enemy2bulletImg)
            enemy2_bullet_mask.append(pygame.mask.from_surface(enemy2_bulletImg[i]))
            enemy2_bullet_x.append(enemy2_x[i])
            enemy2_bullet_y.append(enemy2_y[i])
            enemy2_bullet_x_change.append(0)
            enemy2_bullet_y_change.append(-10)
            enemy2_bullet_counter.append(random.randint(0, 100))
            enemy2_bullet_state.append("")

        # ENEMY3 BULLETS
        enemy3_bulletImg = []
        enemy3_bullet_mask = []
        enemy3_bullet_x = []
        enemy3_bullet_y = []
        enemy3_bullet_x_change = []
        enemy3_bullet_y_change = []
        enemy3_bullet_counter = []
        enemy3_bullet_state = []
        enemy3bulletImg = pygame.image.load('assets/enemy_bullet3.png').convert_alpha()
        enemy3bulletImg = pygame.transform.scale(enemy3bulletImg, (round(11 * w / WIDTH), round(86 * h / HEIGHT)))
        for i in range(num_of_enemies3):
            enemy3_bulletImg.append(enemy3bulletImg)
            enemy3_bullet_mask.append(pygame.mask.from_surface(enemy3_bulletImg[i]))
            enemy3_bullet_x.append(enemy3_x[i])
            enemy3_bullet_y.append(enemy3_y[i])
            enemy3_bullet_x_change.append(0)
            enemy3_bullet_y_change.append(-10)
            enemy3_bullet_counter.append(random.randint(0, 100))
            enemy3_bullet_state.append("")

        # ENEMY4 BULLETS
        enemy4_bulletImg = []
        enemy4_bullet_mask = []
        enemy4_bullet_x = []
        enemy4_bullet_y = []
        enemy4_bullet_x_change = []
        enemy4_bullet_y_change = []
        enemy4_bullet_counter = []
        enemy4_bullet_state = []
        enemy4bulletImg = pygame.image.load('assets/enemy_bullet4.png').convert_alpha()
        enemy4bulletImg = pygame.transform.scale(enemy4bulletImg, (round(20 * w / WIDTH), round(27 * h / HEIGHT)))
        for i in range(num_of_enemies4):
            enemy4_bulletImg.append(enemy4bulletImg)
            enemy4_bullet_mask.append(pygame.mask.from_surface(enemy4_bulletImg[i]))
            enemy4_bullet_x.append(enemy4_x[i])
            enemy4_bullet_y.append(enemy4_y[i])
            enemy4_bullet_x_change.append(0)
            enemy4_bullet_y_change.append(-10)
            enemy4_bullet_counter.append(random.randint(0, 100))
            enemy4_bullet_state.append("")

        loaded = 1
    if menu == True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    carryOn = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        screen.blit(background_image, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(round(660 * w / WIDTH), round(435 * h / HEIGHT), round(600 * w / WIDTH), round(165 * h / HEIGHT))
        button_2 = pygame.Rect(round(660 * w / WIDTH), round(735 * h / HEIGHT), round(600 * w / WIDTH), round(165 * h / HEIGHT))
        if button_1.collidepoint((mx, my)):
            if click:
                menu = False
                game = True
        if button_2.collidepoint((mx, my)):
            if click:
                carryOn=False
        pygame.draw.rect(screen, (255, 255, 255), button_1)
        pygame.draw.rect(screen, (255, 255, 255), button_2)
        draw_text('Space Shooter', fontBig, (255, 255, 255), screen, round(230 * w / WIDTH), round(100 * h / HEIGHT))
        draw_text('Play', fontSmall, (0, 0, 0), screen, round(810 * w / WIDTH), round(450 * h / HEIGHT))
        draw_text('Exit', fontSmall, (0, 0, 0), screen, round(810 * w / WIDTH), round(750 * h / HEIGHT))
        click = False
        pygame.display.update()

    if Scoreboard == True:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    carryOn = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.draw.rect(screen, (255, 255, 255),(0, round(135 * h / HEIGHT), round(1920 * w / WIDTH), round(165 * h / HEIGHT)))
        draw_text('Score: ' + str(display_score), fontSmall, (0, 0, 0), screen, round(600 * w / WIDTH),round(150 * h / HEIGHT))
        button_3 = pygame.Rect(round(710 * w / WIDTH), round(535 * h / HEIGHT), round(500 * w / WIDTH),round(100 * h / HEIGHT))
        button_4 = pygame.Rect(round(710 * w / WIDTH), round(835 * h / HEIGHT), round(500 * w / WIDTH),round(100 * h / HEIGHT))
        pygame.draw.rect(screen, (255, 255, 255), button_3)
        pygame.draw.rect(screen, (255, 255, 255), button_4)
        draw_text('Play Again', fontSmall2, (0, 0, 0), screen, round(785 * w / WIDTH), round(550 * h / HEIGHT))
        draw_text('Main menu', fontSmall2, (0, 0, 0), screen, round(775 * w / WIDTH), round(850 * h / HEIGHT))
        if button_3.collidepoint((mx, my)):
            if click:
                Scoreboard = False
                game = True
        if button_4.collidepoint((mx, my)):
            if click:
                Scoreboard = False
                menu = True
        click = False
        pygame.display.update()
    if game == True:
        clock.tick(60)
        screen.blit(background_image, (0, 0))
        start_ticks = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game = False
                    loaded = 0
                    menu = True
            #KEY EVENTS
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_x_left = -10
                if event.key == pygame.K_RIGHT:
                    move_x_right = 10
                if event.key == pygame.K_UP:
                    move_y_up = -10
                if event.key == pygame.K_DOWN:
                    move_y_down = 10


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_x_left = 0
                if event.key == pygame.K_RIGHT:
                    move_x_right = 0
                if event.key == pygame.K_UP:
                    move_y_up = 0
                if event.key == pygame.K_DOWN:
                    move_y_down = 0

        #SHIP_MOVEMENT
        spaceship_x += move_x_left + move_x_right
        if spaceship_x < 0:
            spaceship_x = 0
        if spaceship_x > WIDTH - 150:
            spaceship_x = WIDTH - 150
        spaceship_y += move_y_up + move_y_down
        if spaceship_y < 0:
            spaceship_y = 0
        if spaceship_y > HEIGHT - 150:
            spaceship_y = HEIGHT - 150

        #ENEMY1 MOVEMENT
        for i in range(num_of_enemies1):
            enemy1_x[i] += enemy1_x_change[i]
            if enemy1_y[i] > 1080:
                enemy1_health[i] = 0
            if enemy1_x[i] <= 0:
                enemy1_x_change[i] = 5
                enemy1_y[i] += enemy1_y_change[i]
            elif enemy1_x[i] >= 1800:
                enemy1_x_change[i] = -5
                enemy1_y[i] += enemy1_y_change[i]
            enemy1(enemy1_x[i], enemy1_y[i], i, enemy1_health[i])

            if enemy1_bullet_counter[i] > 110:
                enemy1_bullet_state[i] = "ready"
                enemy1_bullet_counter[i] = 0

            if enemy1_bullet_state[i] is "ready":
                enemy1_bullet_x[i] = enemy1_x[i]
                enemy1_bullet_y[i] = enemy1_y[i]
                enemy1_fire_bullet(enemy1_bullet_x[i], enemy1_bullet_y[i], i)

            if enemy1_bullet_state[i] is "fire":
                enemy1_fire_bullet(enemy1_bullet_x[i], enemy1_bullet_y[i], i)
                enemy1_bullet_y[i] -= enemy1_bullet_y_change[i]

            offset_collision_es = (round((spaceship_x - enemy1_x[i]) * w / WIDTH), round((spaceship_y - enemy1_y[i]) * h / HEIGHT))
            offset_bullet_es = (round((spaceship_x - enemy1_bullet_x[i]-55)*w/WIDTH), round((spaceship_y - enemy1_bullet_y[i]-80)*h/HEIGHT))
            hit_collision_es = enemy1_mask[i].overlap(spaceship_mask, offset_collision_es)
            hit_bullet_es = enemy1_bullet_mask[i].overlap(spaceship_mask, offset_bullet_es)
            if hit_bullet_es != None:
                enemy1_bullet_y[i] += 1080
                player_health -= 10
            if hit_collision_es != None:
                player_health = 0

            offset_bullet1_se = (round((enemy1_x[i] - bullet1_x-15)*w/WIDTH), round((enemy1_y[i] - bullet1_y-30)*h/HEIGHT))
            hit_bullet1_se = bullet1_mask.overlap(enemy1_mask[i], offset_bullet1_se)
            if hit_bullet1_se != None:
                bullet1_y -= 1080
                enemy1_health[i] -= 10

            offset_bullet2_se = (round((enemy1_x[i] - bullet2_x-120)*w/WIDTH), round((enemy1_y[i] - bullet2_y-30)*h/HEIGHT))
            hit_bullet2_se = bullet2_mask.overlap(enemy1_mask[i], offset_bullet2_se)
            if hit_bullet2_se != None:
                bullet2_y -= 1080
                enemy1_health[i] -= 10

            offset_big_bullet_se = (round((enemy1_x[i] - big_bullet_x-52)*w/WIDTH), round((enemy1_y[i] - big_bullet_y+20)*h/HEIGHT))
            hit_big_bullet_se = big_bullet_mask.overlap(enemy1_mask[i], offset_big_bullet_se)
            if hit_big_bullet_se != None:
                big_bullet_y -= 1080
                enemy1_health[i] -= 20

            if enemy1_health[i] <= 0:
                enemy1_health[i] = 100
                enemy1_x[i] = random.randint(0, 1790)
                enemy1_y[i] = random.randint(50, 150)
                enemy1_x_change[i] *= -1

        #ENEMY2 MOVEMENT
        for i in range(num_of_enemies2):
            enemy2_x[i] += enemy2_x_change[i]
            if enemy2_y[i] > 1080:
                enemy2_health[i] = 0
            if enemy2_x[i] <= 0:
                enemy2_x_change[i] = 5
                enemy2_y[i] += enemy2_y_change[i]
            elif enemy2_x[i] >= 1820:
                enemy2_x_change[i] = -5
                enemy2_y[i] += enemy2_y_change[i]
            enemy2(enemy2_x[i], enemy2_y[i], i, enemy2_health[i])

            if enemy2_bullet_counter[i] > 110:
                enemy2_bullet_state[i] = "ready"
                enemy2_bullet_counter[i] = 0

            if enemy2_bullet_state[i] is "ready":
                enemy2_bullet_x[i] = enemy2_x[i]
                enemy2_bullet_y[i] = enemy2_y[i]
                enemy2_fire_bullet(enemy2_bullet_x[i], enemy2_bullet_y[i], i)

            if enemy2_bullet_state[i] is "fire":
                enemy2_fire_bullet(enemy2_bullet_x[i], enemy2_bullet_y[i], i)
                enemy2_bullet_y[i] -= enemy2_bullet_y_change[i]

            offset_collision_es = (round((spaceship_x - enemy2_x[i]) * w / WIDTH), round((spaceship_y - enemy2_y[i]) * h / HEIGHT))
            offset_bullet_es = (round((spaceship_x - enemy2_bullet_x[i]-40)*w/WIDTH), round((spaceship_y - enemy2_bullet_y[i]-80)*h/HEIGHT))
            hit_collision_es = enemy2_mask[i].overlap(spaceship_mask, offset_collision_es)
            hit_bullet_es = enemy2_bullet_mask[i].overlap(spaceship_mask, offset_bullet_es)
            if hit_bullet_es != None:
                enemy2_bullet_y[i] += 1080
                player_health -= 10
            if hit_collision_es != None:
                player_health = 0

            offset_bullet1_se = (round((enemy2_x[i] - bullet1_x-15)*w/WIDTH), round((enemy2_y[i] - bullet1_y-30)*h/HEIGHT))
            hit_bullet1_se = bullet1_mask.overlap(enemy2_mask[i], offset_bullet1_se)
            if hit_bullet1_se != None:
                bullet1_y -= 1080
                enemy2_health[i] -= 25

            offset_bullet1_se = (round((enemy2_x[i] - bullet1_x-15)*w/WIDTH), round((enemy2_y[i] - bullet1_y-30)*h/HEIGHT))
            hit_bullet1_se = bullet1_mask.overlap(enemy2_mask[i], offset_bullet1_se)
            if hit_bullet1_se != None:
                bullet1_y -= 1080
                enemy2_health[i] -= 25

            offset_bullet2_se = (round((enemy2_x[i] - bullet2_x-120)*w/WIDTH), round((enemy2_y[i] - bullet2_y-30)*h/HEIGHT))
            hit_bullet2_se = bullet2_mask.overlap(enemy2_mask[i], offset_bullet2_se)
            if hit_bullet2_se != None:
                bullet2_y -= 1080
                enemy2_health[i] -= 25
                
            offset_big_bullet_se = (round((enemy2_x[i] - big_bullet_x-52)*w/WIDTH), round((enemy2_y[i] - big_bullet_y+20)*h/HEIGHT))
            hit_big_bullet_se = big_bullet_mask.overlap(enemy2_mask[i], offset_big_bullet_se)
            if hit_big_bullet_se != None:
                big_bullet_y -= 1080
                enemy2_health[i] -= 50

            if enemy2_health[i] <= 0:
                enemy2_health[i] = 100
                enemy2_x[i] = random.randint(0, 1790)
                enemy2_y[i] = random.randint(50, 150)
                enemy2_x_change[i] *= -1

        #ENEMY3 MOVEMENT
        for i in range(num_of_enemies3):
            enemy3_x[i] += enemy3_x_change[i]
            if enemy3_y[i] > 1080:
                enemy3_health[i] = 0
            if enemy3_x[i] <= 0:
                enemy3_x_change[i] = 5
                enemy3_y[i] += enemy3_y_change[i]
            elif enemy3_x[i] >= 1820:
                enemy3_x_change[i] = -5
                enemy3_y[i] += enemy3_y_change[i]
            enemy3(enemy3_x[i], enemy3_y[i], i, enemy3_health[i])

            if enemy3_bullet_counter[i] > 110:
                enemy3_bullet_state[i] = "ready"
                enemy3_bullet_counter[i] = 0

            if enemy3_bullet_state[i] is "ready":
                enemy3_bullet_x[i] = enemy3_x[i]
                enemy3_bullet_y[i] = enemy3_y[i]
                enemy3_fire_bullet(enemy3_bullet_x[i], enemy3_bullet_y[i], i)

            if enemy3_bullet_state[i] is "fire":
                enemy3_fire_bullet(enemy3_bullet_x[i], enemy3_bullet_y[i], i)
                enemy3_bullet_y[i] -= enemy3_bullet_y_change[i]

            offset_collision_es = (round((spaceship_x - enemy3_x[i]) * w / WIDTH), round((spaceship_y - enemy3_y[i]) * h / HEIGHT))
            offset_bullet_es = (round((spaceship_x - enemy3_bullet_x[i]-45)*w/WIDTH), round((spaceship_y - enemy3_bullet_y[i]-120)*h/HEIGHT))
            hit_collision_es = enemy3_mask[i].overlap(spaceship_mask, offset_collision_es)
            hit_bullet_es = enemy3_bullet_mask[i].overlap(spaceship_mask, offset_bullet_es)
            if hit_bullet_es != None:
                enemy3_bullet_y[i] += 1080
                player_health -= 10
            if hit_collision_es != None:
                player_health = 0

            offset_bullet1_se = (round((enemy3_x[i] - bullet1_x-15)*w/WIDTH), round((enemy3_y[i] - bullet1_y-30)*h/HEIGHT))
            hit_bullet1_se = bullet1_mask.overlap(enemy3_mask[i], offset_bullet1_se)
            if hit_bullet1_se != None:
                bullet1_y -= 1080
                enemy3_health[i] -= 15

            offset_bullet2_se = (round((enemy3_x[i] - bullet2_x-120)*w/WIDTH), round((enemy3_y[i] - bullet2_y-30)*h/HEIGHT))
            hit_bullet2_se = bullet2_mask.overlap(enemy3_mask[i], offset_bullet2_se)
            if hit_bullet2_se != None:
                bullet2_y -= 1080
                enemy3_health[i] -= 15

            offset_big_bullet_se = (round((enemy3_x[i] - big_bullet_x-52)*w/WIDTH), round((enemy3_y[i] - big_bullet_y+20)*h/HEIGHT))
            hit_big_bullet_se = big_bullet_mask.overlap(enemy3_mask[i], offset_big_bullet_se)
            if hit_big_bullet_se != None:
                big_bullet_y -= 1080
                enemy3_health[i] -= 30

            if enemy3_health[i] <= 0:
                enemy3_health[i] = 100
                enemy3_x[i] = random.randint(0, 1790)
                enemy3_y[i] = random.randint(50, 150)
                enemy3_x_change[i] *= -1

        #ENEMY4 MOVEMENT
        for i in range(num_of_enemies4):
            enemy4_x[i] += enemy4_x_change[i]
            if enemy4_y[i] > 1080:
                enemy4_health[i] = 0
            if enemy4_x[i] <= 0:
                enemy4_x_change[i] = 3
                enemy4_y[i] += enemy3_y_change[i]
            elif enemy4_x[i] >= 1800:
                enemy4_x_change[i] = -3
                enemy4_y[i] += enemy4_y_change[i]
            enemy4(enemy4_x[i], enemy4_y[i], i, enemy4_health[i])

            if enemy4_bullet_counter[i] > 130:
                enemy4_bullet_state[i] = "ready"
                enemy4_bullet_counter[i] = 0

            if enemy4_bullet_state[i] is "ready":
                enemy4_bullet_x[i] = enemy4_x[i]
                enemy4_bullet_y[i] = enemy4_y[i]
                enemy4_fire_bullet(enemy4_bullet_x[i], enemy4_bullet_y[i], i)

            if enemy4_bullet_state[i] is "fire":
                enemy4_fire_bullet(enemy4_bullet_x[i], enemy4_bullet_y[i], i)
                enemy4_bullet_y[i] -= enemy4_bullet_y_change[i]

            offset_collision_es = (round((spaceship_x - enemy4_x[i]) * w / WIDTH), round((spaceship_y - enemy4_y[i]) * h / HEIGHT))
            offset_bullet_es = (round((spaceship_x - enemy4_bullet_x[i]-40)*w/WIDTH), round((spaceship_y - enemy4_bullet_y[i]-140)*h/HEIGHT))
            hit_collision_es = enemy4_mask[i].overlap(spaceship_mask, offset_collision_es)
            hit_bullet_es = enemy4_bullet_mask[i].overlap(spaceship_mask, offset_bullet_es)
            if hit_bullet_es != None:
                enemy4_bullet_y[i] += 1080
                player_health -= 10
            if hit_collision_es != None:
                player_health = 0

            offset_bullet1_se = (round((enemy4_x[i] - bullet1_x-15)*w/WIDTH), round((enemy4_y[i] - bullet1_y-30)*h/HEIGHT))
            hit_bullet1_se = bullet1_mask.overlap(enemy4_mask[i], offset_bullet1_se)
            if hit_bullet1_se != None:
                bullet1_y -= 1080
                enemy4_health[i] -= 15

            offset_bullet2_se = (round((enemy4_x[i] - bullet2_x-120)*w/WIDTH), round((enemy4_y[i] - bullet2_y-30)*h/HEIGHT))
            hit_bullet2_se = bullet2_mask.overlap(enemy4_mask[i], offset_bullet2_se)
            if hit_bullet2_se != None:
                bullet2_y -= 1080
                enemy4_health[i] -= 15

            offset_big_bullet_se = (round((enemy4_x[i] - big_bullet_x-52)*w/WIDTH), round((enemy4_y[i] - big_bullet_y+20)*h/HEIGHT))
            hit_big_bullet_se = big_bullet_mask.overlap(enemy4_mask[i], offset_big_bullet_se)
            if hit_big_bullet_se != None:
                big_bullet_y -= 1080
                enemy4_health[i] -= 30

            if enemy4_health[i] <= 0:
                enemy4_health[i] = 100
                enemy4_x[i] = random.randint(0, 1790)
                enemy4_y[i] = random.randint(50, 150)
                enemy4_x_change[i] *= -1



        # Bullet Movement
        if bullet1_counter > 20:
            bullet1_state = "ready"
            bullet1_counter = 0

        if bullet1_state is "ready":
            bullet1_x = spaceship_x
            bullet1_y = spaceship_y
            fire_bullet1(bullet1_x, bullet1_y)

        if bullet1_state is "fire":
            fire_bullet1(bullet1_x, bullet1_y)
            bullet1_y -= bullet1_y_change

        if bullet2_counter > 20:
            bullet2_state = "ready"
            bullet2_counter = 0

        if bullet2_state is "ready":
            bullet2_x = spaceship_x
            bullet2_y = spaceship_y
            fire_bullet2(bullet2_x, bullet2_y)

        if bullet2_state is "fire":
            fire_bullet2(bullet2_x, bullet2_y)
            bullet2_y -= bullet2_y_change

        if big_bullet_counter > 60:
            big_bullet_state = "ready"
            big_bullet_counter = 0

        if big_bullet_state is "ready":
            big_bullet_x = spaceship_x
            big_bullet_y = spaceship_y
            fire_big_bullet(bullet1_x, bullet1_y)

        if big_bullet_state is "fire":
            fire_big_bullet(big_bullet_x, big_bullet_y)
            big_bullet_y -= big_bullet_y_change

        for i in range(num_of_enemies1):
            enemy1_bullet_counter[i] += 1

        for i in range(num_of_enemies2):
            enemy2_bullet_counter[i] += 1

        for i in range(num_of_enemies4):
            enemy3_bullet_counter[i] += 1

        for i in range(num_of_enemies4):
            enemy4_bullet_counter[i] += 1

        bullet1_counter += 1
        bullet2_counter += 1
        big_bullet_counter += 1
        player(spaceship_x, spaceship_y,player_health)
        if player_health <= 0:
            display_score = score + 1
            loaded = 0
            game = False
            pygame.display.update()
            Scoreboard = True

        score += 1
        draw_text('Score: '+str(score), fontScore, (255, 255, 255), screen, 20, 20)
        pygame.display.update()