import tkinter
import tkinter.messagebox
import customtkinter
import VertScrollFrame
import itemPlant
from datetime import date
from infoPlant import Plant
import readerJson

class MenuRWidget(customtkinter.CTkFrame):
    
    parent = ""
    numPlant = 0
    llPlants = []
    llWidPlants = []

    def createNewPlant(self):
        today = date.today()
        d = today.strftime("%d/%m/%Y")
        self.llPlants.append(Plant("PlaceHolder", d, [False,False,False,False], 0))

    def addPlantToMenu(self): 
        self.wigPlant = itemPlant.PlantWidget(self.frame_r_scroll.interior,self.llPlants[self.numPlant])
        self.wigPlant.grid(row=self.numPlant,column=0,sticky="nswe", padx = 10, pady = 10)
        self.llWidPlants.append(self.wigPlant)
        self.numPlant = self.numPlant + 1


    def saveTheEditedPlants(self):
        for i in range(0,len(self.llPlants)):
            self.llPlants[i] = Plant(self.llWidPlants[i].getName(),self.llPlants[i].getDate(),self.llWidPlants[i].getSeasonsActive(),self.llWidPlants[i].getWaterTime())
        saveToJson = readerJson.ReadorJSON('/src/plantsFile.json')
        saveToJson.savePlantsToJson(self.llPlants)
        print("Plantes canviades")
        print(self.llPlants[i].getName())

    def __init__(self, parent, listPlants):
        customtkinter.CTkFrame.__init__(self, parent, height=200,corner_radius=20)
        self.parent = parent
        self.numPlant = 0
        self.llPlants = listPlants

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

        self.frame_r_scroll = VertScrollFrame.VerticalScrolledFrame(self)
        self.frame_r_scroll.grid(row=0,column=0,sticky="nswe")

        for i in range(0,len(self.llPlants)):
            self.addPlantToMenu()


