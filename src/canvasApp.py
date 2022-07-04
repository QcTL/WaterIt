import tkinter
import customtkinter

class CanvasPage(customtkinter.CTkFrame):
    """
    A class that represents The Canvas

    ### NOT USED IN THE MOMENT
    """
    waitingForSecond = False
    firstPointLine = []

    placeElement=  ""

    def create_line(self,x:int, y:int):
        print("plip2")
        if not self.waitingForSecond:
            self.waitingForSecond = True
            self.firstPointLine = [x,y]
        else:
            self.canvas.create_line(self.firstPointLine[0],self.firstPointLine[1],x,y, fill="black", width=5)
            self.waitingForSecond = False
            self.firstPointLine = [x,y]


    def pressedLeft(self, x:int, y:int):
        if self.placeElement == "line":
            self.create_line(x,y)
        elif self.placeElement == "placePlant":
            create_plant()

    def activateDesactivatePlaceElement(self, new_element):
        if self.placeElement == "":
            self.placeElement = new_element
        elif self.placeElement == new_element:
            self.placeElement = ""
        print(self.placeElement)

    def turnOnLine(self):
        self.activateDesactivatePlaceElement("line")  

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
                                 hover_color="#458728",
                                 command= self.turnOnLine)
        self.buttonLine.place(relx=(0), rely=0.2, anchor=tkinter.N)

        self.buttonPlacePlants = customtkinter.CTkButton(master=self.canvas,
                                 width=self.widthButtons,
                                 height=self.heightButtons,
                                 border_width=0,
                                 corner_radius=8,
                                 text="",
                                 fg_color="#D35B58", 
                                 hover_color="#C77C78",
                                  command= lambda e: print(self.placeElement))
        self.buttonPlacePlants.place(relx=(0), rely=0.35, anchor=tkinter.N)
    