try:  # Python 2
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter.constants import *
except ImportError:  # Python 2
    import Tkinter as tk
    import ttk
    from tkinter.constants import *
import customtkinter

# Based on
#   https://web.archive.org/web/20170514022131id_/http://tkinter.unpythonic.net/wiki/VerticalScrolledFrame
# Changed to work with customtkinter

class VerticalScrolledFrame(ttk.Frame):

    def __init__(self, parent, *args, **kw):

        s = ttk.Style()
        s.configure('My.TFrame', background='#2a2d2e')

        ttk.Frame.__init__(self, parent, *args, **kw, style='My.TFrame')
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)

        # Create a canvas object and a vertical scrollbar for scrolling it.
        vscrollbar = customtkinter.CTkScrollbar(self, orientation="vertical")
        vscrollbar.grid(row=0,column=1, sticky="nswe")
        

        canvas = tk.Canvas(self, bd=0, bg= "#2a2d2e", highlightthickness=0,
                           yscrollcommand=vscrollbar.set)
        canvas.grid(row=0,column=0, sticky="nswe")
        vscrollbar.config(command=canvas.yview)

        # Reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # Create a frame inside the canvas which will be scrolled with it.
        self.interior = interior = customtkinter.CTkFrame(canvas,corner_radius=20)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)
        self.interior.grid_rowconfigure(0,weight=1)
        self.interior.grid_columnconfigure(0,weight=1)


        # Track changes to the canvas and frame width and sync them,
        # also updating the scrollbar.
        def _configure_interior(event):
            # Update the scrollbars to match the size of the inner frame.
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the canvas's width to fit the inner frame.
                canvas.config(width=interior.winfo_reqwidth())
        
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the inner frame's width to fill the canvas.
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        
        canvas.bind('<Configure>', _configure_canvas)
