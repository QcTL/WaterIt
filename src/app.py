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
    readingPresses = True

    def motion(self, event):
        if(self.readingPresses):
            x, y = event.x, event.y
            print('{}, {}'.format(x, y))
            self.screenShown.pressedLeft(x,y)

    def changeFrame(self, new_frame, readingPresses):
        if screenShown is not None and screenShown is not new_frame:
            self.screenShown.destroy()
            self.screenShown = new_frame
            self.screenShown.grid(row=0,column=0,sticky="nsew")
            self.readingPresses = readingPresses

    def __init__(self, listPlants):
        super().__init__()
        
        
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        #self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)


        #self.screenShown = mantainApp.PlantsPage(self,listPlants)
        #self.screenShown.grid(row=0,column=0,sticky="nsew")

        self.screenShown = canvasApp.CanvasPage(self,listPlants)
        self.screenShown.grid(row=0,column=0,sticky="nsew")

        self.bind("<Button-1>",self.motion)
