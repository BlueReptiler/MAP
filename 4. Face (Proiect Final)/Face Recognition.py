import cv2

import tkinter.filedialog                           #
from tkinter import Tk                              #
                                                    # Deschide fisierul preferat
tkinter.Tk().withdraw()                             #
cascPath = tkinter.filedialog.askopenfilename()      #

faceCascade = cv2.CascadeClassifier(cascPath)

cv2.namedWindow("Camera Preview")
cv2.namedWindow("S1")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    flipHorizontal = cv2.flip(frame,1)
    gray = cv2.cvtColor(flipHorizontal, cv2.COLOR_BGR2GRAY)