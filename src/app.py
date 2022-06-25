import tkinter
import tkinter.messagebox
import customtkinter
import itemPlant

from menuLeft import AddMenuContextLeft 

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    WIDTH = 1600
    HEIGHT = 900

    def dosomething(self):
        print("WAKA")

    def expandWhenHover(self,button):
        button.bind("<Enter>", func=lambda e: button.config(
        width=self.widthButtons*2))
  
        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(
        width=self.widthButtons))
    #TODO> Bind <Configure> to know the new size of the screen


    def __init__(self):
        super().__init__()

        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        #self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        
        # 2 Segments _____________

        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)

        
        AddMenuContextLeft(self)

       
        self.frame_right= customtkinter.CTkFrame(self, width = 200, corner_radius=20)
        self.frame_right.grid(row= 0,column=1,sticky="nswe", padx=10, pady=10)
        self.frame_right.grid_columnconfigure(0,weight=1)

        self.itemPlant = itemPlant.PlantWidget(self.frame_right,"Planta","2021/09/21",10)
        self.itemPlant.grid(row=0,column=0,sticky="nswe", padx=10, pady=10)


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


