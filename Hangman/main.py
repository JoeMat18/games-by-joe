# main.py

import pygame
import sys

from hangman import Hangman
from word_manager import WordManager
from utils import draw_text, play_correct_sound, play_wrong_sound, play_victory_sound, play_defeat_sound, display_score
from constants import *


def game_loop():
    # Инициализация Pygame
    pygame.init()

    # Настройка экрана
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("")

    # Настройка часов для контроля FPS
    clock = pygame.time.Clock()

    # Создание объектов игры
    word_manager = WordManager("words_rus.txt")
    word = word_manager.get_random_word()
    hangman = Hangman()

    guessed_letters = []
    correct_letters = set()
    attempts = 0
    max_attempts = 6
    game_over = False
    win = False

    # Счётчики побед
    player_score = 0
    computer_score = 0

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and not game_over:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    letter = pygame.key.name(event.key).upper()
                    if letter not in guessed_letters:
                        guessed_letters.append(letter)
                        if letter in word:
                            correct_letters.add(letter)
                            play_correct_sound()
                        else:
                            attempts += 1
                            hangman.draw_next_part(screen)
                            play_wrong_sound()

        # Отображение состояния слова
        display_word = ""
        for letter in word:
            if letter in correct_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        draw_text(display_word, FONT, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 180)

        # Отображение списка угаданных букв
        correct_guesses = [letter for letter in guessed_letters if letter in word]
        wrong_guesses = [letter for letter in guessed_letters if letter not in word]

        correct_text = "Правильные буквы: " + ", ".join(correct_guesses)
        wrong_text = "Неправильные буквы: " + ", ".join(wrong_guesses)

        draw_text(correct_text, FONT, GREEN, screen, WIDTH // 2, HEIGHT // 2 + 230)
        draw_text(wrong_text, FONT, RED, screen, WIDTH // 2, HEIGHT // 2 + 260)

        # Отображение счёта
        display_score(screen, FONT, player_score, computer_score)

        # Отрисовка виселицы
        hangman.draw(screen)

        # Проверка условий завершения игры
        if attempts >= max_attempts:
            game_over = True
            win = False
        elif all(letter in correct_letters for letter in word):
            game_over = True
            win = True

        if game_over:
            if win:
                player_score += 1
                play_victory_sound()
                message = "Поздравляем! Вы выиграли!"
            else:
                computer_score += 1
                play_defeat_sound()
                message = f"Вы проиграли! Слово было: {word}"
            draw_text(message, LARGE_FONT, YELLOW, screen, WIDTH // 2, HEIGHT // 2 - 200)
            draw_text("Нажмите R для повторной игры или Q для выхода", FONT, WHITE, screen, WIDTH // 2,
                      HEIGHT // 2 - 150)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                # Сброс игры
                word = word_manager.get_random_word()
                hangman.reset()
                guessed_letters = []
                correct_letters = set()
                attempts = 0
                game_over = False
                win = False
            elif keys[pygame.K_q]:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    game_loop()
