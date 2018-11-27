import pygame
from settings import Settings

def run_game():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode(setting.screen_width,setting.screen_height)
    pygame.display.set_caption('外星人大战')

