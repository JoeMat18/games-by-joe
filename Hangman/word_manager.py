import random


class WordManager:
    def __init__(self, filepath):
        """
        Initializes the word manager.

        :param filepath: Path to the file with the word list.
        """
        self.filepath = filepath
        self.words = self.load_words()

    def load_words(self):
        """
        Loads words from a file.

        :return: List of words.
        """
        with open(self.filepath, 'r', encoding='utf-8') as file:
            words = [line.strip().upper() for line in file if line.strip()]
        return words

    def get_random_word(self):
        """
        Selects a random word from the list.

        :return: String with the selected word.
        """
        return random.choice(self.words)



