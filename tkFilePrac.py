import tkinter as tk
from tkinter import *
from tkinter import filedialog

window = Tk()
window.title("Mo va Doc file")
window.geometry('300x250+300+300')

def openFile():
    filePick = open(filedialog.askopenfilenames())
    fileRead = filePick.read()
    filePick.close()

chooseFile = Button(text= "Choose File",command=openFile)
chooseFile.pack()

window.update()
window.mainloop()