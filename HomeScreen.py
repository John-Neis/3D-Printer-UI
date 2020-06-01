from tkinter import *
from lib import create_tileset

class HomeScreen:
    def __init__(self, master):
        self.top = master
        self.tiles = create_tileset(self.top)

        self.win_width = self.top.winfo_screenwidth()
        self.win_height = self.top.winfo_screenheight()
        size = str(self.win_width) + 'x' + str(self.win_height)
        self.top.geometry(size)

        self.top.attributes('-type', 'dock')

        self.buttons = []
        self.buttons.append(Button(self.top, image=self.tiles["Folder"]["Light"]))
        self.buttons[0].place(x=0 * self.win_width/3, y=0 * self.win_height/2)
        self.buttons[0].bind("<Enter>", self.folder_on_enter)
        self.buttons[0].bind("<Leave>", self.folder_on_leave)
        self.buttons[0].configure(command=self.folder_on_press)

        self.buttons.append(Button(self.top, image=self.tiles["Start"]["Light"]))
        self.buttons[1].place(x=1 * self.win_width/3, y=0 * self.win_height/2)
        self.buttons[1].bind("<Enter>", self.start_on_enter)
        self.buttons[1].bind("<Leave>", self.start_on_leave)
        self.buttons[1].configure(command=self.start_on_press)

        # This will be a button is not clickable
        self.buttons.append(Button(self.top, image=self.tiles["CFile"]))
        self.buttons[2].place(x=2 * self.win_width/3, y=0 * self.win_height/2)

        self.buttons.append(Button(self.top, image=self.tiles["Cancel"]["Light"]))
        self.buttons[3].place(x=0 * self.win_width/3, y=1 * self.win_height/2)
        self.buttons[3].bind("<Enter>", self.cancel_on_enter)
        self.buttons[3].bind("<Leave>", self.cancel_on_leave)
        self.buttons[3].configure(command=self.cancel_on_press)

        self.buttons.append(Button(self.top, image=self.tiles["Pause"]["Light"]))
        self.buttons[4].place(x=1 * self.win_width/3, y=1 * self.win_height/2)
        self.buttons[4].bind("<Enter>", self.pause_on_enter)
        self.buttons[4].bind("<Leave>", self.pause_on_leave)
        self.buttons[4].configure(command=self.pause_on_press)

        # This will be a button is not clickable
        self.buttons.append(Button(self.top, image=self.tiles["CJob"]))
        self.buttons[5].place(x=2 * self.win_width/3, y=1 * self.win_height/2)

        self.top.bind('<Escape>', self.close_window)
        self.top.focus_force()

    def Run(self):
        self.top.mainloop()
        
    def close_window(self, event):
        sys.exit()

    def folder_on_enter(self, event):
        self.buttons[0].configure(image=self.tiles["Folder"]["Dark"])

    def folder_on_leave(self, event):
        self.buttons[0].configure(image=self.tiles["Folder"]["Light"])

    def start_on_enter(self, event):
        self.buttons[1].configure(image=self.tiles["Start"]["Dark"])

    def start_on_leave(self, event):
        self.buttons[1].configure(image=self.tiles["Start"]["Light"])

    def cancel_on_enter(self, event):
        self.buttons[3].configure(image=self.tiles["Cancel"]["Dark"])

    def cancel_on_leave(self, event):
        self.buttons[3].configure(image=self.tiles["Cancel"]["Light"])

    def pause_on_enter(self, event):
        self.buttons[4].configure(image=self.tiles["Pause"]["Dark"])

    def pause_on_leave(self, event):
        self.buttons[4].configure(image=self.tiles["Pause"]["Light"])

    def folder_on_press(self):
        print("You pressed the folder")

    def start_on_press(self):
        print("You pressed the start")

    def cancel_on_press(self):
        print("You pressed the cancel")

    def pause_on_press(self):
        print("You pressed the pause")
