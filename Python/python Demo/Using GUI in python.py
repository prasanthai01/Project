from tkinter import *

app =Tk()
app.title("My first python GUI app")
app.geometry("500x500+500+100")
app.config(bg="Green")
#app.state("zoomed")

def clickresult():
    a=17
    b=18
    c=a+b
    lbltitle.config(text=c,fg="Blue")

lbltitle=Label(app,text="Arithemetic Operations")
lbltitle.grid(row=0, column=1, padx=50, pady=40) 

inputbox1=Entry(app,width=30)
inputbox1.grid(row=0, column=2)


lbltitle=Label(app,text="Today topic is cook")
lbltitle.grid(row=1, column=1, padx=40, pady=40)

inputbox2=Entry(app,width=40)
inputbox2.grid(row=1, column=2)

clickme=Button(app,text="Addition",command=clickresult)
clickme.grid(row=6,column=2)

app.mainloop()