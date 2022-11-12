import os
import keyboard
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filename = askopenfilename()
os.startfile(filename)

while not keyboard.is_pressed("esc"):
    pass