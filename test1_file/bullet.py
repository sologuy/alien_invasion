import pygame
from pygame.sprite import Sprite



class Bullet(Sprite):

    def __init__(self,ai_settings,screen,ship):
        super.__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.top = ship.rect.centery
        self.rect.centerx = ship.rect.right

        self.x = float(self.rect.x)


