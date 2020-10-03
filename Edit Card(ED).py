import pygame
"""
卡片信息管理：1、增加 2、删除 3、更改
pygame与dos结合
"""

"""
参数定义区
"""
# 背景参数
bg_height = 900
bg_width = 900
WHITE = (255,255,255)
BLACK = (0,0,0)
# 时钟参数
clock = pygame.time.Clock()
FPS = 60

"""
函数定义区
"""


def create():
    """
    创建卡片（字典）
    """
    name = input("name:")
    sex = input("sex:")
    tel = input("tel:")
    card_name = {"姓名": name, "性别": sex, "联系方式": tel}
    return card_name


def show(text):
    """
    展示卡片
    """
    times = int(input("times:"))
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("name:"+text["姓名"]+"   sex:"+text["性别"]+"   tel:"+text["联系方式"], True, BLACK)
    text_rect = text.get_rect()
    text_rect.center = (450, 17*times)
    display_surf.fill(WHITE)
    display_surf.blit(text, text_rect)
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("back", True, BLACK)
    text_rect4 = text.get_rect()
    text_rect4.center = (450, 17 * 30)
    display_surf.blit(text, text_rect4)

    # 判断鼠标点击
    while True:
        for Event in pygame.event.get():

            if Event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = Event.pos
                if text_rect4.collidepoint(mouse_x, mouse_y):
                    return
            elif Event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(FPS)


def start():
    """
    开始界面
    """
    # 画上按钮
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("crate", True, BLACK)
    text_rect1 = text.get_rect()
    text_rect1.center = (450,17)
    display_surf.blit(text, text_rect1)

    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("edit", True, BLACK)
    text_rect2 = text.get_rect()
    text_rect2.center = (450, 17*10)
    display_surf.blit(text, text_rect2)

    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("delete", True, BLACK)
    text_rect3 = text.get_rect()
    text_rect3.center = (450, 17*20)
    display_surf.blit(text, text_rect3)

    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("quit", True, BLACK)
    text_rect4 = text.get_rect()
    text_rect4.center = (450,17*30)
    display_surf.blit(text, text_rect4)

    # 判断鼠标点击
    while True:
        for Event in pygame.event.get():
            if Event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = Event.pos
                if text_rect1.collidepoint(mouse_x, mouse_y):
                    texts = create()
                    show(texts)
                    return
            if Event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = Event.pos
                if text_rect2.collidepoint(mouse_x, mouse_y):
                    pass
            if Event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = Event.pos
                if text_rect3.collidepoint(mouse_x, mouse_y):
                    pass
            if Event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = Event.pos
                if text_rect4.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    exit()
            elif Event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(FPS)


"""
pygame运行区
"""
pygame.init()
display_surf = pygame.display.set_mode((bg_height,bg_width))
pygame.display.set_caption("edit card")
display_surf.fill(WHITE)
while True:

    start()

    display_surf.fill(WHITE)

    # 关闭程序按键按下检测
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(FPS)

