import pygame
# клас-батько для спрайтів
class GameSprite(pygame.sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = pygame.transform.scale(pygame.image.load(player_image), (60, 60))
        self.speed = player_speed
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# клас-спадкоємець для спрайту-гравця (керується стрілками)
class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

# клас-спадкоємець для спрайта-ворога (переміщається сам)
class Enemy(GameSprite):
    direction = "left"

    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

# клас для спрайтів-перешкод
class Wall(pygame.sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        # картинка стіни - прямокутник потрібних розмірів та кольору
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        # кожен спрайт повинен зберігати властивість rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        #draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))


# Ігрова сцена:
win_width = 700
win_height = 500

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Maze")
background = pygame.transform.scale(pygame.image.load(
    "thespace.jpg"), (win_width, win_height))

# Персонажі гри:
player = Player('pngwing.com (2).png', 5, win_height - 80, 4)
monster = Enemy('qwer.png', win_width - 80, 280, 2)
final = GameSprite('akym.png', win_width - 120, win_height - 80, 0)

# стіни
w1 = Wall(154, 205, 50, 80, 80, 10, 500)
w2 = Wall(154, 205, 50, 80, 480, 450, 10)
w3 = Wall(154, 205, 50, 180, 400, 350, 10)
#w4 = Wall(154, 205, 50, 525, 400, 10, 100)
w5 = Wall(154, 205, 50, 180, 0, 10, 320)
w6 = Wall(154, 205, 50, 180, 310, 200, 10)
w7 = Wall(154, 205, 50, 460, 230, 10, 170)
w8 = Wall(154, 205, 50, 270, 230, 200, 10)
w9 = Wall(154, 205, 50, 270, 75, 10, 165)
w10 = Wall(154, 205, 50, 360, 0, 10, 160)
w11 = Wall(154, 205, 50, 460, 75, 10, 165)
w12 = Wall(154, 205, 50, 460, 75, 135, 10)
w13 = Wall(154, 205, 50, 555, 180, 190, 10)

game = True
finish = False
clock = pygame.time.Clock()
FPS = 60

'''# написи'''
pygame.font.init()
font = pygame.font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

# музика
pygame.mixer.init()
pygame.mixer.music.load('space.ogg')
pygame.mixer.music.play()

money =pygame.mixer.Sound('money.ogg')
kick = pygame.mixer.Sound('kick.ogg')

# ...

while game:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game = False

    if finish != True:
        window.blit(background,(0, 0))
        
        player.update()
        monster.update()
       
        
        player.reset()
        monster.reset()
        final.reset()
        
        
        
        
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        #w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()
        

    if (pygame.sprite.collide_rect(player, monster) or 
        pygame.sprite.collide_rect(player, w1) or 
        pygame.sprite.collide_rect(player, w2) or
        pygame.sprite.collide_rect(player, w3) or
        #pygame.sprite.collide_rect(player, w4) or 
        pygame.sprite.collide_rect(player, w5) or 
        pygame.sprite.collide_rect(player, w6) or
        pygame.sprite.collide_rect(player, w7) or
        pygame.sprite.collide_rect(player, w8) or
        pygame.sprite.collide_rect(player, w9) or
        pygame.sprite.collide_rect(player, w10) or
        pygame.sprite.collide_rect(player, w11) or
        pygame.sprite.collide_rect(player, w12) or
        pygame.sprite.collide_rect(player, w13)):
        finish = True
        window.blit(lose, (200,200))
        kick.play()
        
        # Натисніть "Space" для рестарту
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            finish = False
            player.rect.x = 5
            player.rect.y = win_height - 80

    if pygame.sprite.collide_rect(player, final) :
        finish = True
        window.blit(win, (200,200))
        money.play()
        for i in range(100):
            i += 1
        break

    pygame.display.update()
    clock.tick(FPS)



window2 = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Maze2")
background2 = pygame.transform.scale(pygame.image.load("64.jpg"), (win_width, win_height))



playerW = False
playerS = False
playerA = False
playerD = False
player1 = Player('pngwing.com (2).png', 5, win_height - 80, 4)
monster1 = Enemy('monster.png', win_width - 80, 280, 2)
final1 = GameSprite('motor.png', win_width - 120, win_height - 80, 0)
kick1 = pygame.mixer.Sound('kick.ogg')
while True:
    window2.blit(background2, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerW = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                playerW = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                playerS = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                playerS = False
    if playerW:
        player1.rect.y -= 10
    if playerS:
        player1.rect.y += 10
    
    if player1.rect.x < 5:
        player1.rect.x = player1.rect.x
    player1.update()
    final1.update()
    monster1.update()
    player1.reset()
    final1.reset()
    monster1.reset()

    w1 = Wall(154, 205, 50, 80, 80, 10, 500)
    w2 = Wall(154, 205, 50, 80, 480, 450, 10)
    w3 = Wall(154, 205, 50, 180, 400, 350, 10)
    #w4 = Wall(154, 205, 50, 525, 400, 10, 100)
    w5 = Wall(154, 205, 50, 180, 0, 10, 320)
    w6 = Wall(154, 205, 50, 180, 310, 200, 10)
    w7 = Wall(154, 205, 50, 460, 230, 10, 170)
    w8 = Wall(154, 205, 50, 270, 230, 200, 10)
    w9 = Wall(154, 205, 50, 270, 75, 10, 165)
    w10 = Wall(154, 205, 50, 360, 0, 10, 160)
    w11 = Wall(154, 205, 50, 460, 75, 10, 165)
    w12 = Wall(154, 205, 50, 460, 75, 135, 10)
    w13 = Wall(154, 205, 50, 555, 180, 190, 10)
    
    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()
    #w4.draw_wall()
    w5.draw_wall()
    w6.draw_wall()
    w7.draw_wall()
    w8.draw_wall()
    w9.draw_wall()
    w10.draw_wall()
    w11.draw_wall()
    w12.draw_wall()
    w13.draw_wall()
    
    if (pygame.sprite.collide_rect(player1, final1,) or 
        pygame.sprite.collide_rect(player1, monster1) or
        pygame.sprite.collide_rect(player1, w1) or 
        pygame.sprite.collide_rect(player1, w2) or
        pygame.sprite.collide_rect(player1, w3) or
        #pygame.sprite.collide_rect(player1, w4) or 
        pygame.sprite.collide_rect(player1, w5) or 
        pygame.sprite.collide_rect(player1, w6) or
        pygame.sprite.collide_rect(player1, w7) or
        pygame.sprite.collide_rect(player1, w8) or
        pygame.sprite.collide_rect(player1, w9) or
        pygame.sprite.collide_rect(player1, w10) or
        pygame.sprite.collide_rect(player1, w11) or
        pygame.sprite.collide_rect(player1, w12) or
        pygame.sprite.collide_rect(player1, w13)):
        finish = True
        window.blit(lose, (200,200))
        kick1.play()
        break


    pygame.display.update()
    clock.tick(60)
    