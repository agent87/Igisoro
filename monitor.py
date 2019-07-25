from tkinter import *
from PIL import Image, ImageTk 
from tkinter import PhotoImage
from time import time
from random import random


monitor = Tk()
monitor.title("Smart Irrigation System Monitor ")


####
app_dimensions = [1000, 700]
center_screen_height = ((int(monitor.winfo_screenheight())-app_dimensions[1])/4) #Center Height Positioning
center_screen_width = ((monitor.winfo_screenwidth()-app_dimensions[0])/2)
print(int(center_screen_height), monitor.winfo_screenheight())
print(int(center_screen_width), monitor.winfo_screenwidth())
####
monitor.geometry('{0}x{1}+{2}+{3}'.format(app_dimensions[0], app_dimensions[1],int(center_screen_width), int(center_screen_height)))
monitor.resizable(0, 0)
monitor.configure(background = 'gray')
######


def donothing():
	filewin = Toplevel(monitor)
	button = Button(filewin, text="Do nothing button")
	button.pack()




menubar = Menu(monitor)
filemenu = Menu(menubar, tearoff=100)
filemenu.add_command(label="Restart", command=donothing)
filemenu.add_command(label="Import", command=donothing)
filemenu.add_command(label="Export", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=monitor.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Preferences", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

monitor.config(menu=menubar)



monitor.mainloop()