from tkinter import *
import tkinter.messagebox
from tkinter import Button
from tkinter import Tk, Frame, Entry, RIGHT  
import tk
import math

# main window
root =Tk()
root.title("Scientific Calculator")
root.configure(background="powder blue")
root.resizable(width=False, height=False)
root.geometry("480x568+0+0")

# frame for the calculator content
calc = Frame(root)
calc.grid()

# Class for calculator input handling
class Calc:
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = textDisplay.get() 
        secondnum = str(num)

        if self.input_value:
            self.current = secondnum  
            self.input_value = False
        else:
            if secondnum == ".": 
                if firstnum in secondnum: 
                    return
            self.current = firstnum + secondnum

        self.display(self.current)  

    def display(self,value):
        textDisplay.delete(0,END)
        textDisplay.insert(0,value)

    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total==float(textDisplay.get())

    def valid_function(self):
        if self.op=="add":
            self.total+=self.current
        if self.op=="sub":
            self.total-=self.current
        if self.op=="multi":
            self.total *=self.current
        if self.op=="divide":
            self.total/=self.current
        if self.op=="mod":
            self.total %=self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)

    def opetator(self,op):
        self.current=float(self.total)
        if self.check_sum:
            self.valid_function
        elif not self.result:
            self.total=self.current
            self.input_value=TRUE
        self.check_sum=TRUE
        self.op=op
        self.result=False

    def pi(self):
        self.result=False
        self.current=math.pi
        self.display(self.current)
    def tau(self):
        self.result=False
        self.current=math.tau
        self.display(self.current)
    def e(self):
        self.result=False
        self.current=math.e
        self.display(self.current)
    def ClearEntry(self):
        self.result=False
        self.current="0"
        self.display(0)
        self.input_value=True
    def all_clear_entry(self):
        self.ClearEntry()
        self.total=0
    def mathsPM(self):
        self.result=False
        self.current=-float(textDisplay.get())
        self.display(self.current)
    def squared(self):
        self.result=False
        self.current=math.sqrt (float(textDisplay.get()))
        self.display(self.current)
    def cos(self):
        self.result=False
        self.current=math.cos(math.radians(float(textDisplay.get())))
        self.display(self.current)
    def cosh(self):
        self.result=False
        self.current=math.cosh(math.radians(float(textDisplay.get())))
        self.display(self.current)
    def sin(self):
        self.result=False
        self.current=math.sin(math.radians(float(textDisplay.get())))
        self.display(self.current)
    def sinh(self):
        self.result=False
        self.current=math.sinh(math.radians(float(textDisplay.get())))
        self.display(self.current)
    def tan(self):
        self.result=False
        self.current=math.tan(math.radians(float(textDisplay.get())))
        self.display(self.current)
    def tanh(self):
        self.result=False
        self.current=math.tanh(math.radians(float(textDisplay.get())))
        self.display(self.current)
    def log10(self):
        self.result=False
        self.current=math.log10(math.radians(float(textDisplay.get())))
        self.display(self.current)
    def log2(self):
        self.result=False
        self.current=math.log2(math.radians(float(textDisplay.get())))
        self.display(self.current)
    def log1p(self):
        self.result=False
        self.current=math.log1p(math.radians(float(textDisplay.get())))
        self.display(self.current)
    def degrees(self):
        self.result=False
        self.current=math.degrees(math.radians(float(textDisplay.get())))
        self.display(self.current)
    def lgamma(self):
        self.result=False
        self.current=math.lgamma(math.radians(float(textDisplay.get())))
        self.display(self.current)
    def expm1(self):
        self.result=False
        self.current=math.expm1(math.radians(float(textDisplay.get())))
        self.display(self.current)
    def asinh(self):
        self.result=False
        self.current=math.asin(math.radians(float(textDisplay.get())))
        self.display(self.current)
    def acosh(self):
        self.result=False
        self.current=math.acosh(math.radians(float(textDisplay.get())))
        self.display(self.current)
    def log(self):
        self.result=False
        self.current=math.log(math.radians(float(textDisplay.get())))
        self.display(self.current)
    def modf(self):
        self.result=False
        self.current=math.modf(math.radians(float(textDisplay.get())))
        self.display(self.current)
    def exp(self):
        self.result=False
        self.current=math.exp(math.radians(float(textDisplay.get())))
        self.display(self.current)







added_value=Calc()
#############################Display box and buttons
#display the solution box
textDisplay = Entry(calc, font=("Arial", 20, "bold"), bg="powder blue", bd=30, width=28, justify=RIGHT)
textDisplay.grid(row=0, column=0, columnspan=4, pady=10)
textDisplay.insert(0,"0")
#number pad
numberpad = "789456123" 
btn = [] 
i = 0
for j in range(2, 5): 
    for k in range(3):  
        btn.append(Button(calc, width=6, height=2, font=("Arial", 20, "bold"), bd=4,
                          text=numberpad[i])) 
        btn[i].grid(row=j, column=k, pady=1)  
        btn[i][COMMAND]=lambda X =numberpad [i]:added_value.numberEnter(X)
        i += 1  


# Create and place buttons in one step
# Row 1
Button(calc, text=chr(67), width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue",command=added_value.all_clear_entry).grid(row=1, column=0, pady=1)
Button(calc, text=chr(67) + chr(69), width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue",command=added_value.ClearEntry).grid(row=1, column=1, pady=1)
Button(calc, text="√", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue",command=added_value.squared).grid(row=1, column=2, pady=1)
Button(calc, text="+", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue",command=lambda:added_value.opetator("add")).grid(row=1, column=3, pady=1)

# Row 2
Button(calc, text="-", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue",command=lambda:added_value.opetator("sub")).grid(row=2, column=3, pady=1)

# Row 3
Button(calc, text="÷", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue",command=lambda:added_value.opetator("divde")).grid(row=3, column=3, pady=1)

# Row 4
Button(calc, text="*", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue",command=lambda:added_value.opetator("multi")).grid(row=4, column=3, pady=1)

# Row 5
Button(calc, text="0", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue",command=lambda:added_value.numberEnter("0")).grid(row=5, column=0, pady=1)
Button(calc, text=".", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue",command=lambda:added_value.numberEnter(".")).grid(row=5, column=1, pady=1)
Button(calc, text="+/-", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=5, column=2, pady=1)
Button(calc, text="=", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue",command=added_value.sum_of_total).grid(row=5, column=3, pady=1)


######################################### Button for Scientific Calculator
# Create and grid buttons in one step
# Row 1
Button(calc, text="π", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue",command=added_value.pi).grid(row=1, column=4, pady=1)
Button(calc, text="cos", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue",command=added_value.cos).grid(row=1, column=5, pady=1)
Button(calc, text="tan", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue",command=added_value.tan).grid(row=1, column=6, pady=1)
Button(calc, text="sin", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue",command=added_value.sin).grid(row=1, column=7, pady=1)

# Row 2
Button(calc, text="2π", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue",command=added_value.tau).grid(row=2, column=4, pady=1)
Button(calc, text="cosh", width=6, height=2, font=("Arial", 20, "bold"), bd=4,command=added_value.cosh).grid(row=2, column=5, pady=1)
Button(calc, text="tanh", width=6, height=2, font=("Arial", 20, "bold"), bd=4,command=added_value.tanh).grid(row=2, column=6, pady=1)
Button(calc, text="sinh", width=6, height=2, font=("Arial", 20, "bold"), bd=4,command=added_value.sinh).grid(row=2, column=7, pady=1)

# Row 3
Button(calc, text="Log", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue",command=added_value.log).grid(row=3, column=4, pady=1)
Button(calc, text="Exp", width=6, height=2, font=("Arial", 20, "bold"), bd=4,command=added_value.exp).grid(row=3, column=5, pady=1)
Button(calc, text="Mod", width=6, height=2, font=("Arial", 20, "bold"), bd=4,command=added_value.modf).grid(row=3, column=6, pady=1)
Button(calc, text="e", width=6, height=2, font=("Arial", 20, "bold"), bd=4,command=added_value.e).grid(row=3, column=7, pady=1)

# Row 4
Button(calc, text="ln", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue",command=added_value.log2).grid(row=4, column=4, pady=1)
Button(calc, text="deg", width=6, height=2, font=("Arial", 20, "bold"), bd=4,command=added_value.degrees).grid(row=4, column=5, pady=1)
Button(calc, text="acosh", width=6, height=2, font=("Arial", 20, "bold"), bd=4,command=added_value.acosh).grid(row=4, column=6, pady=1)
Button(calc, text="asinh", width=6, height=2, font=("Arial", 20, "bold"), bd=4,command=added_value.asinh).grid(row=4, column=7, pady=1)

# Row 5
Button(calc, text="Log10", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue",command=added_value.log10).grid(row=5, column=4, pady=1)
Button(calc, text="Log1p", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue",command=added_value.log1p).grid(row=5, column=5, pady=1)
Button(calc, text="expm1", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue",command=added_value.expm1).grid(row=5, column=6, pady=1)
Button(calc, text="gamma", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue",command=added_value.lgamma).grid(row=5, column=7, pady=1)

lblDisplay=Label(calc,text="Scientific Calculator",font=("arial",30,"bold"),justify=CENTER)
lblDisplay.grid(row=0,column=4,columnspan=4)



#####################       menu bar  #####################
def iExit():
    iExit=tkinter.messagebox.askyesno("Scientific Calculator ","Confirm ,if you want to exit")
    if iExit>0:
        root.destroy()
        return

def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x560+0+0")
    
def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("944x568+0+0")


menubar = Menu(root)

# file menu with no tear-off
filemenu = Menu(menubar, tearoff=0)  
menubar.add_cascade(label="File", menu=filemenu)
#file menu
filemenu.add_command(label="Standard",command=Standard) 
filemenu.add_command(label="Scientific",command=Scientific)
filemenu.add_command(label="Exit", command=iExit)  

# Edit menu with no tear-off
editmenu = Menu(menubar, tearoff=0)  
menubar.add_cascade(label="Edit", menu=editmenu) 
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")

#help menu 
helpmenu = Menu(menubar, tearoff=0)  
menubar.add_cascade(label="Help", menu=helpmenu) 
helpmenu.add_command(label="View Help")



root.config(menu=menubar)  
root.mainloop()
