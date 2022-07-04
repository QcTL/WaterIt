import tkinter as tk
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os


PATH = os.path.dirname(os.path.realpath(__file__))

class SeasonWidget(customtkinter.CTkButton): 
    """
    class to Represent in Widget of the Season Button

    ...

    Attributes
    ----------
    active : bool
        Plant you want to be represented
    colorActive: str
        Color that will have the button when its active

    Methods
    -------
        get(self):
            Returns if the widget is active(pressed) or not
        _flipState(self):
            Change the state of the button, if its active, it turns it off, and vice versa
    """

    active : bool = False
    colorActive :str = ""
    
    def __flipState(self):
        """Change the state of the buttons representing seasons, if its pressed when active turns inactive and vice versa

        Returns:
        Flips the state
        """
        if(self.active):
            self.config(fg_color="#303036")
        else:
            self.config(fg_color= self.colorActive)
        
        self.active = not self.active

    def __init__(self, parent,srcImage,colorActive,active):
        """
        Parameters
        ----------
        parent : widget
            The widget that will contain this widget
        srcImage : str
            The path **from the project folder** to the image
        colorActive : str
            color of the button when active
        active: bool
            The initial state of active
        """
        
        self.image = ImageTk.PhotoImage(Image.open(PATH + "/../" + srcImage).resize((50, 50)))
        self.active = active
        self.colorActive = colorActive
        customtkinter.CTkButton.__init__(self, master=parent,
                                 width=50,
                                 height=50,
                                 border_width=0,
                                 corner_radius=8,
                                 text="",
                                 fg_color=colorActive, 
                                 command = self.__flipState,
                                 image= self.image)
        if(not self.active):
            self.config(fg_color="#303036")

    def get(self):
        """Return the active value of the button

        Parameters:
            none

        Returns:
        plant: self.active
       """
        return self.active