import dictionary_handler
import gui

def set_new_word():
    french_english_dictionary.get_new_word()
    gui.set_word(french_english_dictionary.active_word)

if __name__ == '__main__':
    gui = gui.FlashcardApp()
    gui.set_layout()
    gui.set_word("blabla")
    french_english_dictionary = dictionary_handler.Wordbook(csv_file="data/french_words.csv")

    gui.cross_button.configure(command=set_new_word)
    gui.tick_button.configure(command=set_new_word)

    gui.screen.mainloop()
