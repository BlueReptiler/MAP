import cv2
import imutils
import numpy as np
import pytesseract

import tkinter.filedialog                           #
from tkinter import Tk                              #
                                                    # Deschide browserul preferat
tkinter.Tk().withdraw()                             #
filename = tkinter.filedialog.askopenfilename()     #

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #Deschidem tesseract
img = cv2.imread(filename) #Poza pe care o alegem
img = cv2.resize(img, (800, 600)) #Micsoram chenarul cu poza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Aplicam un filtru monocrom pe imagine
cv2.imshow("img1", gray) #Afisam imaginea

gray = cv2.bilateralFilter(gray,25,25,25) #Aplicam un filtru mat
cv2.imshow("img1", gray) #Afisam imaginea

edged = cv2.Canny(gray,30,200) #Evidentiem conturul
cv2.imshow("img1", edged) #Afisam imaginea

contur=cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) #Detectare contur
contur = imutils.grab_contours(contur)
contur = sorted(contur,key=cv2.contourArea,reverse=True)[:10]
screenCnt = None
for c in contur:
    peri = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.018*peri,True)
    if(len(approx)==4):
        screenCnt = approx
        break
if screenCnt is None:
    detected = 0
    print("nu am gasit niciun contur")
else:
    detected = 1

mask = np.zeros(gray.shape,np.uint8) #Creem o masca
new_image = cv2.drawContours(mask,[screenCnt],0,255,-1)
cv2.imshow("img1",new_image) #Afisam noua imagine
new_image = cv2.bitwise_and(img,img,mask=mask) #Aplicam masca asupra imaginii initiale
cv2.imshow("img1",new_image)
(x,y)=np.where(mask==255) 
#(topx,topy) = (np.max(x),np.min(y))
#(bottomx,bottomy) = (np.min(x),np.max(y))
# Crop = gray[topx:bottomx+1,topy:bottomx+1]

new_image = cv2.bitwise_and(gray,gray,mask=mask)
cv2.imshow("img1",new_image)

print(pytesseract.image_to_string(new_image))

cv2.waitKey(0)
cv2.destroyAllWindows()