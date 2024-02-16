from tkinter import *

bike=Tk()

bike.title("Yamaha")
bike.geometry("500x500+500+100")
bike.state("zoomed")
bike.config(bg="Green")

def info():
    ib=(inputbox.get())
    ib1=(inputbox1.get())
    ib2=(inputbox2.get())
    outputbox.config(text="Hi"+" "+ib+" "+"You want this"+" "+ib1+" "+"And it cost Rs"+" "+ib2)
def Bio():
     ib=(inputbox.get())
     ib1=(inputbox1.get())
     ib2=(inputbox2.get())
     outputbox1.config(text="Hi"+" "+ib+" "+"You want this"+" "+ib1+" "+"And it cost Rs"+" "+ib2)

labeltitle=Label(bike,text="Give me your name:",bg="white",fg="blue")
labeltitle.grid(row=0,column=10,padx=40,pady=40)

inputbox=Entry(bike,text="")
inputbox.grid(row=0,column=250)


labeltitle1=Label(bike,text="Which bike you want:",bg="white",fg="blue")
labeltitle1.grid(row=2,column=10,padx=40,pady=40)


inputbox1=Entry(bike,text="")
inputbox1.grid(row=2,column=250)



labeltitle2=Label(bike,text="Price of bike:",bg="white",fg="blue")
labeltitle2.grid(row=4,column=10,padx=40,pady=40)


inputbox2=Entry(bike,text="")
inputbox2.grid(row=4,column=250)

clickButton=Button(bike,text="Submit",command=info)
clickButton.grid(row=15,column=447)

clickButton1=Button(bike,text="BIO",command=Bio)
clickButton1.grid(row=15,column=40)

outputbox=Label(bike,text="")
outputbox.grid(row=40,column=40)


outputbox1=Label(bike,text="")
outputbox1.grid(row=40,column=80)



mainloop()