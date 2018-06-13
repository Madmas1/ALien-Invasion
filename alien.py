import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):  # Инициализация пришельца и задание начальных параметров
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('alien.bmp')  # Отрисовка и координаты
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)  # Точная позиция пришельца

    def blitme(self):
        self.screen.blit(self.image, self.rect)
