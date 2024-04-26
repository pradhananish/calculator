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
        self.root.configure(background="gray")

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=0,width=560,height=460)

        lbl_title=Label(main_frame, text="Calculator", font=("time new roman",16,"bold"), fg="black", bd=1, relief=RIDGE)
        lbl_title.place(x=0,y=0, width=560, height=20)


if __name__ == '__main__':
    root=Tk()
    object=Calculator(root)
    root.mainloop()


