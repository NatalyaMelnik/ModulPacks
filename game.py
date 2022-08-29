import pygame
import sys

"""Подготовка модулей pygame к работе"""

pygame.init()

"""Создаем графическое окно"""

screen = pygame.display.set_mode((1000, 600))

"""Основной цикл программы"""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # закрытие графического окна пользователем
            pygame.quit()
            sys.exit()
