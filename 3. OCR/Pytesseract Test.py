import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image

import tkinter.filedialog                           #
from tkinter import Tk                              #
                                                    # Deschide browserul preferat
tkinter.Tk().withdraw()                             #
filename = tkinter.filedialog.askopenfilename()     #
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print(pytesseract.image_to_string(Image.open(filename), lang="ron"))