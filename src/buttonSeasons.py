import tkinter as tk
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os


PATH = os.path.dirname(os.path.realpath(__file__))

class SeasonWidget(customtkinter.CTkButton): 


    active = False
    colorActive = ""
    
    def flipState(self):
        if(self.active):
            self.config(fg_color="#303036")
        else:
            self.config(fg_color= self.colorActive)
        
        self.active = not self.active

    def __init__(self, parent,srcImage,colorActive,active,default=""):
        self.image = ImageTk.PhotoImage(Image.open(PATH + "/../" + srcImage).resize((40, 40)))
        self.active = active
        self.colorActive = colorActive
        customtkinter.CTkButton.__init__(self, master=parent,
                                 width=50,
                                 height=50,
                                 border_width=0,
                                 corner_radius=8,
                                 text="",
                                 fg_color=colorActive, 
                                 command = self.flipState,
                                 image= self.image)
        if(not self.active):
            self.config(fg_color="#303036")