#!/usr/bin/python3

from tkinter import *
from PIL import ImageTk, Image
from lib import *

#top = Tk()
#w = top.winfo_screenwidth()
#h = top.winfo_screenheight()
size = str(w) + 'x' + str(h)
top.geometry(size)
top.attributes('-type', 'dock')

tiles = create_tileset()

buttons = []

buttons.append(Button(top, image=tiles["Folder"]["Light"]))
buttons.append(Button(top, image=tiles["Start"]["Light"]))
buttons.append(Button(top, image=tiles["CFile"]))
buttons.append(Button(top, image=tiles["Cancel"]["Light"]))
buttons.append(Button(top, image=tiles["Pause"]["Light"]))
buttons.append(Button(top, image=tiles["CJob"]))

def close_window(event):
    sys.exit()

def folder_on_enter(event):
    buttons[0].configure(image=tiles["Folder"]["Dark"])

def folder_on_leave(event):
    buttons[0].configure(image=tiles["Folder"]["Light"])

def start_on_enter(event):
    buttons[1].configure(image=tiles["Start"]["Dark"])

def start_on_leave(event):
    buttons[1].configure(image=tiles["Start"]["Light"])

def cancel_on_enter(event):
    buttons[3].configure(image=tiles["Cancel"]["Dark"])

def cancel_on_leave(event):
    buttons[3].configure(image=tiles["Cancel"]["Light"])

def pause_on_enter(event):
    buttons[4].configure(image=tiles["Pause"]["Dark"])

def pause_on_leave(event):
    buttons[4].configure(image=tiles["Pause"]["Light"])

def folder_on_press():
    print("You pressed the folder")

def start_on_press():
    print("You pressed the start")

def cancel_on_press():
    print("You pressed the cancel")

def pause_on_press():
    print("You pressed the pause")

buttons[0].place(x=0 * w/3, y=0 * h/2)
buttons[0].bind("<Enter>", folder_on_enter)
buttons[0].bind("<Leave>", folder_on_leave)
buttons[0].configure(command=folder_on_press)

buttons[1].place(x=1 * w/3, y=0 * h/2)
buttons[1].bind("<Enter>", start_on_enter)
buttons[1].bind("<Leave>", start_on_leave)
buttons[1].configure(command=start_on_press)

buttons[3].place(x=0 * w/3, y=1 * h/2)
buttons[3].bind("<Enter>", cancel_on_enter)
buttons[3].bind("<Leave>", cancel_on_leave)
buttons[3].configure(command=cancel_on_press)

buttons[4].place(x=1 * w/3, y=1 * h/2)
buttons[4].bind("<Enter>", pause_on_enter)
buttons[4].bind("<Leave>", pause_on_leave)
buttons[4].configure(command=pause_on_press)

# This will be a button is not clickable
buttons[2].place(x=2 * w/3, y=0 * h/2)

# This will be a button is not clickable
buttons[5].place(x=2 * w/3, y=1 * h/2)

top.focus_force()
top.bind("<Escape>", close_window)
top.mainloop()
