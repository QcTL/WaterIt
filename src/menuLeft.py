import tkinter
import tkinter.messagebox
import customtkinter


class MenuLWidget(customtkinter.CTkFrame):
	"""
    A class to save and extract the values of a json file and torn it into Plants

    ...

    Attributes
    ----------
    parent : CTkFrame
    	The Frame where this Widget is placed inside
    
    Methods
    -------
		addPlantList(self):
			Create a new plant to the list of plants and adds it into the screen
		applyChangesPlantList(self):
			save the widgets into a json file
	"""
	parent = ""

	def addPlantList(self):
		self.parent.createNewPlant()
		self.parent.addPlantToMenu()

	def applyChangesPlantList(self):
		self.parent.saveTheEditedPlants()


	def __init__(self, parent):
		customtkinter.CTkFrame.__init__(self, parent, height=200,corner_radius=20)
		self.parent = parent

		# Items in Menu
		textModList = customtkinter.CTkLabel(master=self, text="Plant Collection", text_font=("Roboto Medium",-25))
		textModList.grid(row=0,column=0, padx= 5, pady = 10)

		#Buttons:
		buttonAddPlant = customtkinter.CTkButton(master=self, text="Add Plant", command= self.addPlantList,text_font=("Roboto",-20))
		buttonAddPlant.grid(row=1,column=0, padx= 5, pady = 10)

		buttonApplyChangesPlant = customtkinter.CTkButton(master=self, text="Apply Changes", command= self.applyChangesPlantList,text_font=("Roboto",-20))
		buttonApplyChangesPlant.grid(row=3,column=0, padx= 5, pady = 10)