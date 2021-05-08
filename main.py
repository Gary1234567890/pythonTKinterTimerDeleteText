from tkinter import *
import tkinter
import time

tk = tkinter.Tk()
text_count = 0
second = 0


def update_clock():
    global text_count, second
    chars = text_1.get(0.0, "end")
    num = len(chars)
    if num > text_count:
        second = 0
        text_count = num
        tk.after(1000, update_clock)
        return
    if second == 5:
        text_1.delete(1.0, END)
        text_count = 0
        tk.after(1000, update_clock)
        return
    second += 1
    print(second)
    print(text_count)
    tk.after(1000, update_clock)


tk.geometry("600x600")
tk.title("Disappearing Text - 5sec background timer deletes text if nothing changes")
text_1 = tkinter.Text(tk, width=400, height=100, wrap="word")
text_1.pack(side=BOTTOM)

update_clock()

tk.mainloop()
