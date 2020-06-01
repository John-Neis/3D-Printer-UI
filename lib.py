from PIL import ImageTk, Image
from tkinter import Tk

top = Tk()
w = top.winfo_screenwidth()
h = top.winfo_screenheight()

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