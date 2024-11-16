# Main file, complete main game loop
import pygame
import sys

from hangman import Hangman
from word_manager import WordManager
from utils import draw_text
from constants import *


def game_loop():
    pygame.init()

    # Screen settings
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hangman")

    # FPS settings
    clock = pygame.time.Clock()

    # Creating game objects
    word_manager = WordManager("words_eng.txt")
    word = word_manager.get_random_word()
    hangman = Hangman()

    guessed_letters = []  # A list that contains all the letters that the player has already guessed
    correct_letters = set()
    attempts = 0
    max_attempts = 6
    game_over = False
    win = False

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and game_over:
                if event.key >= pygame.K_a and event.key <= pygame.Key_z:
                    letter = pygame.key.name(event.key).upper()
                    if letter not in guessed_letters:
                        guessed_letters.append(letter)
                        if letter in word:
                            correct_letters.add(letter)
                        else:
                            attempts += 1

            # Display the state of the word
            display_word = ""
            for letter in word:
                if letter in correct_letters:
                    display_word += letter + " "
                else:
                    display_word += "_ "

            draw_text(display_word, FONT, WHITE, screen, WIDTH // 2 , HEIGHT // 2)

            # Displaying a list of guessed letters
            guessed_letters = "Guessed letters: " + ", ".join(guessed_letters)
            draw_text = (guessed_letters, FONT, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 50)

            # Checking the game end conditions
            if attempts >= max_attempts:
                game_over = True
                win = False
            elif all(letter in correct_letters for letter in word):
                game_over = True
                win = True

            if game_over:
                if win:
                    message = "Congratulations! You won!"
                else:
                    message = f"You lost! The word was: {word}"
                draw_text(message, LARGE_FONT, YELLOW, screen, WIDTH // 2, HEIGHT // 2 - 100)
                draw_text("Press R for retry or Q for quit", FONT, WHITE, screen, WIDTH // 2, HEIGHT // 2 - 50)

                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    # Reset the game
                    word = word_manager.get_random_word()
                    hangman.reset()
                    guessed_letters = []
                    correct_letters = set()
                    attempts  = 0
                    game_over = False
                    win = False
                elif keys[pygame.K_q]:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    game_loop()







