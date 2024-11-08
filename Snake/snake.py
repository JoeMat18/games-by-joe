import pygame
import time
import random

pygame.init()

width = 800  # Ширина окна
height = 400  # Длина окна

black = (0, 0, 0)  # Фон игры
white = (255, 255, 255)  # Текст
red = (255, 40, 60)  # GAME OVER
green = (0, 255, 0)  # Змейка
blue = (43, 247, 255)  # Еда

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
snake_speed = 15  # Скорость змейки

block_size = 10

font_style = pygame.font.SysFont("arial", 35)
score_font = pygame.font.SysFont("comicsans", 30)

def my_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    game_display.blit(value, [0, 0])

def my_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], block_size, block_size])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [width / 5, height / 2])

def game_loop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []  # Список сегментов змейки
    length_of_snake = 1

    foodx = round(random.randrange(0, width - block_size) / 10) * 10
    foody = round(random.randrange(0, height - block_size) / 10) * 10

    while not game_over:

        while game_close:
            game_display.fill(black)
            message("Game Over! Press Q to exit or ESC to play again", red)
            my_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True  # Завершение игры
                        game_close = False
                    if event.key == pygame.K_ESCAPE:
                        # Сброс переменных игры
                        game_close = False
                        snake_list = []
                        length_of_snake = 1
                        x1 = width / 2
                        y1 = height / 2
                        x1_change = 0
                        y1_change = 0
                        foodx = round(random.randrange(0, width - block_size) / 10) * 10
                        foody = round(random.randrange(0, height - block_size) / 10) * 10

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True  # Завершение игры при закрытии окна
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:  # ВЛЕВО
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:  # ВПРАВО
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:  # ВВЕРХ
                    x1_change = 0
                    y1_change = -block_size
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:  # ВНИЗ
                    x1_change = 0
                    y1_change = block_size

        # Проверка выхода змейки за границы окна
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Обновляем позицию змейки
        x1 += x1_change
        y1 += y1_change

        game_display.fill(black)
        pygame.draw.rect(game_display, blue, [foodx, foody, block_size, block_size])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Проверка столкновения змейки с собой
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        my_snake(block_size, snake_list)
        my_score(length_of_snake - 1)

        pygame.display.update()

        # Проверка поедания еды

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 10) * 10
            foody = round(random.randrange(0, height - block_size) / 10) * 10
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()

