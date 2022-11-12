import cv2
import numpy as np
import keyboard

cv2.namedWindow("Camera Preview")
cv2.namedWindow("S1")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    flipHorizontal = cv2.flip(frame,1)
    frame2 = cv2.flip(frame,1)
    flipHorizontal = cv2.cvtColor(flipHorizontal, cv2.COLOR_BGR2GRAY)
    flipHorizontal = cv2.bilateralFilter(flipHorizontal,15,15,15)
    #cv2.imshow("", flipHorizontal)
    flipHorizontal = cv2.Canny(flipHorizontal,7000,1,50,7,100)

    contours,h = cv2.findContours(flipHorizontal,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, .03 * cv2.arcLength(cnt, True), True)
        if(len(approx)>8 and len(approx)<20):
            cv2.imshow("S1",cv2.drawContours(frame2, [cnt], 0, (0, 255, 0), -1))
            cv2.drawMarker(frame2, (100,50), (255,0,0))

    cv2.imshow("Camera Preview", flipHorizontal)
    cv2.rectangle(flipHorizontal,(384,0),(510,128),(0,255,0),3)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

vc.release()
cv2.destroyWindow("Camera Preview")
