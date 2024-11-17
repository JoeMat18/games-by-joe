from constants import *

class Hangman:
    def __init__(self):
        """
        Initializes the Hangman object
        """
        self.current_part = 0

        # Загрузка изображений для каждой части виселицы
        self.images = [
            pygame.image.load(r"C:\Users\97252\Desktop\Games\Hangman\assets\images\hangman1.png"),
            pygame.image.load(r"C:\Users\97252\Desktop\Games\Hangman\assets\images\hangman2.png"),
            pygame.image.load(r"C:\Users\97252\Desktop\Games\Hangman\assets\images\hangman3.png"),
            pygame.image.load(r"C:\Users\97252\Desktop\Games\Hangman\assets\images\hangman4.png"),
            pygame.image.load(r"C:\Users\97252\Desktop\Games\Hangman\assets\images\hangman5.png"),
            pygame.image.load(r"C:\Users\97252\Desktop\Games\Hangman\assets\images\hangman6.png"),
        ]

        # Загрузка фонового изображения
        self.background = pygame.image.load(r"C:\Users\97252\Desktop\Games\Hangman\assets\images\background.jpeg")

    def reset(self):
        """
        Reset the Hangman
        """
        self.current_part = 0

    def draw_background(self, screen):
        """
        Displays the background on the screen.

        :param screen: Pygame screen object.
        """
        screen.blit(self.background, (0, 0))

    def draw_next_part(self, screen):
        """
        Draws the next part of the gallows.

        :param screen: Pygame screen object.
        """
        if self.current_part < len(self.images):
            screen.blit(self.images[self.current_part], (WIDTH // 2 - 150, HEIGHT // 2 - 100))
            self.current_part += 1

    def draw(self, screen):
        """
        Рисует все текущие части виселицы.

        :param screen: Объект экрана Pygame.
        """
        # Рисуем фон

        # Рисуем все части, которые должны быть видны
        for i in range(self.current_part):
            screen.blit(self.images[i], (WIDTH // 2 - 150, HEIGHT // 2 - 100))
