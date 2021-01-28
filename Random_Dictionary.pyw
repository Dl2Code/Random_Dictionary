from tkinter import *
from random import randint, choice

window = Tk()
window.title("Random Dictionary")
window.resizable(False, False)

width, height = 660, 400
canvas = Canvas(width=width, height=height, background="#000000", highlightthickness=0)
canvas.pack()

try:

    word_list, text = [], []
    with open('Dictionary.txt', 'r') as dictionary:
        for line in dictionary:
            word_list.append(line.strip())

    while True:

        val = lambda: randint(0, 255)
        text.append(canvas.create_text(
            randint(0, width),
            randint(0, height),
            text=choice(word_list),
            fill='#%02X%02X%02X' % (val(), val(), val()),
            font=("Helvetica", randint(8, 21))
        ))

        canvas.after(85, canvas.update())        
        for i in range(len(text)-15):
            canvas.delete(text[i])


except TclError:

    window.quit()
