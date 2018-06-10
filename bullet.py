import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):  # Создание объекта пули
    def __init__(self, ai_settings, screen, shuttle):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = shuttle.rect.centerx
        self.rect.top = shuttle.rect.top

        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):  # Пермещение пули
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

