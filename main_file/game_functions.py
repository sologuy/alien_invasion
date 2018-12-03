import sys
from time import sleep

import pygame
from bullet import Bullet
from alien import Alien


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
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, bullets, screen, ship)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, bullets, screen, ship):
    if len(bullets) < ai_settings.bullet_allowed:
        # 创建一颗子弹,并将其加入到编组中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_key_up_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(screen, setting, ship, aliens, bullets):
    # 每次循环时都重绘屏幕
    screen.fill(setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # test.blit_test()
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullet(ai_settings, screen, ship, bullets, aliens):
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))
    check_bullet_alien_collision(ai_settings, screen, ship, bullets, aliens)


def check_bullet_alien_collision(ai_settings, screen, ship, bullets, aliens):
    # 检查子弹事都击中了外星人
    # 如果是击中了,就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # 删除现有的子弹,并新建外星人
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    numbers_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien_width)
    for number_row in range(number_rows):
        for alien_number in range(numbers_aliens_x):
            create_alien(ai_settings, screen, alien_width, aliens, alien_number, number_row)


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    numbers_aliens_x = int(available_space_x / (2 * alien_width))
    return numbers_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    # 计算可以容纳多少行外星人
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, alien_width, aliens, alien_number, number_row):
    # 创建第一行外星人
    new_alien = Alien(ai_settings, screen)
    new_alien.x = alien_width + 2 * alien_width * alien_number
    new_alien.rect.x = new_alien.x
    new_alien.rect.y = new_alien.rect.height + 2 * new_alien.rect.height * number_row
    aliens.add(new_alien)


def check_fleet_edges(ai_setting, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setting, aliens)
            break


def change_fleet_direction(ai_setting, aliens):
    """将整群外星人下移 并改变他们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1


def update_aliens(ai_settings,screen,stats,ship, aliens,bullets):
    """更新所有外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    #检测外星人和飞船的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,screen,ship,stats,aliens,bullets)
    check_aliens_bottom(ai_settings,stats,screen,ship,bullets,aliens)

def ship_hit(ai_settings,screen,ship,stats,aliens,bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left>0:
        #将ships_left -1
        stats.ships_left -= 1

        #清空外星人列表 和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新的外星人
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

        #暂停
        sleep(0.5)
    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings,stats,screen,ship,bullets,aliens):
    """检查是否有外星人碰到底部"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #像飞船被撞倒一样处理
            ship_hit(ai_settings,screen,ship,stats,aliens,bullets)
            break
