import pygame

class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position  # (x, y)
        self.key_combo = ()  # Текущая комбинация клавиш
        self.index_combo = 0  # Индекс текущей клавиши в комбинации
        self.reaction_time = None # Время реакции

    def assign_key_combo(self, keys):
        """
        Назначает комбинацию клавиш для игрока.

        :param keys: Кортеж из двух клавиш (например, ('A', 'F')).
        """
        self.key_combo = keys
        self.index_combo = 0
        self.reaction_time = None

    def reset(self):
        """
        Назначает комбинацию клавиш для игрока.

        :param keys: Кортеж из двух клавиш (например, ('A', 'F')).
        """
        self.index_combo = 0
        self.reaction_time = None

    def hande_key_press(self, key):
        """
        Обрабатывает нажатие клавиши игроком.

        :param key: Нажатая клавиша (строка).
        :return: True, если комбинация завершена, иначе False.
        """
        if self.index_combo < len(self.key_combo) and key == self.key_combo[self.index_combo]:
            self.index_combo += 1
            if self.index_combo == len(self.key_combo):
                self.reaction_time = pygame.time.get_ticks()
                return True
            else:
                self.reset()
                return False

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.position, 100, 50)
        name_text = pygame.font.SysFont('arial', 30).render(self.name, True, (255, 255, 255))
        screen.blit(name_text, self.position[0] + 10, self.position[1] + 10)

