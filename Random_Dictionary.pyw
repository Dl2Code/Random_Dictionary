from tkinter import *
from random import randint, choice

window = Tk()
window.title("Random Dictionary")
window.attributes('-fullscreen', True)

width, height = window.winfo_screenwidth(), window.winfo_screenheight()
canvas = Canvas(window, background="#000000", highlightthickness=0)
canvas.pack(fill=BOTH, expand=True)

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
        font=("Helvetica", randint(12, 42))
    ))

    canvas.after(10, canvas.update())
    for i in range(len(text)-25):   # Change this number to set the max list length
        canvas.delete(text[i])
        del(text[i])
