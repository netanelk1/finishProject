import tkinter as tk
from tkinter import messagebox
import numpy as np
from PIL import Image,ImageTk
import cv2
import glob
import os
from matplotlib import pyplot as plt


#GLOBAL PARAMETERS
count = 0
top = tk.Tk()
canvas = tk.Canvas(top, width = 500, height = 500)
canvas.pack()

def nextImage(currImg,images):
    global count
    count = count + 1
    if (count < 0 or count == len(images)):
        count = 0
    newImg = tk.PhotoImage(file="Data/" + images[count])
    canvas.itemconfig(currImg,image = newImg)
    messagebox.showinfo("hello", "hi")



#def doTheCanny(image):
#    img = cv2.imread(image,0)
#    imgC = cv2.Canny(img, 100, 200)
#    plt.subplot(122), plt.imshow(imgC, cmap='gray')
#    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#    return plt

def main():
    images = os.listdir("Data/")
    lab = tk.Label(top, text= images[count])
    lab.pack()
    img = tk.PhotoImage(file="Data/" + images[count])

    img_on_canvas = canvas.create_image(0, 0, anchor=tk.NW, image=img)
    bNext = tk.Button(top, text = "Next" ,fg='white', bg='purple', font=('comicsans', 12),command= lambda :nextImage(img_on_canvas,images))
    bNext.pack(side="right", expand=True, padx=2, pady=2)
    # bPrevious = tk.Button(top, text = "Previous" ,fg='white', bg='purple', font=('comicsans', 12), command=nextImage)
    # bPrevious.pack(side="left", expand=True, padx=4, pady=2)
    #imgC = doTheCanny(images[count])
    #orig.create_image(20, 20, anchor=NW, image=imgC)
    top.mainloop()

if __name__ == "__main__":
    main()




