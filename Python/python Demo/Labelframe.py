from tkinter import *

loss = Tk()
loss.title("Visual")
loss.geometry("500x500+500+100")

labelframe1=LabelFrame(loss, text= "Your details:")
labelframe1.pack(fill="both",expand="yes")

toplabel=Label(labelframe1,text="Prasanth 27/07/2000 9361216766")
toplabel.pack()

labelframe2=LabelFrame(loss, text= "My details:")
labelframe2.pack(fill="both",expand="yes")

bottomlabel=Label(labelframe2, text="Saran 16/01/2003 7092626320")
bottomlabel.pack()



loss.mainloop()