import tkinter
import tkinter.messagebox
import customtkinter
import VertScrollFrame
import itemPlant
from datetime import date
from infoPlant import Plant
import readerJson

class MenuRWidget(customtkinter.CTkFrame):
    """
    A class to express the right site menu

    ...

    Attributes
    ----------
    parent : CtkFrame
        The parent where its placed
    numPlant : int
        Number of plants
    llPlants : list[Plant]
        Number of total Plants
    llWidPlants : list[itemPlant]
        Number of plants showing
    actualView:
        If there is a filter for the plants currently showing
    Methods
    -------
        Getters of all the Methods
            deletePlant(self,namePlant):
                Deletes the plant with the name namePlant
            createNewPlant(self):
                Create new Plant with PlaceHolder values
            addPlantToMenu(self):
                Add the plant form the list plants to the list and save it like a widget in the list of widgets Plants
            addWidgetPlantToMenu(self,widgPlant):
                Add the widget to the scrollable menu
            clearList(self):
                Deletes all the widgets of the list and from the screen
            showAllPlants(self):
                Adds all the plants to the list of widgets and the screen
            showWaterPlants(self):
                Add only to the list and to the screen the plants that need watering
            saveTheEditedPlants(self):
                Save the edited widgets to Json so the changes can be saved with json
            swapView(self):
                Change if the program shows only the plants that need watering or all plants

    """

    parent = ""
    numPlant = 0
    llPlants = []
    llWidPlants = []
    actualView = "NoFilter"

    def deletePlant(self,namePlant):
        i = 0
        found = False
        while i < self.numPlant and not found:
            found = self.llPlants[i].getName() == namePlant
            if(not found):
                i = i+1
        print("Deleted: " + str(i)+ " :" + self.llPlants[i].getName())
        self.llPlants.pop(i)
        self.llWidPlants.pop(i)

    def createNewPlant(self):
        today = date.today()
        d = today.strftime("%d/%m/%Y")
        self.llPlants.append(Plant("PlaceHolder", d, [False,False,False,False], 0,d))

    def addPlantToMenu(self): 
        self.wigPlant = itemPlant.PlantWidget(self.frame_r_scroll.interior,self,self.llPlants[self.numPlant])
        self.wigPlant.grid(row=self.numPlant,column=0,sticky="nswe", padx = 10, pady = 10)
        print("El correcte hi ha un a posicio" + str(self.numPlant) )
        self.llWidPlants.append(self.wigPlant)
        self.numPlant = self.numPlant + 1

    def addWidgetPlantToMenu(self,widgPlant):
        wigNewPlant = itemPlant.PlantWidget(self.frame_r_scroll.interior,self,widgPlant.getPlant())
        wigNewPlant.grid(row=self.numPlant,column=0,sticky="nswe", padx = 10, pady = 10)
        self.numPlant = self.numPlant + 1

    def clearList(self):
        nActu = self.numPlant
        self.numPlant = 0
        for i in range(0,nActu):
            self.frame_r_scroll.interior.grid_slaves(i,0)[0].destroy()

    def showAllPlants(self):
        self.clearList()
        for i in range(0,len(self.llPlants)):
            self.addPlantToMenu()

    def showWaterPlants(self):
        self.clearList()
        for i in range(0,len(self.llPlants)):
            print(self.llWidPlants[i].getNeedsWater())
            if(self.llWidPlants[i].getNeedsWater()):
                self.addWidgetPlantToMenu(self.llWidPlants[i])

    def saveTheEditedPlants(self):
        for i in range(0,len(self.llPlants)):
            self.llPlants[i] = Plant(self.llWidPlants[i].getName(),self.llPlants[i].getDate(),self.llWidPlants[i].getSeasonsActive(),self.llWidPlants[i].getWaterTime(), self.llWidPlants[i].getLastWaterTime())
        saveToJson = readerJson.ReadorJSON('/src/plantsFile.json')
        saveToJson.savePlantsToJson(self.llPlants)
        print("Plantes canviades")
        print(self.llPlants[i].getName())

    def swapView(self):
        if self.actualView == "NoFilter":
            self.actualView = "Filter"
            self.showWaterPlants()
        else:
            self.actualView = "NoFilter"
            self.showAllPlants()

    def __init__(self, parent, listPlants):
        customtkinter.CTkFrame.__init__(self, parent, height=200,corner_radius=20)
        self.parent = parent
        self.numPlant = 0
        self.llPlants = listPlants

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

        self.frame_r_scroll = VertScrollFrame.VerticalScrolledFrame(self)
        self.frame_r_scroll.grid(row=0,column=0,sticky="nswe")

        self.showAllPlants()