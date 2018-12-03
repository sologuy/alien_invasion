import pygame
import game_functions as gf
from main_file.settings import Settings
from ship import Ship
from alien import Alien
from my_test import Test
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode([setting.screen_width, setting.screen_height])
    pygame.display.set_caption('Alien Invasion')
    # 创建一艘飞船
    ship = Ship(setting, screen)
    aliens = Group()
    gf.create_fleet(setting, screen, ship, aliens)
    #创建统计游戏信息的实例
    stats = GameStats(setting)

    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(setting, screen, ship, bullets)
        if stats.game_active:
            ship.update_moving()
            gf.update_aliens(ai_settings=setting,screen=screen,stats =stats,ship=ship, aliens=aliens,bullets= bullets)
            gf.update_bullet(setting, screen, ship, bullets, aliens)
        gf.update_screen(screen, setting, ship, aliens, bullets)


run_game()
