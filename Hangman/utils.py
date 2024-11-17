from constants import *

# Initializing the sound mixer
pygame.mixer.init()

# Loading sounds
correct_sound = pygame.mixer.Sound('assets/sounds/correct.wav')
wrong_sound = pygame.mixer.Sound('assets/sounds/wrong.wav')
victory_sound = pygame.mixer.Sound('assets/sounds/victory.wav')
defeat_sound = pygame.mixer.Sound('assets/sounds/defeat.wav')


def draw_text(text, font, color, surface, x, y):
    """
    Displays text on the screen.

    :param text: A string of text.
    :param font: A Pygame font object.
    :param color: The color of the text (RGB).
    :param surface: The surface to draw on.
    :param x: The X coordinate of the center of the text.
    :param y: The Y coordinate of the center of the text.
    """
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)


def play_correct_sound():
    correct_sound.play()


def play_wrong_sound():
    wrong_sound.play()


def play_victory_sound():
    victory_sound.play()


def play_defeat_sound():
    defeat_sound.play()


def display_score(screen, font, player, computer):
    """
    Displays the score on the screen.

    :param screen: Pygame screen object.
    :param font: Pygame font object.
    :param player: Number of wins the player has.
    :param computer: Number of wins the computer has.
    """
    score_text = f"Player: {player}     Computer: {computer}"
    draw_text(score_text, font, WHITE, screen, WIDTH // 2, 30)
