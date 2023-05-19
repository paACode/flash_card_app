import pandas
import random

class Wordbook:
    def __init__(self, csv_file):
        self.original_language = None
        self.translated_language = None
        self.active_word = None
        self.words = []
        self.translations = []
        self.csv_file_as_dataframe = pandas.read_csv(filepath_or_buffer=csv_file)
        self.initialize()

    def initialize(self):
        self.original_language = self.csv_file_as_dataframe.columns[0]
        self.translated_language = self.csv_file_as_dataframe.columns[1]
        self.words = list(self.csv_file_as_dataframe[f"{self.original_language}"])
        self.translations = list(self.csv_file_as_dataframe[f"{self.translated_language}"])
        self.get_new_word()

    def get_new_word(self):
        self.active_word = random.choice(self.words)



