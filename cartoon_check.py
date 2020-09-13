# 导入pygame库
import random
import pygame

# 按钮
game_over_bottom_width = 300
game_over_bottom_height = 41
resume_nor_width = 60
resume_nor_height = 45

# 颜色
BLUE = (0,0,255,128)
WHITE = (255,255,255,128)
RED = (255,0,0,128)

# 分数记录
SCORE = 0

# 设置背景全局变量
BACK_HEIGHT = 700
BACK_WIDTH = 480
BGX = 0
BGY = 0
bg_rect = pygame.Rect(BGX,BGY,BACK_WIDTH,BACK_HEIGHT)

# 设置飞机全局变量
ENEMY_WIDTH = 57
ENEMY_HEIGHT = 43
ENEMY_X = random.randint(0, BACK_WIDTH - ENEMY_WIDTH)
ENEMY_Y = BGY - ENEMY_HEIGHT


MEX = bg_rect.centerx - 50
MEY = bg_rect.bottom - 200
ME_WIDTH = 102
ME_HEIGHT = 126
me1_rect = pygame.Rect(MEX,MEY,ME_WIDTH,ME_HEIGHT)

# 子弹的全局变量
BULLET_WIDTH = 5
BULLET_HEIGHT = 11
BULLET_X = me1_rect.centerx
Bullet_Y = MEY - BULLET_HEIGHT
bullet_rect = pygame.Rect(BULLET_X, Bullet_Y, BULLET_WIDTH, BULLET_HEIGHT)
SPEED = 2
BULLET_SUPPLY_WIDTH = 58
BULLET_SUPPLY_HEIGHT = 88

# 定时器
CREATE_ENEMY = pygame.USEREVENT
pygame.time.set_timer(CREATE_ENEMY,1000)

CREATE_BULLET = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_BULLET,1000)

CREATE_BULLET_SUPPLY = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BULLET_SUPPLY,20000)

CREATE_BULLET1 = pygame.USEREVENT + 3

CREATE_BOMB_SUPPLY = pygame.USEREVENT+4
pygame.time.set_timer(CREATE_BOMB_SUPPLY,100000)

# 设置时钟
clock = pygame.time.Clock()

# 初始化pygame
pygame.init()

# 设置窗口和窗口标题
back = pygame.display.set_mode((BACK_WIDTH,BACK_HEIGHT))
pygame.display.set_caption("飞机大战")

# 开始动画参数
FY_width = 480
FY_height = 700

back.fill(WHITE)

start = pygame.image.load("./p/start.png")
start1 = pygame.image.load("./p/start1.png")

pause = pygame.image.load("./p/pi/pause_nor.png")
pause_rect = pygame.rect.Rect(240 - 30,350,60,45)

start_font = pygame.font.Font('freesansbold.ttf', 30)
text2_surface = start_font.render('This is a simple game of plane',
                                  True, BLUE)
text3_surface = start_font.render('wars, only learning, thank you!',
                                  True,BLUE)
text4_surface = start_font.render('Email:linjinhuixxx@126.com',
                                  True, BLUE)
text5_surface = start_font.render('Press W/A/S/D',
                                  True,BLUE)
text6_surface = start_font.render('or UP/LEFT/DOWN/RIGHT',
                                  True,BLUE)
text7_surface = start_font.render('to move the plane',
                                  True,BLUE)
text8_surface = start_font.render('Press the left of the screen to',
                                  True,BLUE)
text9_surface = start_font.render('shut bomb',
                                  True,BLUE)
next_surface = start_font.render('NEXT',
                                 True,RED)

# 炸弹参数
bomb_supply_width = 60
bomb_supply_height = 107

bomb_width = 63
bomb_height = 57

bomb_num = 0

# 精灵类


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, x=0, y=0, width=0, height=0, speed=1):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_name)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Enemy(GameSprite):

    def update(self):
        # 让敌机以1-3速率飞行
        self.speed = random.randint(1, 3)
        # 让敌机从上向下飞行
        self.rect.y += self.speed
        # 判断是否要回收敌机
        if self.rect.y >= BACK_HEIGHT:
            self.kill()


class Me(GameSprite):

    def update(self):
        self.keys_pressed = pygame.key.get_pressed()
        if self.keys_pressed[pygame.K_RIGHT] or self.keys_pressed[pygame.K_d]:
            self.rect.x += SPEED
            if self.rect.x >= BACK_WIDTH - ME_WIDTH:
                self.rect.x = BACK_WIDTH - ME_WIDTH
        if self.keys_pressed[pygame.K_LEFT] or self.keys_pressed[pygame.K_a]:
            self.rect.x -= SPEED
            if self.rect.x <= 0:
                self.rect.x = 0
        if self.keys_pressed[pygame.K_UP] or self.keys_pressed[pygame.K_w]:
            self.rect.y -= SPEED
            if self.rect.y <= 0:
                self.rect.y = 0
        if self.keys_pressed[pygame.K_DOWN] or self.keys_pressed[pygame.K_s]:
            self.rect.y += SPEED
            if self.rect.bottom >= BACK_HEIGHT:
                self.rect.y = BACK_HEIGHT - ME_HEIGHT


class Bullet(GameSprite):

    def update(self):

        # 让子弹从下向上飞
        self.rect.y -= self.speed
        # 判断是否要回收子弹
        if self.rect.y + BULLET_HEIGHT <= 0:
            self.kill()


class Background(GameSprite):

    def update(self):
        super().update()
        if self.rect.y >= BACK_HEIGHT:
            self.rect.bottom = 0

# 检查碰撞


def crash_check():
    global SCORE
    global bomb_num
    # 碰撞检测
    crash_enemy = pygame.sprite.groupcollide(bullet_group, enemy_group, True, True)
    if len(crash_enemy) > 0:
        SCORE += 1

    crash_me = pygame.sprite.groupcollide(me_group, enemy_group, True, True)
    if len(crash_me) > 0:

        i1 = pygame.image.load("./p/pi/me_destroy_1.png")
        i2 = pygame.image.load("./p/pi/me_destroy_2.png")
        i3 = pygame.image.load("./p/pi/me_destroy_3.png")
        i4 = pygame.image.load("./p/pi/me_destroy_4.png")
        back.blit(i1, (me1.rect.x,me1.rect.y))
        back.blit(i2, (me1.rect.x,me1.rect.y))
        back.blit(i3, (me1.rect.x,me1.rect.y))
        back.blit(i4, (me1.rect.x,me1.rect.y))
        pygame.display.update()
        clock.tick(60)
        game_over_cartoon()

    crash_bullet_supply = pygame.sprite.groupcollide(bullet_supply_group,me_group,True,False)
    if len(crash_bullet_supply) > 0:
        pygame.time.set_timer(CREATE_BULLET1,2000)

    crash_me_bomb = pygame.sprite.groupcollide(bomb_supply_group,me_group,True,False)
    if len(crash_me_bomb) > 0:
        bomb_num += 1
        pass

    crash_enemy_bomb = pygame.sprite.groupcollide(bomb_group,enemy_group,False,True)
    if len(crash_enemy_bomb) > 0:
        SCORE += 1

# 退出键


def escape():
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_ESCAPE]:
        pygame.quit()
        exit()


# 游戏声明文字
def start_wards1():
    next_rect = next_surface.get_rect()
    next_rect.x = 240
    next_rect.y = 350

    while True:
        back.fill(WHITE)

        back.blit(next_surface,(240,350))
        back.blit(text2_surface, (0, 0))
        back.blit(text3_surface, (0, 30))
        back.blit(text4_surface, (0, BACK_HEIGHT - 30))
        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if next_rect.collidepoint(mousex, mousey):
                    return
        pygame.display.update()
        clock.tick(1)


def start_wards2():

    next_rect = next_surface.get_rect()
    next_rect.x = 240
    next_rect.y = 350

    while True:
        back.fill(WHITE)

        back.blit(next_surface, (240, 350))
        back.blit(text5_surface, (0, 0))
        back.blit(text6_surface, (0, 40))
        back.blit(text7_surface, (0, 80))
        back.blit(text8_surface,(0,BACK_HEIGHT - 70))
        back.blit(text9_surface,(0,BACK_HEIGHT - 30))
        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if next_rect.collidepoint(mousex, mousey):
                    return
        pygame.display.update()
        clock.tick(1)


# 游戏标志展示
def start_vi():
    back.fill(WHITE)
    pygame.display.update()
    pygame.time.wait(1000)

    back.blit(start1, (0, 0))
    pygame.display.update()
    pygame.time.wait(3000)


# 游戏开始动画
def start_cartoon():
    while True:

        back.blit(start, (0, 0))
        back.blit(pause, (240 - 30, 350))
        back.blit(game_over_bottom,game_over_bottom_rect)

        pygame.display.update()
        clock.tick(60)

        for Event in pygame.event.get():
            # 退出游戏
            if Event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # 按钮按下
            if Event.type == pygame.MOUSEBUTTONUP:
                mousex1, mousey1 = Event.pos
                if pause_rect.collidepoint(mousex1, mousey1):
                    return
            # 按钮按下
            if Event.type == pygame.MOUSEBUTTONUP:
                mousex2, mousey2 = Event.pos
                if game_over_bottom_rect.collidepoint(mousex2, mousey2):
                    pygame.quit()
                    exit()


# 游戏结束画面
def game_over_cartoon():
    while True:
        bg3 = Background("./p/pi/background.png",width=BACK_WIDTH,height=BACK_HEIGHT)
        bg_other_group = pygame.sprite.Group(bg3)
        bg_other_group.update()
        bg_other_group.draw(back)

        score1_font = pygame.font.Font('freesansbold.ttf', 30)
        score1_surface = score1_font.render('score:' + str(SCORE), True, WHITE)
        back.blit(score1_surface, (bg1.rect.centerx - 90,350 - 30))

        back.blit(game_over_bottom, game_over_bottom_rect)

        pygame.display.update()
        clock.tick(60)

        for Event in pygame.event.get():
            # 退出游戏
            if Event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # 按钮按下
            if Event.type == pygame.MOUSEBUTTONUP:
                mousex2, mousey2 = Event.pos
                if game_over_bottom_rect.collidepoint(mousex2, mousey2):
                    pygame.quit()
                    exit()


# 游戏暂停画面
def stop_cartoon():
    while True:
        bg3 = Background("./p/pi/background.png",width=BACK_WIDTH,height=BACK_HEIGHT)
        bg_other_group = pygame.sprite.Group(bg3)
        bg_other_group.update()
        bg_other_group.draw(back)

        score1_font = pygame.font.Font('freesansbold.ttf', 30)
        score1_surface = score1_font.render('score:' + str(SCORE), True, WHITE)
        back.blit(score1_surface, (bg1.rect.centerx - 90,30))

        resume = pygame.image.load("./p/pi/resume_nor.png")
        resume_rect = pygame.rect.Rect(240 - 30,350,resume_nor_width,resume_nor_height)

        back.blit(resume, (240 - 30, 350))
        back.blit(game_over_bottom, game_over_bottom_rect)

        pygame.display.update()
        clock.tick(60)

        for Event in pygame.event.get():
            # 退出游戏
            if Event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # 按钮按下
            if Event.type == pygame.MOUSEBUTTONUP:
                mousex, mousey = Event.pos
                if resume_rect.collidepoint(mousex, mousey):
                    return
            # 按钮按下
            if Event.type == pygame.MOUSEBUTTONUP:
                mousex2, mousey2 = Event.pos
                if game_over_bottom_rect.collidepoint(mousex2, mousey2):
                    pygame.quit()
                    exit()


# 生成各种素材区域
bullet_group = pygame.sprite.Group()

enemy_group = pygame.sprite.Group()

me1 = Me("./p/pi/me1.png",speed=0,x=MEX,y=MEY,width=ME_WIDTH,height=ME_HEIGHT)
me_group = pygame.sprite.Group(me1)

bg1 = Background("./p/pi/background.png",width=BACK_WIDTH,height=BACK_HEIGHT)
bg2 = Background("./p/pi/background.png",x=0,y=-BACK_HEIGHT,width=BACK_WIDTH,height=BACK_HEIGHT)
bg_group = pygame.sprite.Group(bg2,bg1)

bullet_supply_group = pygame.sprite.Group()

exit_font = pygame.font.Font('freesansbold.ttf',30)
exit_surface = exit_font.render('exit',True,WHITE)
exit_rect = exit_surface.get_rect()
exit_rect.x = BACK_WIDTH - exit_rect.width
exit_rect.y = BACK_HEIGHT - exit_rect.height

enemy = Enemy("./p/pi/enemy1.png",
              speed=2,
              x=ENEMY_X, y=ENEMY_Y,
              width=57, height=43)
enemy_group.add(enemy)

game_over_bottom = pygame.image.load("./p/pi/gameover.png")
game_over_bottom_rect = pygame.rect.Rect(0,0,game_over_bottom_width,game_over_bottom_height)
game_over_bottom_rect.bottom = BACK_HEIGHT - 20
game_over_bottom_rect.centerx = bg_rect.centerx

bomb_supply_group = pygame.sprite.Group()

bomb_group = pygame.sprite.Group()

bomb = pygame.image.load("./p/pi/bomb.png")
bomb_rect = pygame.rect.Rect(0,BACK_HEIGHT - bomb_height,bomb_width,bomb_height)


def main_game():
    # 游戏循环
    while True:

        # 修改暂停按钮位置
        pause_rect.x = BACK_WIDTH - pause_rect.width
        pause_rect.y = 0

        # 炸弹数量
        global bomb_num
        bomb_font = pygame.font.Font('freesansbold.ttf', 30)
        bomb_surface = bomb_font.render('X' + str(bomb_num), True, WHITE)
        bomb_text_rect = bomb_surface.get_rect()
        bomb_text_rect.x = bomb_width + 20
        bomb_text_rect.y = BACK_HEIGHT - bomb_text_rect.height

        # 积分器
        score_font = pygame.font.Font('freesansbold.ttf', 20)
        score_surface = score_font.render('score:' + str(SCORE), True, WHITE)
        score_rect = score_surface.get_rect()

        # 随机生成敌机的水平位置
        ENEMY_X = random.randint(0, BACK_WIDTH - ENEMY_WIDTH)

        # 随机生成子弹补给位置
        BULLET_SUPPLY_X = random.randint(0, BACK_WIDTH - BULLET_SUPPLY_WIDTH)
        BULLET_SUPPLY_Y = random.randint(0, BACK_HEIGHT - BULLET_SUPPLY_HEIGHT)

        # 随机生成炸弹补给位置
        bomb_supply_x = random.randint(0, BACK_WIDTH - BULLET_SUPPLY_WIDTH)
        bomb_supply_y = random.randint(0, BACK_HEIGHT - BULLET_SUPPLY_HEIGHT)

        # 碰撞检测
        crash_check()

        # 事件检测
        escape()

        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # 按钮按下
            if event.type == pygame.MOUSEBUTTONUP:
                mousex, mousey = event.pos
                press_rect = pygame.rect.Rect(0, 0, BACK_WIDTH - pause_rect.width, BACK_HEIGHT)
                if press_rect.collidepoint(mousex, mousey):
                    if bomb_num > 0:
                        bomb_big = GameSprite("./p/pi/bomb.png", speed=-3)
                        bomb_big.rect.centerx = me1.rect.centerx - 15
                        bomb_big.rect.y = me1.rect.y
                        bomb_big.rect.width = bomb_width
                        bomb_big.rect.height = bomb_height
                        bomb_group.add(bomb_big)
                        bomb_num -= 1

            # 按钮按下
            if event.type == pygame.MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if pause_rect.collidepoint(mousex, mousey):
                    stop_cartoon()

            # 按钮按下
            if event.type == pygame.MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if exit_rect.collidepoint(mousex, mousey):
                    pygame.quit()
                    exit()

            # 定时器创建敌机
            if event.type == CREATE_ENEMY:
                enemy = Enemy("./p/pi/enemy1.png",
                              speed=2,
                              x=ENEMY_X, y=ENEMY_Y,
                              width=57, height=43)
                enemy_group.add(enemy)

            # 定时器创建子弹
            if event.type == CREATE_BULLET:
                bullet1 = Bullet("./p/pi/bullet1.png",
                                 speed=3,
                                 y=Bullet_Y,
                                 width=BULLET_WIDTH,
                                 height=BULLET_HEIGHT)
                bullet1.rect.x = me1.rect.centerx - 35
                bullet1.rect.y = me1.rect.y

                bullet_group.add(bullet1)

            # 定时器创建弹药补给
            if event.type == CREATE_BULLET_SUPPLY:
                bullet_supply = GameSprite("./p/pi/bullet_supply.png",
                                           speed=1,
                                           x=BULLET_SUPPLY_X,
                                           y=BULLET_SUPPLY_Y,
                                           width=BULLET_SUPPLY_WIDTH,
                                           height=BULLET_SUPPLY_HEIGHT)
                bullet_supply.rect.bottom -= 300
                bullet_supply_group.add(bullet_supply)

            # 定时器创建另一种弹药
            if event.type == CREATE_BULLET1:
                bullet2 = Bullet("./p/pi/bullet2.png",
                                 speed=3,
                                 y=Bullet_Y,
                                 width=BULLET_WIDTH,
                                 height=BULLET_HEIGHT)
                bullet2.rect.x = me1.rect.centerx + 30
                bullet2.rect.y = me1.rect.y
                bullet_group.add(bullet2)

            # 创建炸弹补给
            if event.type == CREATE_BOMB_SUPPLY:
                bomb_supply = GameSprite("./p/pi/bomb_supply.png")
                bomb_supply.rect.x = bomb_supply_x
                bomb_supply.rect.y = bomb_supply_y
                bomb_supply.rect.width = bomb_supply_width
                bomb_supply.rect.height = bomb_supply_height
                bomb_supply.rect.bottom -= 300
                bomb_supply_group.add(bomb_supply)

        # 刷新区域
        bg_group.update()
        bg_group.draw(back)

        enemy_group.update()
        enemy_group.draw(back)

        me_group.update()
        me_group.draw(back)

        bullet_group.update()
        bullet_group.draw(back)

        bullet_supply_group.update()
        bullet_supply_group.draw(back)

        back.blit(score_surface, score_rect)

        back.blit(exit_surface, exit_rect)

        back.blit(pause, (BACK_WIDTH - pause_rect.width, 0))

        bomb_supply_group.update()
        bomb_supply_group.draw(back)

        bomb_group.update()
        bomb_group.draw(back)

        back.blit(bomb, (0, BACK_HEIGHT - bomb_height))

        back.blit(bomb_surface, bomb_text_rect)

        # 刷新窗口
        pygame.display.update()

        # 设置帧率
        clock.tick(60)


# 总程序
def main():
    while True:

        # 声明文字
        start_wards1()
        start_wards2()

        # 展示标志
        start_vi()

        # 开始游戏动画
        start_cartoon()

        # 游戏程序
        main_game()


if __name__ == '__main__':
    main()
