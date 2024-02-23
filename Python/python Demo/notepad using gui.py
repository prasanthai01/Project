from tkinter import *
from tkinter import ttk
 
dheeran=Tk()
dheeran.title("Untitled - Notepad")
dheeran.geometry("500x500")
dheeran.state("zoomed")

def quit():
  dheeran.destroy()

menubar=Menu(dheeran)
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New", accelerator="Ctrl N")
filemenu.add_command(label="Open...", accelerator="Ctrl O")
filemenu.add_command(label="Save", accelerator="Ctrl S")
filemenu.add_command(label="Save as...")
filemenu.add_separator()
filemenu.add_command(label="Page Setup...", accelerator="Ctrl N")
filemenu.add_command(label="Print", accelerator="Ctrl P")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quit)


editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Undo", accelerator="Ctrl Z")
editmenu.add_command(label="Cut", accelerator="Ctrl X")
editmenu.add_command(label="Copy", accelerator="Ctrl C")
editmenu.add_command(label="Paste", accelerator="Ctrl V")
editmenu.add_command(label="Delete", accelerator="Del")
editmenu.add_separator()
editmenu.add_command(label="Find", accelerator="Ctrl F")
editmenu.add_command(label="Find Next...", accelerator="F3")
editmenu.add_command(label="Replace...", accelerator="Ctrl H")
editmenu.add_command(label="Go to...", accelerator="Ctrl G")
editmenu.add_separator()
editmenu.add_command(label="Select All", accelerator="Ctrl A")
editmenu.add_command(label="Time/Date", accelerator="F5 ")

formatmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Format",menu=formatmenu)
formatmenu.add_command(label="Word Wrop")
formatmenu.add_cascade(label="Font...")

viewmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="View",menu=viewmenu)
viewmenu.add_cascade(label="Staus Bar")

helpmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_cascade(label="View Help")
helpmenu.add_separator()
helpmenu.add_cascade(label="About Notepad")



dheeran.config(menu=menubar)
dheeran.mainloop()