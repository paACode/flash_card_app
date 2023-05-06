import tkinter
import os

main_pwd = os.path.dirname(__file__)
image_folder = os.path.join(main_pwd, "images")
tick_path = os.path.join(image_folder, "right.png")
cross_path = os.path.join(image_folder, "wrong.png")
card_front_path = os.path.join(image_folder, "card_front.png")
card_back_path = os.path.join(image_folder, "card_back.png")

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 526
BACKGROUND_COLOR = "#B1DDC6"


def get_image(path):
    print(path)
    return tkinter.PhotoImage(file=path)


class FlashcardGUI:
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
        #Buttons and Labels
        self.tick_button = tkinter.Button(image=self.tick_img, highlightthickness=0)
        self.cross_button = tkinter.Button(image=self.cross_img, highlightthickness=0)
        self.language_label = tkinter.Label()
        self.word_label = tkinter.Label()

        self.set_card_state(img= self.card_front_img)

    def set_layout(self):
        self.screen.config(padx=50, pady=50, background=BACKGROUND_COLOR)
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.cross_button.grid(row=1, column=0)
        self.tick_button.grid(row=1, column=1)

    def set_card_state(self, img):
        self.canvas.configure(width=img.width(), height=img.height())
        self.canvas.add
        self.canvas.create_image(img.width() / 2, img.height() / 2, image=img)


