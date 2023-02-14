import tkinter as tk
import os
from random import randrange

ws = open('words.md').readlines()
w = None

def speak_next_word(e=None):

    global w

    w = ws[randrange(0,len(ws))]
    os.system(f"say {w}")

    text.set("")

def is_right():

    w1 = word.get().strip()
    w2 = text.get().strip()

    return w1.lower() == w2.lower()

def show_word(event):
    word.set(w)

    if is_right():
        label.configure(highlightbackground="green")
    else: 
        label.configure(highlightbackground="red")

root = tk.Tk()

text = tk.StringVar()
word = tk.StringVar()

root.geometry("350x120+0+0")
root.geometry("350x120+{}+0".format(root.winfo_screenwidth() - 350))

entry = tk.Entry(root, textvariable=text, font=("Arial", 25))
entry.pack()
entry.focus()

entry.bind("<Return>", show_word)

entry.bind("<Command-d>", lambda e: os.system(f"open dict://{w}"))
entry.bind("<Command-s>", speak_next_word)

label = tk.Entry(root, textvariable=word, font=("Arial", 25))
label.pack()

root.mainloop()

