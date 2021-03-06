import pygame
from shuttle import Shuttle
from settings import Settings
from pygame.sprite import Group
import game_func as gf


def run_game():  # Запуск и создание объекта экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    shuttle = Shuttle(ai_settings, screen)  # Cоздание корабля
    bullets = Group()                       # Создание группы для хранения пуль
    aliens = Group()                        # Создание группы для хранения пришельцев

    gf.create_fleet(ai_settings, screen, aliens)  # Создание флота

    # Запуск основго цикла игры
    while True:
        gf.check_events(ai_settings, screen, shuttle, bullets)  # Отслеживание событий
        shuttle.update()
        gf.update_bullets(bullets)
        #  print(len(bullets))
        gf.update_screen(ai_settings, screen, shuttle, aliens, bullets)

