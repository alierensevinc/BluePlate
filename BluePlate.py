# Ali Eren Sevinc
# BluePlate Car Plate Recognition Application

# Libraries for image processing
import numpy as np
import cv2

# Libraries for GUI
from Tkinter import Tk
import Tkinter as tk

# Library for selecting images
from tkFileDialog import askopenfilename

# Libraries for OCR operations
from PIL import Image
import pytesseract

# License plate template
plate_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_russian_plate_number.xml')

# Function for saving license plates
def savePlate():

    # Choose the file
    Tk().withdraw()
    filelocation = askopenfilename()
    filename = filelocation.split('/images/')   # Get the name of the image

    # Take image make it B&W
    img = cv2.imread(filelocation)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # .detectMultiScale(image, scaleFactor, minNeighbors)
    # scaleFactor > Parameter specifying how much the image size is reduced at each image scale.
    # minNeighbors > Parameter specifying how many neighbors each candidate rectangle should have to retain it.
    plates = plate_cascade.detectMultiScale(gray, 1.3, 5)

    # In the license plates you found
    # (x location, y location, width, height)
    for(x,y,w,h) in plates:
        cv2.rectangle(img, (x,y), (x+w,y+h),(255,0,0), 2)   # Draw a blue rectangle as big as the plate
        roi_gray = gray[y:y+h, x:x+w]                       # Region of image > License Plate
        roi_color = img[y:y+h, x:x+w]                       # Get the same region in original image
        
        crop_img = img[y:y+h, x:x+w]                            # Now our license plate is in crop_img
        crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)   # Turn our license plate to B&W
        crop_img = cv2.adaptiveThreshold(crop_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                     cv2.THRESH_BINARY,45,6)    # Apply thresholding 

    cv2.imshow('image', img)        # Show the original image
    cv2.imshow('plate', crop_img)   # Show the thresholded license plate
    cv2.imwrite('./_plates/'+filename[1], crop_img) # Save the license plate
        

    
        
# Function for OCR operations on license plates
def readPlate():

    # Choose the file
    Tk().withdraw()
    filelocation = askopenfilename()

    # Main OCR process
    text = pytesseract.image_to_string(Image.open(filelocation))
    print(text)


# GUI
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
