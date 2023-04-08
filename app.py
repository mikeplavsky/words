import tkinter as tk
import os
from random import randrange

from sys import argv
fn = argv[1]

ws = open(fn).readlines()
w = "Press Command+S"

count = 0
right = 0

def speak():

    global w
    os.system(f"say {w}")

def speak_next_word(e=None):

    global w

    w = ws[randrange(0,len(ws))]
    speak()

    text.set("")
    word.set("")

def is_right():

    w1 = word.get().strip()
    w2 = text.get().strip()

    return w1.lower() == w2.lower()

def show_word(event):

    global count, right 
    
    word.set(w.capitalize())

    if is_right():

        right += 1
        total_v.set(right)

        label.configure(highlightbackground="green")

        try:
            ws.remove(w)
        except ValueError as e: 
            print(e)

    else: 

        label.configure(highlightbackground="red")

        count += 1
        cnt_v.set(str(count))

    percent.config(text=f"{right/(count + right) * 100:.0f}%")


root = tk.Tk()

text = tk.StringVar()
word = tk.StringVar()
cnt_v = tk.StringVar()
total_v = tk.StringVar()

width= 1200
height = 120

root.geometry(f"{width}x{height}+0+0")
root.geometry("{}x{}+{}+0".format(width, height, root.winfo_screenwidth() - width))

entry = tk.Entry(root, textvariable=text, font=("Arial", 25))
entry.pack(fill='x')
entry.focus()

entry.bind("<Return>", show_word)

entry.bind("<Command-d>", lambda e: os.system(f"open dict://'{w}'"))
entry.bind("<Command-s>", speak_next_word)

label = tk.Entry(root, textvariable=word, font=("Arial", 25))
label.pack(fill='x')

percent = tk.Label(root, text="0%", fg="green", font=("Arial", 25))
percent.pack(side="right")

total = tk.Label(root, textvariable=total_v, fg="green", font=("Arial", 25))
total.pack(side="right")

cnt = tk.Label(root, textvariable=cnt_v, fg="red", font=("Arial", 25))
cnt.pack(side="right")

total_v.set(right)
cnt_v.set(count)

root.mainloop()

