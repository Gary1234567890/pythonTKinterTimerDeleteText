from tkinter import *
import tkinter
import time

tk = tkinter.Tk()
count = 0

def update_clock():
    global count
    chars = text_1.get(0.0, "end")
    num = len(chars)
    if num <= count:
        text_1.delete(1.0, END)
    count = num
    tk.after(5000, update_clock)


tk.geometry("600x600")
tk.title("Disappearing Text - 5sec background timer deletes text if nothing changes")
text_1 = tkinter.Text(tk, width=400, height=100, wrap="word")
text_1.pack(side=BOTTOM)

update_clock()

tk.mainloop()
