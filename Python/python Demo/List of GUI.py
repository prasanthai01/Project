from tkinter import *

bike=Tk()

bike.title("Yamaha")
bike.geometry("500x500+500+100")
bike.config(bg="Green")
#bike.state("zoomed")


lbl=Label(bike,text="List of Yamaha bikes:",fg="Blue",bg="Yellow")
lbl.grid(row=0,column=1,padx=50,pady=50)

listbox=Listbox(bike)

listbox.insert(1,"Yamaha Rx100")
listbox.insert(2,"Master Toque 15")
listbox.insert(3,"Master Toque 15 ver2")
listbox.insert(4,"Yamaha R15")
listbox.insert(5,"Yamaha R15 ver2")
listbox.insert(6,"Yamaha R15 ver3")

listbox.configure(fg="Orange",bg="Black")

lbl.pack()
listbox.pack()


bike.mainloop()