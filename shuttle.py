import pygame


class Shuttle():
    def __init__(self, ai_settings, screen):  # Инициализация корабля
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('shuttle.bmp')  # Загрузка изображения корабля
        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx  # Каждый новый корабль появляется у нижнего крана экрана
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)  # Сохранение вещественной координаты корабля
        self.moving_right = False  # Флаги перемещения
        self.moving_left = False

    def update(self):  # обновление позиции корабля
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.shuttle_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.shuttle_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)  # отрисовка корабля в текущей позиции

