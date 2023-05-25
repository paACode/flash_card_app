import dictionary_handler
import gui

def set_new_word():
    gui.set_card_state_to_front()
    gui.set_language(french_english_dictionary.original_language)
    french_english_dictionary.get_new_word()
    gui.set_word(french_english_dictionary.active_word)

def show_translation():
    gui.set_card_state_to_back()
    gui.set_language(french_english_dictionary.translated_language)
    french_english_dictionary.get_translation()
    gui.set_word(french_english_dictionary.active_translation)

def show_translation_with_delay():
    gui.screen.after(3000,show_translation)

if __name__ == '__main__':
    gui = gui.FlashcardApp()
    gui.set_layout()
    french_english_dictionary = dictionary_handler.Wordbook(csv_file="data/french_words.csv")

    set_new_word()
    gui.cross_button.configure(command=set_new_word)
    gui.tick_button.configure(command=show_translation_with_delay)


    gui.screen.mainloop()
