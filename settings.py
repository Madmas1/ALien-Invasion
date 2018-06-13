# Класс для хранения настроек игры


class Settings():
    def __init__(self):
        self.screen_width = 1200  # Параметры экрана
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.shuttle_speed_factor = 1  # Скорость шатла

        self.bullet_speed_factor = 1  # Параметры пуль
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

