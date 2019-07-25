from tkinter import *
from tkinter import PhotoImage
from tkinter.ttk import *
import time
from random import random
from PIL import Image, ImageTk


#Title Bar or Name of The Program
root = Tk()
root.title("Smart Irrigation System Monitor")

load = Image.open("start_icon.jpg")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.image = render
img.place(x=150, y=100)


app_dimensions = [600, 500]
center_screen_height = ((int(root.winfo_screenheight())-app_dimensions[1])/2) #Center Height Positioning
center_screen_width = ((root.winfo_screenwidth()-app_dimensions[0])/2)
print(int(center_screen_height), root.winfo_screenheight())
print(int(center_screen_width), root.winfo_screenwidth())
####
root.geometry('{0}x{1}+{2}+{3}'.format(app_dimensions[0], app_dimensions[1],int(center_screen_width), int(center_screen_height)))

root.configure(background = 'blue')


#Start up Progress Bar
progress = Progressbar(root, orient=HORIZONTAL, length=590, mode='determinate' )
progress.pack()
progress.step(0.01)
progress.place(x=5, y=450)
progress.start(500)
#progress.stop()

'''
def bar():
	time.sleep(2)
    for i in range(104):
    	progress['value'] = i
    	root.update_idletasks()
    	time.sleep(0.03)

#start = Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()
bar()
'''

root.mainloop()
