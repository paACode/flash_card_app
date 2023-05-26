import tkinter
import os

main_pwd = os.path.dirname(__file__)
image_folder = os.path.join(main_pwd, "images")
tick_path = os.path.join(image_folder, "right.png")
cross_path = os.path.join(image_folder, "wrong.png")
card_front_path = os.path.join(image_folder, "card_front.png")
card_back_path = os.path.join(image_folder, "card_back.png")

BACKGROUND_COLOR = "#B1DDC6"
BACKGROUND_COLOR_CARD_BACK = "#91c2af"
BACKGROUND_COLOR_CARD_FRONT = "#FFFFFF"


def get_image(path):
    print(path)
    return tkinter.PhotoImage(file=path)


class FlashcardApp:
    def __init__(self):
        # Basic Elements
        self.screen = tkinter.Tk()
        self.screen.title("Flashcard App")
        self.canvas = tkinter.Canvas(background=BACKGROUND_COLOR)
        # Images
        self.tick_img = tkinter.PhotoImage(file=tick_path)
        self.cross_img = tkinter.PhotoImage(file=cross_path)
        self.card_front_img = tkinter.PhotoImage(file=card_front_path)
        self.card_back_img = tkinter.PhotoImage(file=card_back_path)
        self.delay_timers = {}

        # Buttons and Labels
        self.tick_button = tkinter.Button(image=self.tick_img, highlightthickness=0)
        self.cross_button = tkinter.Button(image=self.cross_img, highlightthickness=0)
        self.language_label = tkinter.Label(master=self.canvas, font=("Arial", "40", "italic"),
                                            text="Placeholder", background=BACKGROUND_COLOR_CARD_FRONT)
        self.word_label = tkinter.Label(master=self.canvas, font=("Arial", "60", "bold"),
                                        text="Placeholder", background=BACKGROUND_COLOR_CARD_FRONT)
        self.card_state = "Front"
        self.update_card_image()

    def set_layout(self):
        self.screen.config(padx=50, pady=50, background=BACKGROUND_COLOR)
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.cross_button.grid(row=1, column=0)
        self.tick_button.grid(row=1, column=1)
        self.language_label.place(x=400, y=150, anchor=tkinter.CENTER)
        self.word_label.place(x=400, y=253, anchor=tkinter.CENTER)

    def update_card_image(self):
        if self.card_state == "Front":
            img = self.card_front_img
        elif self.card_state == "Back":
            img = self.card_back_img
        self.canvas.configure(width=img.width(), height=img.height(), highlightthickness=0)
        self.canvas.create_image(img.width() / 2, img.height() / 2, image=img)

    def set_word(self, word):
        self.word_label.configure(text=word)

    def set_language(self, language):
        self.language_label.configure(text=language)

    def set_card_state_to_front(self):
        self.card_state = "Front"
        self.update_card_image()
        self.set_label_color(color_background=BACKGROUND_COLOR_CARD_FRONT, color_font="black")

    def set_label_color(self, color_background, color_font):
        self.language_label.configure(background=color_background, foreground=color_font)
        self.word_label.configure(background=color_background,foreground=color_font)


    def set_card_state_to_back(self):
        self.card_state = "Back"
        self.update_card_image()
        self.set_label_color(color_background=BACKGROUND_COLOR_CARD_BACK, color_font="White")

    def create_delay_timer_for_function(self, delay_ms, function):
        if f"{function.__name__}" not in self.delay_timers:
            self.delay_timers[f"{function.__name__}"] = self.screen.after(delay_ms, function)
        elif f"{function.__name__}" in self.delay_timers:
            self.destroy_delay_timer_for_function(function)
            self.create_delay_timer_for_function(delay_ms,function)

    def destroy_delay_timer_for_function(self, function):
        if f"{function.__name__}" in self.delay_timers:
            self.screen.after_cancel(self.delay_timers[f"{function.__name__}"])
            del self.delay_timers[f"{function.__name__}"]
