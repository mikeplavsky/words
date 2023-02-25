import tkinter as tk
import os
from random import randrange

ws = open('words.md').readlines()
w = "Press Command+S"
count = 0

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

    global count 
    
    word.set(w.capitalize())

    if is_right():

        label.configure(highlightbackground="green")
        try:
            ws.remove(w)
        except ValueError as e: 
            print(e)

    else: 

        label.configure(highlightbackground="red")
        cnt.configure(fg="red")

        count += 1
        cnt_v.set(str(count))

    total_v.set(len(ws))

root = tk.Tk()

text = tk.StringVar()
word = tk.StringVar()
cnt_v = tk.StringVar()
total_v = tk.StringVar()

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

total = tk.Label(root, textvariable=total_v, font=("Arial", 25))
total.pack(side="right")

cnt = tk.Label(root, textvariable=cnt_v, font=("Arial", 25))
cnt.pack(side="right")

total_v.set(len(ws))

root.mainloop()

