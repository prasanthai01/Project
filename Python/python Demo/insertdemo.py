from tkinter import *
import mysql.connector

zara = Tk()
zara.title("('Insert into Mysql DB Demo')")
zara.geometry("500x500")

frameleft=Frame(zara, bg="black",width=500,height=500)
frameleft.pack(side= LEFT)

frameright=Frame(zara, bg="red",width=500,height=500)
frameright.pack(side= RIGHT)

lbl_Title_of_operation =Label(frameleft,text="INSERT INTO MYSQL DB DEMO").pack(side=TOP,padx=40,pady=40)
#lbl_Title_of_operation.grid(frameleft,text="Name")
#lblTamil=Label(frameleft,text="Tamil")
#lblTamil.grid()



zara.mainloop()