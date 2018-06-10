import sys
import pygame
from bullet import Bullet


# Перемещение корабля

def check_keydown_events(event, ai_settings, screen, shuttle, bullets):  # В функции отслеживается зажатие клавиши
    if event.key == pygame.K_RIGHT:  # Вправо
        shuttle.moving_right = True
    elif event.key == pygame.K_LEFT:    # Влево
        shuttle.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, shuttle, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, shuttle):
    if event.key == pygame.K_RIGHT:
        shuttle.moving_right = False
    if event.key == pygame.K_LEFT:
        shuttle.moving_left = False


def check_events(ai_settings, screen, shuttle, bullets):  # проверка событий (нажатие клавиш и отслеживание мыши)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, shuttle, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, shuttle)


def update_screen(ai_setting, screen, shuttle, bullets):  # функция обновления изображения
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    shuttle.blitme()
    pygame.display.flip()   # Отоброжение последнего прорисованного экран


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullets(ai_settings, screen, shuttle, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, shuttle)
        bullets.add(new_bullet)
