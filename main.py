import dictionary_handler
import gui


def set_new_word():
    gui.destroy_delay_timer_for_function(function=show_translation)
    gui.set_card_state_to_front()
    gui.set_language(french_english_dictionary.original_language)
    french_english_dictionary.get_new_word()
    gui.set_word(french_english_dictionary.active_word)

def update_wordbook():
    french_english_dictionary.remove_translation_word_from_list()
    french_english_dictionary.update_data()
    french_english_dictionary.save_data_to_csv()

def show_translation():
    gui.destroy_delay_timer_for_function(function=show_translation)
    gui.set_card_state_to_back()
    gui.set_language(french_english_dictionary.translated_language)
    french_english_dictionary.get_translation()
    gui.set_word(french_english_dictionary.active_translation)
    update_wordbook()


def show_translation_delayed():
    gui.create_delay_timer_for_function(delay_ms=3000, function=show_translation)



if __name__ == '__main__':
    gui = gui.FlashcardApp()
    gui.set_layout()
    french_english_dictionary = dictionary_handler.Wordbook()

    set_new_word()

    gui.cross_button.configure(command=set_new_word)
    gui.tick_button.configure(command=show_translation_delayed)

    gui.screen.mainloop()
