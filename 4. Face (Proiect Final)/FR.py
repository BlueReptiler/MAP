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

ancuta = cv2.imread(r"C:\Users\stefa\Desktop\MAP\Face3.png", cv2.IMREAD_UNCHANGED)
masca_clovn = cv2.imread(r"C:\Users\stefa\Desktop\MAP\clown.png", cv2.IMREAD_UNCHANGED)
masca_anon = cv2.imread(r"C:\Users\stefa\Desktop\MAP\anon.png", cv2.IMREAD_UNCHANGED)
dog = cv2.imread(r"C:\Users\stefa\Desktop\MAP\dog1.png", cv2.IMREAD_UNCHANGED)
moustache = cv2.imread(r"C:\Users\stefa\Desktop\MAP\Moustache.png", cv2.IMREAD_UNCHANGED)
halo = cv2.imread(r"C:\Users\stefa\Desktop\MAP\Halo.png", cv2.IMREAD_UNCHANGED)


masca = ancuta
alpha = 1
refy = 0
refx = 0

if cap.isOpened(): # Incercam sa incarcam primul frame
    rval, frame = cap.read()
else:
    rval = False

while rval:

    flipHorizontal = cv2.flip(frame,1) # Intoarcem imaginea afisata de camera web pentru
                                       # a nu afisa imaginea in oglinda

    # Detectam fetele din live feed
    faces = faceCascade.detectMultiScale(flipHorizontal,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))


    for (x, y, w, h) in faces: # Salvam dimensiunile fetelor detectate ca puncte si latime respectiv inaltime.

        if(keyboard.is_pressed("1")): #
            masca = masca_clovn       # Cand apasam butonul dintre paranteze, comutam intre masti si schimbam
            alpha = 1                 # alpha-ul pentru fiecare masca in parte
            refy = 0
            refx = 0
        if(keyboard.is_pressed("2")):
            masca = masca_anon
            alpha = 0.7
            refy = 0
            refx = 0
        if(keyboard.is_pressed("3")):
            masca = dog
            alpha = 0.9
            refy = 0
            refx = 0
        if(keyboard.is_pressed("4")):
            masca = moustache
            alpha = 1
            refy = 0
            refx = 0
        if(keyboard.is_pressed("5")):
            masca = halo
            alpha = 0.7
            refy = -int((x/(h*2))*h)
            refx = 0

        # if len(faces) == 2 and zet == 0:
        #     zet = 1                                    - Face swap try -
        #     masca = flipHorizontal[y:y+h,x:x+w]

        if(len(faces) > 0): # Daca se detecteaza minim o fata#
            
            # FORMULA MAGICA : [y:y+h,x:x+w]
            
            # Redimensionam imaginea mastii ca sa fie egala cu dimensiunea fetei
            res = cv2.resize(masca, (h,w))
            try:
                flipHorizontal = cvzone.overlayPNG(flipHorizontal,res,[x+refx,y+refy])
            except:
                next

            cv2.imshow("Camera Preview", flipHorizontal) # Afisam


    cv2.imshow("Camera Preview", flipHorizontal)
    rval, frame = cap.read()
    key = cv2.waitKey(20)
    if key == 27: # La apasarea butonului ESC , se va opri rularea programului
        break

cap.release()
cv2.destroyWindow("Camera Preview")
