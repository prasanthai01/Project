from tkinter import *

def math_operation():
    ravanan=Tk()
    ravanan.title("Mathematical Operations")
    ravanan.geometry("500x500+500+500")
    ravanan.state("zoomed")

    def Addition():
        a=int(tbEntrya.get())
        b=int(tbEntryb.get())
        c=a+b
        labeloutput.config(text=c)
    def Subtraction():
        a=int(tbEntrya.get())
        b=int(tbEntryb.get())
        c=a-b
        labeloutput.config(text=c)
    def Multiplication():
        a=int(tbEntrya.get())
        b=int(tbEntryb.get())
        c=a*b
        labeloutput.config(text=c)
    def Division():
        a=int(tbEntrya.get())
        b=int(tbEntryb.get())
        c=a/b
        labeloutput.config(text=c)

    Labeltitle=Label(ravanan,text="Arithematic Operations",font=("ALGERIAN",16),fg="green")
    Labeltitle.grid(row=0,column=20)

    label1msg=Label(ravanan,text="Enter the Value of A",font=("Lucida Calligraphy",14),fg="blue")
    label1msg.grid(row=1,column=20,pady=20)
    tbEntrya=Entry(ravanan, width=60)
    tbEntrya.grid(row=1,column=25)

    label2msg=Label(ravanan,text="Enter the Value of B",font=("Lucida Calligraphy",14),fg="blue")
    label2msg.grid(row=2,column=20,pady=20)
    tbEntryb=Entry(ravanan, width=60)
    tbEntryb.grid(row=2,column=25)

    labeloutput=Label(ravanan,text=" ")
    labeloutput.grid(row=3,column=30,pady=20)


    btnadd=Button(ravanan,text="Addition",font=("calibri",14),fg="White",bg="Black",command=Addition)
    btnadd.grid(row=5,column=1)

    btnsub=Button(ravanan,text="Subtraction",font=("calibri",14),fg="White",bg="Black",command=Subtraction)
    btnsub.grid(row=5,column=2)

    btnmul=Button(ravanan,text="Multiplication",font=("calibri",14),fg="White",bg="Black",command=Multiplication)
    btnmul.grid(row=5,column=3)

    btndiv=Button(ravanan,text="Division",font=("calibri",14),fg="White",bg="Black",command=Division)
    btndiv.grid(row=5,column=4)


    ravanan.mainloop()