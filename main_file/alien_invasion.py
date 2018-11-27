import pygame
import game_functions as gf
from main_file.settings import Settings
from ship import Ship
from my_test import Test
from pygame.sprite import Group


def run_game():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode([setting.screen_width, setting.screen_height])
    pygame.display.set_caption('Alien Invasion')
    # 创建一艘飞船
    ship = Ship(setting, screen)
    test = Test(screen)

    #创建一个用于存储子弹的编组
    bullets = Group()
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(setting,screen,ship,bullets)
        ship.update_moving()
        gf.update_bullet(bullets)
        gf.update_screen(screen, setting, ship, bullets)


run_game()
