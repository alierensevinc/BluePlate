# Ali Eren Sevinc
# BluePlate Car Plate Recognition Application

import numpy as np
import cv2
from Tkinter import Tk
import Tkinter as tk
from tkFileDialog import askopenfilename

from PIL import Image
import pytesseract
import os
import argparse

plate_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_russian_plate_number.xml')

def savePlate():
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
        
        break
    
        

def readPlate():
    
    Tk().withdraw()
    filelocation = askopenfilename()

    text = pytesseract.image_to_string(Image.open(filelocation))
    print(text)



root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

btnSave = tk.Button(frame, 
                   text="Save License Plate", 
                   command=savePlate,
                   padx=10,
                   pady=10)
btnSave.pack(side=tk.LEFT)
btnRead = tk.Button(frame,
                   text="Read License Plate",
                   command=readPlate,
                   padx=10,
                   pady=10)
btnRead.pack(side=tk.LEFT)
btnQuit = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit,
                   padx=10,
                   pady=10)
btnQuit.pack(side=tk.LEFT)

root.mainloop()
