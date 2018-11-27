import sys
import pygame
from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event=event, ship=ship)


def check_key_down_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,bullets,screen,ship)


def fire_bullet(ai_settings,bullets,screen,ship):
    if len(bullets) < ai_settings.bullet_allowed:
        # 创建一颗子弹,并将其加入到编组中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_key_up_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(screen, setting, ship, bullets):
    # 每次循环时都重绘屏幕
    screen.fill(setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # test.blit_test()
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullet(bullets):
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))
