import tkinter
import tkinter.messagebox
import customtkinter

class PlantWidget(tk.Frame):
	def __init__(self, parent, namePlant, datePlant, timebtwWater, default=""):
        tk.Frame.__init__(self, parent)
        #TODO: Propose a sistem where the Plant is represented, with a Name-Date.

    def get(self):
        return self.entry.get()