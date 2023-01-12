# Import the library OpenCV
import cv2
import cv2
import numpy as np

masca = cv2.imread(r"C:\Users\stefa\Desktop\MAP\lalala.png", cv2.IMREAD_UNCHANGED)

# Save the transparency channel alpha
*_, alpha = cv2.split(masca)

gray_layer = cv2.cvtColor(masca, cv2.COLOR_BGR2GRAY)

# ... Your image processing

# Duplicate the grayscale image to mimic the BGR image and finally add the transparency
dst = cv2.merge((gray_layer, gray_layer, gray_layer, alpha))
cv2.imshow("result.png", dst)



while 1:
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

