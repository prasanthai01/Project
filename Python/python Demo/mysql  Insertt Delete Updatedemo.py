from tkinter import *
import mysql.connector



zara=Tk()
zara.title("MARK LIST")
zara.geometry("500x500+500+100")
zara.config(bg="Light blue")
zara.state("zoomed")


def mydbconnection():
   con=mysql.connector.connect(

    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="ai_prasanth"
   )
   return con      

def Insert():
    a=(tbinput1.get())
    b=(tbinput2.get())
    c=(tbinput3.get())
    d=(tbinput4.get())
    e=(tbinput5.get())
    f=(tbinput6.get())
    g=(tbinput7.get())
        

    cl=mydbconnection()
    result=cl.cursor()
    
    sql="INSERT INTO Mark_list(name,TAMIL,ENGLISH,MATHS,PHYSICS,CHEMISTRY,cOMPUTER_SCIENCE) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    val=(a,b,c,d,e,f,g)
    result.execute(sql, val)
    cl.commit()

    print(result.rowcount, "row inserted")

def Delete():
    a=(tbinput1.get())

    cl=mydbconnection()       
    result=cl.cursor()
    
    sql="Delete from Mark_list where name=(%s)"
    val=(a,)
    result.execute(sql, val)
    cl.commit()

    print(result.rowcount, "row deleted")
    
def Update():
    a=(tbinput1.get())

    cl= mydbconnection()
    result=cl.cursor()

    sql="Update from Mark_list set name=(%s) where name=(%s)"
    val=(a,)
    result.execute(sql,val)
    cl.commit()

    print(result.rowcount, "row Update")

#label    
labelTitle=Label(zara,text="MARK LIST")
labelTitle.grid(row=0,column=10,padx=150, pady=30)


label=Label(zara,text="NAME")
label.grid(row=1,column=8,padx=20,pady=20)

labelmsg1=Label(zara,text="TAMIL")
labelmsg1.grid(row=2,column=8,padx=20,pady=20)


labelmsg2=Label(zara,text="ENGLISH")
labelmsg2.grid(row=3,column=8,padx=20,pady=20)

labelmsg3=Label(zara,text="MATHS")
labelmsg3.grid(row=4,column=8,padx=20,pady=20)

labelmsg4=Label(zara,text="PHYSICS")
labelmsg4.grid(row=5,column=8,padx=20,pady=20)

labelmsg5=Label(zara,text="CHEMISTRY")
labelmsg5.grid(row=6,column=8,padx=20,pady=20)

labelmsg6=Label(zara,text="COMPUTER SCIENCE")
labelmsg6.grid(row=7,column=8,padx=20,pady=20)

#tbinput
tbinput1=Entry(zara,width=30)
tbinput1.grid(row=1,column=10)

tbinput2=Entry(zara,width=30)
tbinput2.grid(row=2,column=10)

tbinput3=Entry(zara,width=30)
tbinput3.grid(row=3,column=10)

tbinput4=Entry(zara,width=30)
tbinput4.grid(row=4,column=10)

tbinput5=Entry(zara,width=30)
tbinput5.grid(row=5,column=10)

tbinput6=Entry(zara,width=30)
tbinput6.grid(row=6,column=10)


tbinput7=Entry(zara,width=30)
tbinput7.grid(row=7,column=10)

#btn
btn=Button(zara,text="Insert", command=Insert)
btn.grid(row=8, column=2,padx=20,pady=20)
btn.configure(bg="Light Green", fg="Black")


btn2=Button(zara,text="Delete", command=Delete)
btn2.grid(row=8, column=3,padx=20,pady=20)
btn2.configure(bg="Light Green", fg="Black")


btn3=Button(zara,text="Update", command=Delete)
btn3.grid(row=8, column=4,padx=20,pady=20)
btn3.configure(bg="Light Green", fg="Black")

#labeloutput

labeloutput1=Label(zara,text="")
labeloutput1.grid(row=10,column=10, pady=20)



zara.mainloop()