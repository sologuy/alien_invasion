import pygame


class Test:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('test_images/hover.png')

        self.avatar_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.avatar_rect.centerx = self.screen_rect.centerx
        self.avatar_rect.centery = self.screen_rect.centery
        # self.avatar_rect.center = self.screen_rect.center
        # self.avatar_rect.top = self.screen_rect.top
    def blit_test(self):
        """在制定位置绘制飞船"""
        self.screen.blit(self.image, self.avatar_rect)
