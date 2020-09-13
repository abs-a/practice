import time
import random
import pygame
"""
思路：0、开始按钮 1、黑色背景 2、50X50小方块 3、新世纪时间
"""

"""初始化"""
pygame.init()

"""定义参数"""
# 颜色
BLACK = (0,0,0)
GREEN = (0,255,0)
# 背景宽高
bg_height = 600
bg_width = 600
# 小方块宽高
sq_height = 50
sq_width = 50
# 帧率
clock = pygame.time.Clock()
FPS = 60

"""背景"""
display_surf = pygame.display.set_mode((bg_height,bg_width))
pygame.display.set_caption("check")
# 填上白色
display_surf.fill(BLACK)


def start():
    """
    开始按钮
    """
    # 按钮宽高
    st_height = 100
    st_width = 200
    # 按钮位置
    st_x = 300-100
    st_y = 300-50
    # 画上按钮
    st_rect = pygame.rect.Rect(st_x,st_y,st_width,st_height)
    pygame.draw.rect(display_surf,GREEN,(st_x,st_y,st_width,st_height))
    # 字体
    font = pygame.font.Font("freesansbold.ttf",32)
    text = font.render("start game",True,BLACK)
    text_rect = text.get_rect()
    text_rect.center = (300,300)
    display_surf.blit(text,text_rect)
    # 字体
    font1 = pygame.font.Font("freesansbold.ttf", 32)
    text1 = font1.render("click the square as soon as possible", True, BLACK,GREEN)
    text_rect1 = text1.get_rect()
    text_rect1.center = (300, 17)
    display_surf.blit(text1, text_rect1)
    # 判断鼠标点击
    while True:
        for Event in pygame.event.get():
            if Event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = Event.pos
                if st_rect.collidepoint(mouse_x, mouse_y):
                    display_surf.fill(BLACK)
                    return
            elif Event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(FPS)


def check1():
    """
    刷新小方块 算出新世纪时间
    """
    # 小方块x、y值
    x = random.randint(0, bg_width - sq_width)
    y = random.randint(0, bg_height - sq_height)
    # 画上按钮
    st_rect = pygame.rect.Rect(x,y,sq_width,sq_height)
    pygame.draw.rect(display_surf, GREEN, (x,y,sq_width,sq_height))
    start_time = time.time()
    # 判断鼠标点击
    while True:
        for Event in pygame.event.get():
            if Event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = Event.pos
                if st_rect.collidepoint(mouse_x, mouse_y):
                    end_time = time.time()
                    need_time1 = end_time - start_time
                    display_surf.fill(BLACK)
                    return need_time1
            elif Event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(FPS)


def check2():
    """
    刷新小方块 算出新世纪时间
    """
    # 小方块x、y值
    x = random.randint(0, bg_width - sq_width)
    y = random.randint(0, bg_height - sq_height)
    # 画上按钮
    st_rect = pygame.rect.Rect(x,y,sq_width,sq_height)
    pygame.draw.rect(display_surf, GREEN, (x,y,sq_width,sq_height))
    start_time = time.time()
    # 判断鼠标点击
    while True:
        for Event in pygame.event.get():
            if Event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = Event.pos
                if st_rect.collidepoint(mouse_x, mouse_y):
                    end_time = time.time()
                    need_time2 = end_time - start_time
                    display_surf.fill(BLACK)
                    return need_time2
            elif Event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(FPS)


def check3():
    """
    刷新小方块 算出新世纪时间
    """
    # 小方块x、y值
    x = random.randint(0, bg_width - sq_width)
    y = random.randint(0, bg_height - sq_height)
    # 画上按钮
    st_rect = pygame.rect.Rect(x,y,sq_width,sq_height)
    pygame.draw.rect(display_surf, GREEN, (x,y,sq_width,sq_height))
    start_time = time.time()
    # 判断鼠标点击
    while True:
        for Event in pygame.event.get():
            if Event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = Event.pos
                if st_rect.collidepoint(mouse_x, mouse_y):
                    end_time = time.time()
                    need_time3 = end_time - start_time
                    display_surf.fill(BLACK)
                    return need_time3
            elif Event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(FPS)


def avenge(need_time1,need_time2,need_time3):
    """
    取平均数
    """
    need_time = (need_time1+need_time2+need_time3)/3
    need_time = str(need_time)
    # 字体
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("you need:"+need_time+"s", True, BLACK,GREEN)
    text_rect = text.get_rect()
    text_rect.center = (300, 17)
    display_surf.blit(text, text_rect)
    # 字体
    font1 = pygame.font.Font("freesansbold.ttf", 32)
    text1 = font1.render("next", True, BLACK,GREEN)
    text_rect1 = text1.get_rect()
    text_rect1.center = (300, 300)
    display_surf.blit(text1, text_rect1)
    # 判断鼠标点击
    while True:
        for Event in pygame.event.get():
            if Event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = Event.pos
                if text_rect1.collidepoint(mouse_x, mouse_y):
                    display_surf.fill(BLACK)
                    return
            elif Event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(FPS)


def ending1():
    """
    终止按钮
    """
    # 按钮宽高
    ed_height = 100
    ed_width = 200
    # 按钮位置
    ed_x = 300 - 100
    ed_y = 300 - 50
    # 画上按钮
    ed_rect = pygame.rect.Rect(ed_x, ed_y, ed_width, ed_height)
    pygame.draw.rect(display_surf, GREEN, (ed_x, ed_y, ed_width, ed_height))
    # 字体
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("again", True, BLACK)
    text_rect = text.get_rect()
    text_rect.center = (300, 300)
    display_surf.blit(text, text_rect)
    """
    终止按钮 
    """
    # 按钮宽高
    ed1_height = 100
    ed1_width = 200
    # 按钮位置
    ed1_x = 300 - 100
    ed1_y = 300 - 200
    # 画上按钮
    ed1_rect = pygame.rect.Rect(ed1_x, ed1_y, ed1_width, ed1_height)
    pygame.draw.rect(display_surf, GREEN, (ed1_x, ed1_y,ed1_width, ed1_height))
    # 字体
    font1 = pygame.font.Font("freesansbold.ttf", 32)
    text1 = font1.render("quit", True, BLACK)
    text_rect1 = text1.get_rect()
    text_rect1.center = (ed1_rect.centerx, ed1_rect.centery)
    display_surf.blit(text1, text_rect1)
    # 判断鼠标点击
    while True:
        for Event in pygame.event.get():
            if Event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = Event.pos
                if ed1_rect.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    exit()
                elif ed_rect.collidepoint(mouse_x, mouse_y):
                    display_surf.fill(BLACK)
                    return
            elif Event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(FPS)


while True:
    """
    游戏循环
    """
    # 开始按钮
    start()
    # 小方块刷出
    need_time11 = check1()
    need_time22 = check2()
    need_time33 = check3()
    # 算出平均数
    avenge(need_time11,need_time22,need_time33)
    # 终止按钮
    ending1()
    # 关闭程序按键按下检测
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(FPS)
