from tkinter import *
import GUI_load
import GUI_Display

# This script is created by Jones Jernfors

# This script needs the next scripts in order to work
# GUI_Display
# GUI_load
# x-ray
# Spectrum


root = Tk()
root.geometry("1920x1080")
root.title("X ray Machine")

GUI_Display.display(root)


root.mainloop()
