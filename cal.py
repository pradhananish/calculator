from tkinter import *
import math
import tkinter.messagebox
from tkinter import ttk
import mysql.connector
import random



class Calculator():
    def __init__(self,root):
        self.root=root 
        self.root.title("Calculator")
        self.root.geometry("560x460+0+0")
        self.root.configure(bg="gray")

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=0,width=560,height=460)

        
        menubar=Menu()
        filemenu=Menu(menubar,tearoff='0')
        menubar.add_cascade(label="File",menu=filemenu)
        filemenu.add_command(label="Scientific")
        filemenu.add_command(label="Standard")
        filemenu.add_command(label="Exi5")



if __name__ == '__main__':
    root=Tk()
    object=Calculator(root)
    root.mainloop()


