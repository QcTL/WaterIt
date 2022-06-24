import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

def addPlantList():
	print("TODO :)")

def removePlantList():
	print("TODO :)")

def applyChangesPlantList():
	print("TODO :)d=")


def AddMenuContextLeft(UI):
	frame_left= customtkinter.CTkFrame(UI, width = 200, corner_radius=20)
	frame_left.grid(row= 0,column=0,sticky="nswe", padx=10, pady=10)

	# Items in Menu
	textModList = customtkinter.CTkLabel(master=frame_left, text="Plant Collection", text_font=("Roboto Medium",-25))
	textModList.grid(row=0,column=0, padx= 5, pady = 10)

	#Buttons:
	buttonAddPlant = customtkinter.CTkButton(master=frame_left, text="Add Plant", command= addPlantList,text_font=("Roboto",-20))
	buttonAddPlant.grid(row=1,column=0, padx= 5, pady = 10)

	buttonRemovePlant = customtkinter.CTkButton(master=frame_left, text="Remove Plant", command= removePlantList,text_font=("Roboto",-20))
	buttonRemovePlant.grid(row=2,column=0, padx= 5, pady = 10)

	buttonApplyChangesPlant = customtkinter.CTkButton(master=frame_left, text="Apply Changes", command= applyChangesPlantList,text_font=("Roboto",-20))
	buttonApplyChangesPlant.grid(row=3,column=0, padx= 5, pady = 10)