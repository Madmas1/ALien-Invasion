import sys
import pygame
from bullet import Bullet
from alien import Alien


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


def update_screen(ai_setting, screen, shuttle, aliens, bullets):  # функция обновления изображения
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    shuttle.blitme()
    aliens.draw(screen)

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


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens):  # Создание флота
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)

    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)
