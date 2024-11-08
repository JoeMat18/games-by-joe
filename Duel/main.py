# Основной файл, который запускает игру и содержит игровой цикл

import pygame
import sys
import random

from player import Player

pygame.init()

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Размер окна
WIDTH = 800
HEIGHT = 600

WINDOW_SIZE = (WIDTH, HEIGHT)

# Настройки экрана
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Duel")

# Настройка часов для контроля FPS
clock = pygame.time.Clock()
FPS = 60

# Шрифты
font = pygame.font.SysFont("arial", 30)
large_font = pygame.font.SysFont("comicsansms", 50)

def game_loop():
    # Выбор уровня сложности
    difficulty = select_difficulty()

    player_name = input("Enter your name: ")
    # Создание игроков
    player1 = Player(player_name, (200, HEIGHT // 2 - 25))
    player2 = RobotPlayer("Enemy", (500, HEIGHT // 2 - 25), difficulty)
