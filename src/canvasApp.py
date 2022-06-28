import tkinter
import customtkinter

class CanvasPage(customtkinter.CTkFrame):

    waitingForSecond = False
    firstPointLine = []

    def pressedLeft(self, x:int, y:int):
        print("plip2")
        if not self.waitingForSecond:
            self.waitingForSecond = True
            self.firstPointLine = [x,y]
        else:
            self.canvas.create_line(self.firstPointLine[0],self.firstPointLine[1],x,y, fill="black", width=5)
            self.waitingForSecond = False
            self.firstPointLine = [x,y]



    def __init__(self, parent, listPlants):
        customtkinter.CTkFrame.__init__(self, parent)
        self.waitingForSecond = False
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)

        self.canvas = tkinter.Canvas(parent)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.heightButtons = 75
        self.widthButtons = 75

        self.buttonLine = customtkinter.CTkButton(master=self.canvas,
                                 width=self.widthButtons,
                                 height=self.heightButtons,
                                 border_width=0,
                                 corner_radius=8,
                                 text="",
                                 fg_color="#006400", 
                                 hover_color="#458728")
        self.buttonLine.place(relx=(0), rely=0.2, anchor=tkinter.N)

        self.buttonPlacePlants = customtkinter.CTkButton(master=self.canvas,
                                 width=self.widthButtons,
                                 height=self.heightButtons,
                                 border_width=0,
                                 corner_radius=8,
                                 text="",
                                 fg_color="#D35B58", 
                                 hover_color="#C77C78")
        self.buttonPlacePlants.place(relx=(0), rely=0.35, anchor=tkinter.N)
    