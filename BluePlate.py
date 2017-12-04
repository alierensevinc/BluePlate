# Ali Eren Sevinc
# BluePlate Car Plate Recognition Application

import numpy as np
import cv2
from Tkinter import Tk
from tkFileDialog import askopenfilename

plate_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_russian_plate_number.xml')

Tk().withdraw()
filelocation = askopenfilename()
filename = filelocation.split('/images/')

while 1:
    img = cv2.imread(filelocation)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(gray, 1.3, 5)

    for(x,y,w,h) in plates:
        cv2.rectangle(img, (x,y), (x+w,y+h),(255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        crop_img = img[y:y+h, x:x+w]
        crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        crop_img = cv2.adaptiveThreshold(crop_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                 cv2.THRESH_BINARY,45,6)


    cv2.imshow('image', img)
    cv2.imshow('plate', crop_img)
    cv2.imwrite('./_plates/'+filename[1], crop_img)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


cv2.destroyAllWindows()
        
