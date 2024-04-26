from tkinter import *
import tkinter.messagebox
from tkinter import Button
from tkinter import Tk, Frame, Entry, RIGHT  
import tk

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
    def __init__(self, display):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False
        self.display_widget = display 

    def number_enter(self, num):
        self.result = False
        firstnum = self.display_widget.get()  # Get current text in display
        secondnum = str(num)

        if self.input_value:
            self.current = secondnum  # Start a new number
            self.input_value = False
        else:
            if secondnum == "." and "." in firstnum:  # Avoid multiple dots
                return
            self.current = firstnum + secondnum

        self.display(self.current)  # Update the display with the new value

    def display(self, value):
        self.display_widget.delete(0, END)  # Clear the current display
        self.display_widget.insert(0, value)  # Insert the new value


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
        btn[i]["command"]=lambda x = numberpad [i]:added_value.numberEnter(x)
        i += 1  


# Create and place buttons in one step
# Row 1
Button(calc, text=chr(67), width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=1, column=0, pady=1)
Button(calc, text=chr(67) + chr(69), width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=1, column=1, pady=1)
Button(calc, text="√", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=1, column=2, pady=1)
Button(calc, text="+", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=1, column=3, pady=1)

# Row 2
Button(calc, text="-", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=2, column=3, pady=1)

# Row 3
Button(calc, text="÷", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=3, column=3, pady=1)

# Row 4
Button(calc, text="*", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=4, column=3, pady=1)

# Row 5
Button(calc, text="0", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=5, column=0, pady=1)
Button(calc, text=".", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=5, column=1, pady=1)
Button(calc, text="+/-", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=5, column=2, pady=1)
Button(calc, text="=", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=5, column=3, pady=1)


######################################### Button for Scientific Calculator
# Create and grid buttons in one step
# Row 1
Button(calc, text="π", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=1, column=4, pady=1)
Button(calc, text="cos", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=1, column=5, pady=1)
Button(calc, text="tan", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=1, column=6, pady=1)
Button(calc, text="sin", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=1, column=7, pady=1)

# Row 2
Button(calc, text="2π", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=2, column=4, pady=1)
Button(calc, text="cosh", width=6, height=2, font=("Arial", 20, "bold"), bd=4).grid(row=2, column=5, pady=1)
Button(calc, text="tanh", width=6, height=2, font=("Arial", 20, "bold"), bd=4).grid(row=2, column=6, pady=1)
Button(calc, text="sinh", width=6, height=2, font=("Arial", 20, "bold"), bd=4).grid(row=2, column=7, pady=1)

# Row 3
Button(calc, text="Log", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=3, column=4, pady=1)
Button(calc, text="Exp", width=6, height=2, font=("Arial", 20, "bold"), bd=4).grid(row=3, column=5, pady=1)
Button(calc, text="Mod", width=6, height=2, font=("Arial", 20, "bold"), bd=4).grid(row=3, column=6, pady=1)
Button(calc, text="e", width=6, height=2, font=("Arial", 20, "bold"), bd=4).grid(row=3, column=7, pady=1)

# Row 4
Button(calc, text="ln", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=4, column=4, pady=1)
Button(calc, text="deg", width=6, height=2, font=("Arial", 20, "bold"), bd=4).grid(row=4, column=5, pady=1)
Button(calc, text="acosh", width=6, height=2, font=("Arial", 20, "bold"), bd=4).grid(row=4, column=6, pady=1)
Button(calc, text="asinh", width=6, height=2, font=("Arial", 20, "bold"), bd=4).grid(row=4, column=7, pady=1)

# Row 5
Button(calc, text="Log10", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=5, column=4, pady=1)
Button(calc, text="Log1p", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=5, column=5, pady=1)
Button(calc, text="expm1", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=5, column=6, pady=1)
Button(calc, text="gamma", width=6, height=2, font=("Arial", 20, "bold"), bd=4, bg="powder blue").grid(row=5, column=7, pady=1)

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
