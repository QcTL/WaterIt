import tkinter
import tkinter.messagebox
import customtkinter
import menuLeft 
import menuRight 

class PlantsPage(customtkinter.CTkFrame):

    def createNewPlant(self):
        self.frame_right.createNewPlant()

    def addPlantToMenu(self):
        self.frame_right.addPlantToMenu()

    def saveTheEditedPlants(self):
        self.frame_right.saveTheEditedPlants()

    



    def dosomething(self):
        print("WAKA")

    def expandWhenHover(self,button):
        button.bind("<Enter>", func=lambda e: button.config(
        width=self.widthButtons*2))
  
        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(
        width=self.widthButtons))
    #TODO> Bind <Configure> to know the new size of the screen


    def __init__(self, parent, listPlants):
        customtkinter.CTkFrame.__init__(self, parent)
        
        # 2 Segments _____________
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)

        
        self.frame_left = menuLeft.MenuLWidget(self)
        self.frame_left.grid(row= 0,column=0,sticky="nswe", padx=10, pady=10)
       



        self.frame_right= menuRight.MenuRWidget(self,listPlants)
        self.frame_right.grid(row= 0,column=1,sticky="nswe", padx=10, pady=10)


        # 3 Button to change window:

        self.heightButtons = 75
        self.widthButtons = 75

        self.buttonWaterPlants = customtkinter.CTkButton(master=self,
                                 width=self.widthButtons,
                                 height=self.heightButtons,
                                 border_width=0,
                                 corner_radius=8,
                                 text="",
                                 fg_color="#006400", 
                                 hover_color="#458728")
        self.buttonWaterPlants.place(relx=(0.030), rely=0.85, anchor=tkinter.CENTER)
        self.expandWhenHover(self.buttonWaterPlants)


        self.buttonManagePlants = customtkinter.CTkButton(master=self,
                                 width=self.widthButtons,
                                 height=self.heightButtons,
                                 border_width=0,
                                 corner_radius=8,
                                 text="",
                                 fg_color="#D35B58", 
                                 hover_color="#C77C78",
                                 command = self.dosomething)
        self.buttonManagePlants.place(relx=(0.030), rely=0.95, anchor=tkinter.CENTER)
        self.expandWhenHover(self.buttonManagePlants)