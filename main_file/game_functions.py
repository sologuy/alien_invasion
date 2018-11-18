import sys
import pygame


def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(screen, setting, ship):
    # 每次循环时都重绘屏幕
    screen.fill(setting.bg_color)
    ship.blitme()
    # test.blit_test()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
