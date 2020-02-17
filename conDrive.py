#from pydrive.auth import GoogleAuth
#from pydrive.drive import GoogleDrive


import numpy as np
import os
from tkinter import *
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from PIL import Image,ImageTk,ImageFilter,ImageOps
from tkinter import messagebox




#gauth = GoogleAuth()
#gauth.LocalWebserverAuth()

#drive = GoogleDrive(gauth)
#file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
#for file1 in file_list:
#  #print('title: %s, id: %s' % (file1['title'], file1['id']))
#  if  file1['title']=="Classify lesions- Machon Lev Project":
#         #for file2 in file1:
#         # print('title: %s, id: %s' % (file2['title'], file2['id']))
#          file2=drive.ListFile({'q': "'%s' in parents and trashed=false" % file1['id']}).GetList()
#          for file3 in file2:
#             print((file3['title']))
#             if file3['title']=="Data Images":
#               file4=drive.ListFile({'q': "'%s' in parents and trashed=false" % file3['id']}).GetList()
#               for file5 in file4:
#                 print((file5['title']))
#                 if file5['title'] == "Gums (gingiva)":
#                   file6=drive.ListFile({'q': "'%s' in parents and trashed=false" % file5['id']}).GetList()
#                  # os.mkdir('Gums (gingiva)')
#                   for file7 in file6:
#                      print((file7['title']))
#                      #file7.GetContentFile('Gums (gingiva)/%s'%(file7['title']))


count = 0
N_directory = r'C:\Users\Netanel Moshehayev\PycharmProjects\myProject\Gums (gingiva)'
file_list=os.listdir(N_directory)
file_list=sorted(file_list, key=lambda x: int("".join([i for i in x if i.isdigit()])))
for x in file_list:
  print(x)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        # added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Show Img", command=self.showImg)
        edit.add_command(label="Show Text", command=self.showText)
        edit.add_command(label="next Img", command=self.nextImg)
        # added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)

       # widget = Button(self, text='Mouse Clicks')
       # widget.pack()
       # widget.bind('<Button-1>', self.hello())
       # widget.bind('<Double-1>', self.quit())
       # widget.mainloop()
        B = tkinter.Button(self, text="next_image", command = self.nextImg)
        #B.pack( side = BOTTOM )
        B.grid(row = 1, column = 0)
    def helloCallBack(self):
        messagebox.showinfo("Hello Python", "Hello World")
    #def hello(self,event):
     #   print("Single Click, Button-l")

    #def quit(self,event):
     #   print("Double Click, so let's stop")
      #  import sys;
       # sys.exit()


    def showImg(self):
        load = Image.open("Gums (gingiva)/GG_1.jpg")
        render = ImageTk.PhotoImage(load)
        imageCV=cv2.imread("Gums (gingiva)/GG_1.jpg")
        if(os.path.exists('./Gums (gingiva)-Canny')==False):
             os.mkdir('Gums (gingiva)-Canny')
        directory= r'C:\Users\Netanel Moshehayev\PycharmProjects\myProject'
        N_directory = r'C:\Users\Netanel Moshehayev\PycharmProjects\myProject\Gums (gingiva)-Canny'
        os.chdir(N_directory)
        cv2.imwrite("(canny)GG_1.jpg",cv2.Canny(cv2.cvtColor(imageCV, cv2.COLOR_BGR2GRAY),100,350))
        os.chdir(directory)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.grid(row = 0, column = 0)
        #img.place(x=0, y=0)
        #img.pack( side = LEFT )



    def showText(self):
        text = Label(self, text="Hey there good lookin!")
        text.pack()

    def nextImg(self):
        global count
        #global file6
        global  file_list
        for label in self.grid_slaves():
            if label.grid_info().get('row')==0:
                label.grid_forget()
        #if (count==len(file6)):
        if (count==len(file_list)):
                 count=0
        #load = Image.open('Gums (gingiva)/%s'%file6[count]['title'])
        load = Image.open('Gums (gingiva)/%s'%file_list[count])
        render = ImageTk.PhotoImage(load)

        if (os.path.exists('./Gums (gingiva)-Canny') == False):
            os.mkdir('Gums (gingiva)-Canny')
        #imageCV = cv2.imread('Gums (gingiva)/%s'%file6[count]['title'])
        imageCV = cv2.imread('Gums (gingiva)/%s'%file_list[count])
        directory = r'C:\Users\Netanel Moshehayev\PycharmProjects\myProject'
        N_directory = r'C:\Users\Netanel Moshehayev\PycharmProjects\myProject\Gums (gingiva)-Canny'
        os.chdir(N_directory)
        if(os.path.exists('./(canny)%s'%file_list[count])==False):
            cv2.imwrite('(canny)%s'%file_list[count], cv2.Canny(cv2.cvtColor(imageCV, cv2.COLOR_BGR2GRAY), 100, 350))
        os.chdir(directory)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        #img.place(x=0, y=0)
        img.grid(row=0, column=0)
        count = count + 1

    def client_exit(self):
        exit()


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("1000x1000")

# creation of an instance
app = Window(root)

# mainloop
root.mainloop()












