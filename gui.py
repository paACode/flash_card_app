import tkinter
import os

main_pwd = os.path.dirname(__file__)
image_folder = os.path.join(main_pwd, "images")
tick_path = os.path.join(image_folder, "right.png")
cross_path = os.path.join(image_folder, "wrong.png")
card_front_path = os.path.join(image_folder, "card_front.png")
card_back_path = os.path.join(image_folder, "card_back.png")

BACKGROUND_COLOR_CARD_BACK = "#B1DDC6"
BACKGROUND_COLOR_CARD_FRONT = "#FFFFFF"


def get_image(path):
    print(path)
    return tkinter.PhotoImage(file=path)


class FlashcardApp:
    def __init__(self):
        # Basic Elements
        self.screen = tkinter.Tk()
        self.screen.title("Flashcard App")
        self.canvas = tkinter.Canvas()
        # Images
        self.tick_img = tkinter.PhotoImage(file=tick_path)
        self.cross_img = tkinter.PhotoImage(file=cross_path)
        self.card_front_img = tkinter.PhotoImage(file=card_front_path)
        self.card_back_img = tkinter.PhotoImage(file=card_back_path)

        # Buttons and Labels
        self.tick_button = tkinter.Button(image=self.tick_img, highlightthickness=0)
        self.cross_button = tkinter.Button(image=self.cross_img, highlightthickness=0)
        self.language_label = tkinter.Label(master=self.canvas, font=("Arial", "40", "italic"),
                                            text="Placeholder", background=BACKGROUND_COLOR_CARD_FRONT)
        self.word_label = tkinter.Label(master=self.canvas, font=("Arial", "60", "bold"),
                                        text="Placeholder", background=BACKGROUND_COLOR_CARD_FRONT)

        self.set_card_state(img=self.card_front_img)

    def set_layout(self):
        self.screen.config(padx=50, pady=50, background=BACKGROUND_COLOR_CARD_BACK)
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.cross_button.grid(row=1, column=0)
        self.tick_button.grid(row=1, column=1)
        self.language_label.place(x=400, y=150, anchor=tkinter.CENTER)
        self.word_label.place(x=400, y=253, anchor=tkinter.CENTER)

    def set_card_state(self, img):
        self.canvas.configure(width=img.width(), height=img.height(), highlightthickness=0)
        self.canvas.create_image(img.width() / 2, img.height() / 2, image=img)
    def set_word(self,word):
        self.word_label.configure(text=word)

    def set_language(self, language):
        self.language_label.configure(text=language)
