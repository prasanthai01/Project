from tkinter import *

app =Tk()
app.title("My first python GUI app")
app.geometry("500x500+500+100")
app.config(bg="Green")
#app.state("zoomed")

def Addition():
    a=17
    b=18
    c=a+b
    lbltitle.config(text=c,fg="Blue")

def subraction():
    a=50
    b=20
    c=a-b
    lbltitle1.config(text=c,fg="Blue")

lbltitle=Label(app,text="Arithemetic Operations")
lbltitle.grid(row=0, column=1, padx=40, pady=40)

inputbox1=Entry(app,width=30)
inputbox1.grid(row=0, column=2)


lbltitle=Label(app,text="***")
lbltitle.grid(row=2, column=2, padx=40, pady=40)

inputbox2=Entry(app,width=40)
inputbox2.grid(row=1, column=2)

clickme1=Button(app,text="Addition",command=Addition)
clickme1.grid(row=6,column=2)


lbltitle1=Label(app,text="###")
lbltitle1.grid(row=3, column=4, padx=40, pady=40)

inputbox2=Entry(app,width=30)
inputbox2.grid(row=2, column=4)

clickme2=Button(app,text="Subraction",command=subraction)
clickme2.grid(row=7,column=4)

app.mainloop()