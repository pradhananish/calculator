from tkinter import *
import tkinter.messagebox

# main window
root = Tk()
root.title("Scientific Calculator")
root.configure(background="powder blue")
root.resizable(width=False, height=False)
root.geometry("480x560+0+0")

# frame for the calculator content
calc = Frame(root)
calc.grid()

#####################       menu bar  #####################
def iExit():
    iExit=tkinter.messagebox.askyesno("Scientific Calculator ","Confirm ,if you want to exit")
    if iExit>0:
        root.destroy()
        return


menubar = Menu(root)

# file menu with no tear-off
filemenu = Menu(menubar, tearoff=0)  
menubar.add_cascade(label="File", menu=filemenu)
#file menu
filemenu.add_command(label="Standard") 
filemenu.add_command(label="Scientific")
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
