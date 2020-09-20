import pygame
"""
卡片信息管理：1、增加 2、删除 3、更改
pygame与dos结合
"""

"""
参数定义区
"""
bg_height = 600
bg_width = 600
WHITE = (255,255,255)
BLACK = (0,0,0)

clock = pygame.time.Clock()
FPS = 60

"""
函数定义区
"""


def create(name,sex,connect):
    """
    创建卡片（字典）
    """
    card_name = {"姓名":name,"性别":sex,"联系方式":connect}
    return card_name


def start(text):
    # 字体
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render(text, True, BLACK)
    text_rect = text.get_rect()
    text_rect.center = (300, 300)
    display_surf.blit(text, text_rect)


"""
pygame运行区
"""
display_surf = pygame.display.set_mode((bg_height,bg_width))
pygame.display.set_caption("check")
display_surf.fill(WHITE)
while True:

    text1 = create("stupid","man",133)

    # start()

    # 关闭程序按键按下检测
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(FPS)
