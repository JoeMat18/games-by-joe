# word_manager.py

import random

class WordManager:
    def __init__(self, filepath):
        """
        Инициализирует менеджер слов.

        :param filepath: Путь к файлу со списком слов.
        """
        self.filepath = filepath
        self.words = self.load_words()

    def load_words(self):
        """
        Загружает слова из файла.

        :return: Список слов.
        """
        with open(self.filepath, 'r', encoding='utf-8') as file:
            words = [line.strip().upper() for line in file if line.strip()]
        return words

    def get_random_word(self):
        """
        Выбирает случайное слово из списка.

        :return: Строка с выбранным словом.
        """
        return random.choice(self.words)
