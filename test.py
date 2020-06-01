#!/usr/bin/python3

from tkinter import *
from PIL import ImageTk, Image

top = Tk()
w = top.winfo_screenwidth()
h = top.winfo_screenheight()
size = str(w) + 'x' + str(h)
top.geometry(size)
top.attributes('-type', 'dock')

buttons = []

def close_window(event):
    sys.exit()

def create_tileset():
    tileset = {}
    #Folder Light
    preimage = Image.open("assets/Folder_Tile.jpg")
    preimage = preimage.resize((w/3, h/2), Image.ANTIALIAS)
    img_folder = ImageTk.PhotoImage(preimage)
    tileset['Folder'] = dict(Light=img_folder)
    # Folder Dark
    preimage = Image.open("assets/Folder_Tile_Dark.jpg")
    preimage = preimage.resize((w/3, h/2), Image.ANTIALIAS)
    img_folder = ImageTk.PhotoImage(preimage)
    tileset['Folder']['Dark'] = img_folder
        
    # Start Light
    preimage = Image.open("assets/Start_Tile.jpg")
    preimage = preimage.resize((w/3, h/2), Image.ANTIALIAS)
    img_start = ImageTk.PhotoImage(preimage)
    tileset['Start'] = dict(Light=img_start)
    # Start Dark
    preimage = Image.open("assets/Start_Tile_Dark.jpg")
    preimage = preimage.resize((w/3, h/2), Image.ANTIALIAS)
    img_start = ImageTk.PhotoImage(preimage)
    tileset["Start"]["Dark"] = img_start
    
    # Current File Light
    preimage = Image.open("assets/Current_File_Tile.jpg")
    preimage = preimage.resize((w/3, h/2), Image.ANTIALIAS)
    img_currf = ImageTk.PhotoImage(preimage)
    tileset["CFile"] = dict(Light=img_currf)
    # Current File Dark
    preimage = Image.open("assets/Current_File_Tile_Dark.jpg")
    preimage = preimage.resize((w/3, h/2), Image.ANTIALIAS)
    img_currf = ImageTk.PhotoImage(preimage)
    tileset["CFile"]["Dark"] = img_currf
    
    # Cancel Light
    preimage = Image.open("assets/Cancel_Tile.jpg")
    preimage = preimage.resize((w/3, h/2), Image.ANTIALIAS)
    img_cancel = ImageTk.PhotoImage(preimage)
    tileset["Cancel"] = dict(Light=img_cancel)
    # Cancel Dark
    preimage = Image.open("assets/Cancel_Tile_Dark.jpg")
    preimage = preimage.resize((w/3, h/2), Image.ANTIALIAS)
    img_cancel = ImageTk.PhotoImage(preimage)
    tileset["Cancel"]["Dark"] = img_cancel
    
    # Pause Light
    preimage = Image.open("assets/Pause_Tile.jpg")
    preimage = preimage.resize((w/3, h/2), Image.ANTIALIAS)
    img_pause = ImageTk.PhotoImage(preimage)
    tileset["Pause"] = dict(Light=img_pause)
    # Pause Dark
    preimage = Image.open("assets/Pause_Tile_Dark.jpg")
    preimage = preimage.resize((w/3, h/2), Image.ANTIALIAS)
    img_pause = ImageTk.PhotoImage(preimage)
    tileset["Pause"]["Dark"] = img_pause
    
    # Current Job Light
    preimage = Image.open("assets/Current_Job_Tile.jpg")
    preimage = preimage.resize((w/3, h/2), Image.ANTIALIAS)
    img_currj = ImageTk.PhotoImage(preimage)
    tileset["CJob"] = dict(Light=img_currj)
    # Current Job Dark
    preimage = Image.open("assets/Current_Job_Tile_Dark.jpg")
    preimage = preimage.resize((w/3, h/2), Image.ANTIALIAS)
    img_currj = ImageTk.PhotoImage(preimage)
    tileset["CJob"]["Dark"] = img_currj

    return tileset

tiles = create_tileset()
buttons.append(Button(top, image=tiles["Folder"]["Light"]))
buttons.append(Button(top, image=tiles["Start"]["Light"]))
buttons.append(Button(top, image=tiles["CFile"]["Light"]))
buttons.append(Button(top, image=tiles["Cancel"]["Light"]))
buttons.append(Button(top, image=tiles["Pause"]["Light"]))
buttons.append(Button(top, image=tiles["CJob"]["Light"]))

def on_enter(event):
    buttons[0].configure(image=tiles["Folder"]["Dark"])

def on_leave(event):
    buttons[0].configure(image=tiles["Folder"]["Light"])

#top.attributes('-zoomed', True)





buttons[0].place(x=0 * w/3, y=0 * h/2)
buttons[0].bind("<Enter>", on_enter)
buttons[0].bind("<Leave>", on_leave)


buttons[1].place(x=1 * w/3, y=0 * h/2)

buttons[2].place(x=2 * w/3, y=0 * h/2)

buttons[3].place(x=0 * w/3, y=1 * h/2)

buttons[4].place(x=1 * w/3, y=1 * h/2)

buttons[5].place(x=2 * w/3, y=1 * h/2)

top.focus_force()
top.bind("<Escape>", close_window)
top.mainloop()
