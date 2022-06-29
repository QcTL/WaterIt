import tkinter
import tkinter.messagebox
import customtkinter
import mantainApp
import canvasApp

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    WIDTH = 1600
    HEIGHT = 900
    
    screenShown = None
    readingPresses = False

    currFrame = "plants"

    def motion(self, event):
        if(self.readingPresses):
            x, y = event.x, event.y
            print('{}, {}'.format(x, y))
            self.screenShown.pressedLeft(x,y)

    def swapFrame(self):
        self.screenShown.destroy()
        if self.currFrame == "plants":
            self.screenShown =  canvasApp.CanvasPage(self,self.listPlants)
            self.currFrame = "canvas" 
            self.readingPresses = True
            
        else:
            self.readingPresses = False
            self.screenShown = mantainApp.PlantsPage(self,self.listPlants)
            self.currFrame = "plants" 
            

        self.screenShown.grid(row=0,column=0,sticky="nsew")
        

    def __init__(self, listPlants):
        super().__init__()
        
        self.framePlants = mantainApp.PlantsPage(self,listPlants)
        self.listPlants = listPlants
        self.screenShown = self.framePlants
        self.screenShown.grid(row=0,column=0,sticky="nsew")
        self.currFrame = "plants"
        print(self.currFrame)

        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        #self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)


        self.bind("<Button-1>",self.motion)
