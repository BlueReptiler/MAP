import cv2
import numpy as np
from PIL import Image
import keyboard
import cvzone

#(Blue, Green, Red)
color_PURPLE = (255,80,180)
color_RED = (0,0,255)
color_GREEN = (0,255,0) #Creem culori pentru a fi mai usor in cod
color_BLUE = (255,0,0)

cv2.namedWindow("Camera Preview")
cap = cv2.VideoCapture(0) #camera video
faceCascade = cv2.CascadeClassifier(r"C:\Users\stefa\Desktop\MAP\haarcascade_frontalface_default.xml")

if cap.isOpened(): # Incercam sa incarcam primul frame
    rval, frame = cap.read()
else:
    rval = False

while rval:

    flipHorizontal = cv2.flip(frame,1) # Intoarcem imaginea afisata de camera web pentru
                                       # a nu afisa imaginea in oglinda

    # Detectam fetele din live feed``
    faces = faceCascade.detectMultiScale(flipHorizontal,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))

    for (x, y, w, h) in faces: # Salvam dimensiunile fetelor detectate ca puncte si latime respectiv inaltime.
        if(len(faces)>0):
            if len(faces) == 2:
                (x0,y0,w0,h0) = faces[0]
                (x1,y1,w1,h1) = faces[1]

                face0 = flipHorizontal[y0:y0+h0,x0:x0+w0]
                face1 = flipHorizontal[y1:y1+h1,x1:x1+w1]

                cv2.imshow("face0", face0)
                cv2.imshow("face1", face1)

                resize0 = cv2.resize(face0, (h1,w1))
                resize1 = cv2.resize(face1, (h0,w0))

                cv2.imshow("resize0", resize0)
                cv2.imshow("resize1", resize1)
                
                cv2.add(flipHorizontal[y1:y1+h1,x1:x1+w1],resize0)
                flipHorizontal[y1:y1+h1,x1:x1+w1] = resize0
                flipHorizontal[y0:y0+h0,x0:x0+w0] = resize1
    
    cv2.imshow("Camera Preview", flipHorizontal)
    rval, frame = cap.read()
    key = cv2.waitKey(20)
    if key == 27: # La apasarea butonului ESC , se va opri rularea programului
        break

cap.release()
cv2.destroyWindow("Camera Preview")
