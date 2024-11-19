import sys

from hangman import Hangman
from word_manager import WordManager
from utils import draw_text, play_correct_sound, play_wrong_sound, play_defeat_sound, play_victory_sound, display_score
from constants import *


def game_loop():
    pygame.init()

    # Screen settings
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hangman")

    # FPS
    clock = pygame.time.Clock()

    # Create game objects
    word_manager = WordManager("words.txt")
    word = word_manager.get_random_word()
    hangman = Hangman()

    guessed_letters = []
    correct_letters = set()
    attempts = 0
    max_attempts = 6
    game_over = False
    win = False
    score_update = False

    # Victory count
    player_score = 0
    computer_score = 0

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and not game_over:
                if pygame.K_a <= event.key <= pygame.K_z:
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

        # Displaying the state of a word
        display_word = ""
        for letter in word:
            if letter in correct_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        draw_text(display_word, FONT, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 180)

        # Displaying a list of guessed letters
        correct_guesses = [letter for letter in guessed_letters if letter in word]
        wrong_guesses = [letter for letter in guessed_letters if letter not in word]

        correct_text = "Correct letters: " + ", ".join(correct_guesses)
        wrong_text = "Wrong letters: " + ", ".join(wrong_guesses)

        draw_text(correct_text, FONT, GREEN, screen, WIDTH // 2, HEIGHT // 2 + 220)
        draw_text(wrong_text, FONT, RED, screen, WIDTH // 2, HEIGHT // 2 + 250)

        # Display score
        display_score(screen, FONT, player_score, computer_score)

        # Drawing of the gallows
        hangman.draw(screen)

        # Checking the game end conditions
        if attempts >= max_attempts:
            game_over = True
            win = False
        elif all(letter in correct_letters for letter in word):
            game_over = True
            win = True

        if game_over and not score_update:
            if win:
                player_score += 1
            else:
                computer_score += 1
            score_update = True

        if game_over:
            if win:
                message = "You won! Congratulations!"
                play_victory_sound()
            else:
                message = f"You lost! The words was: {word}"
                play_defeat_sound()

            draw_text(message, LARGE_FONT, YELLOW, screen, WIDTH // 2, HEIGHT // 2 - 150)
            draw_text("Press R to replay or Q to quit ", FONT, BLUE, screen, WIDTH // 2, HEIGHT - 170)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                # Game reset
                word = word_manager.get_random_word()
                hangman.reset()
                guessed_letters = []
                correct_letters = set()
                attempts = 0
                game_over = False
                win = False
                score_update = False
            elif keys[pygame.K_q]:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    game_loop()
