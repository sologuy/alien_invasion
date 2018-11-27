import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        self.moving_up = False
        self.moving_down = False

        self.center = float(self.rect.centery)

    def render_me(self):
        self.screen.blit(self.image, self.rect)

    def update_moving(self):
        if self.moving_up and self.rect.top > 0:
            self.center -= self.settings.ship_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ship_speed_factor
        self.rect.centery = self.center
