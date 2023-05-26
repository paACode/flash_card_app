import pandas
import random

class Wordbook:
    def __init__(self):
        self.original_language = None
        self.translated_language = None
        self.active_word = None
        self.active_translation = None
        self.words = []
        self.translations = []
        self.csv_file_as_dataframe = None
        self.load_csv_file()
        self.initialize()

    def initialize(self):
        self.original_language = self.csv_file_as_dataframe.columns[0]
        self.translated_language = self.csv_file_as_dataframe.columns[1]
        self.words = list(self.csv_file_as_dataframe[f"{self.original_language}"])
        self.translations = list(self.csv_file_as_dataframe[f"{self.translated_language}"])
        self.get_new_word()

    def get_new_word(self):
        self.active_word = random.choice(self.words)

    def get_translation(self):
        index = self.words.index(self.active_word)
        self.active_translation = self.translations[index]

    def remove_translation_word_from_list(self):
        self.words.remove(self.active_word)
        self.translations.remove(self.active_translation)

    def update_data(self):
        data = {f"{self.original_language}": self.words, f"{self.translated_language}": self.translations}
        self.csv_file_as_dataframe = pandas.DataFrame(data)

    def save_data_to_csv(self):
        self.csv_file_as_dataframe.to_csv("data/french_words_to_learn.csv", index=False)


    def load_csv_file(self):
        try:
            self.csv_file_as_dataframe = pandas.read_csv(filepath_or_buffer="data/french_words_to_learn.csv")
        except FileNotFoundError:
            self.csv_file_as_dataframe = pandas.read_csv(filepath_or_buffer="data/french_words.csv")




