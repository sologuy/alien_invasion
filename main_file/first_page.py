import pygame
import game_functions as gf
from main_file.settings import Settings
from ship import Ship
from my_test import Test

def run_game():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode([setting.screen_width,setting.screen_height])
    pygame.display.set_caption('Alien Invasion')
    #创建一艘飞船
    ship = Ship(screen)
    test = Test(screen)
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ship)
        ship.update_moving()
        gf.update_screen(screen,setting,ship)


run_game()