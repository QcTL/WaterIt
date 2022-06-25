import tkinter as tk
import tkinter.messagebox
import customtkinter
import buttonSeasons
from PIL import Image, ImageTk
import os
import infoPlant

PATH = os.path.dirname(os.path.realpath(__file__))

class PlantWidget(customtkinter.CTkFrame):
    


    def dosomething(self):
        print("TODO")

    def __init__(self, parent,plant, default=""):
        customtkinter.CTkFrame.__init__(self, parent, height=180,corner_radius=5)
        self.plant = plant
        #Plant Get Seasons active:
        self.activeSeasons = self.plant.getSeasonActive()
        print(self.activeSeasons)

        self.labelPlant = customtkinter.CTkEntry(master=self,placeholder_text=self.plant.getName(),text_font=("Roboto",-20), width = 300, placeholder_text_color="#dce4ee")
        self.labelPlant.grid(row = 0, column = 0, padx=30, pady= 25)
        

        self.labelSeasons = customtkinter.CTkFrame(self, width = 200, corner_radius=20)
        self.labelSeasons.grid_columnconfigure([0,1,2,3],minsize=50)
        self.labelSeasons.grid(row=1, column =0,pady=10)

        #DATE:
        self.labelDate= customtkinter.CTkLabel(self, text=self.plant.getDate(),text_font=("Roboto",-16),corner_radius = 10,fg_color="grey")
        self.labelDate.grid(row=0, column =1,pady=20)
        # Seasons ActivePlant

        self.unSelectedColor ="#303036"

        self.buttonWinter = buttonSeasons.SeasonWidget(self.labelSeasons,"resources/seasons/Winter.png","#a7c6da",self.activeSeasons[0])
        self.buttonWinter.grid(row=0, column = 0)  

        self.buttonSpring = buttonSeasons.SeasonWidget(self.labelSeasons,"resources/seasons/Spring.png","#2d936c",self.activeSeasons[1])
        self.buttonSpring.grid(row=0, column = 1)  

        self.buttonSummer = buttonSeasons.SeasonWidget(self.labelSeasons,"resources/seasons/Summer.png","#bfae48",self.activeSeasons[2])
        self.buttonSummer.grid(row=0, column = 2)  

        self.buttonAutumn = buttonSeasons.SeasonWidget(self.labelSeasons,"resources/seasons/Autumn.png","#c84c09",self.activeSeasons[3])
        self.buttonAutumn.grid(row=0, column = 3)  

        
        #Time BTW WATER:

        self.labelTimeWater = customtkinter.CTkFrame(self, width = 200, corner_radius=20)
        self.labelTimeWater.grid(row=1, column =1,pady=10)

        self.waterPlant = customtkinter.CTkEntry(master=self.labelTimeWater,placeholder_text=self.plant.getTimeWater(), text_font=("Roboto",-16), width = 75, placeholder_text_color="#dce4ee")
        self.waterPlant.grid(row=0,column=1)

            #Icon Water:
        self.water_image = ImageTk.PhotoImage(Image.open(PATH + "/../resources/water/drop.png").resize((40, 40)))
        self.waterLabel = tk.Label(self.labelTimeWater, image=self.water_image)
        self.waterLabel.grid(row=0,column=0) 

    def get(self):
        return self.entry.get()