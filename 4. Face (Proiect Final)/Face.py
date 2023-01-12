import cv2
import numpy as np
from PIL import Image
import keyboard

# W - latime patrat
# H - inaltime patrat
# X

#(Blue, Green, Red)
color_PURPLE = (255,80,180)
color_RED = (0,0,255)
color_GREEN = (0,255,0)
color_BLUE = (255,0,0)

cv2.namedWindow("Camera Preview")
cap = cv2.VideoCapture(0) #camera video
faceCascade = cv2.CascadeClassifier(r"C:\Users\stefa\Desktop\MAP\haarcascade_frontalface_default.xml")
masca = cv2.imread(r"C:\Users\stefa\Desktop\MAP\Face2.PNG")


if cap.isOpened(): # try to get the first frame
    rval, frame = cap.read()
else:
    rval = False

while rval:
    flipHorizontal = cv2.flip(frame,1)
    width,height,dontknow = flipHorizontal.shape
    # flipHorizontal = cv2.cvtColor(flipHorizontal,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(flipHorizontal,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))

    for face in faces:
        fatau = cv2.bitwise_and(flipHorizontal,flipHorizontal,mask=face)
        cv2.imshow("gg",fatau)
    for (x, y, w, h) in faces:
        center_coordinates = x + w // 2, y + h // 2
        right_down = x+w,y+h
        left_down = x,y+h
        right_top = x+w,y
        left_top = x,y
        radius = w/2

        

        # rect = cv2.rectangle(flipHorizontal, (x, y), (x+w, y+h), color_PURPLE, 2)
        # res = cv2.resize(masca, (w,h),interpolation = cv2.INTER_AREA)
        # cv2.imshow("ss",res)
        # new_image = cv2.addWeighted(rect,1,masca,1,2)

        # cv2.rectangle(flipHorizontal, (x, y), (x+w, y+h), color_PURPLE, 2)
        # cv2.line(flipHorizontal, left_top, center_coordinates, color_RED, 1)


    cv2.imshow("Camera Preview", flipHorizontal)
    # cv2.rectangle(flipHorizontal,(384,0),(510,128),(0,255,0),3)
    rval, frame = cap.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cap.release()
cv2.destroyWindow("Camera Preview")
