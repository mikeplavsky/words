import os      
from random import randrange
from curses import wrapper, curs_set

ws = open('words.md').readlines()

def main(scr):

    y,x = scr.getmaxyx()

    curs_set(False)
    scr.clear()

    while True:

        key = scr.getkey()

        if key == 'q':
            break

        scr.clear()

        w = ws[randrange(0,len(ws))]
        os.system(f"say {w}")

        key = scr.getkey()

        if key == 'q':
            break

        scr.addstr(y//2,(x - len(w))//2,w)

wrapper(main)



