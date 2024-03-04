import mysql.connector 
from tkinter import *

class DBMaanipulate:
    def __init__(self):
        print("Welcome to Db Manipulation ")

    def returnmsg(self):    
        return "connected"
    
    def mydbconnection(self):
        con=mysql.connector.connect(
            host="192.168.1.240",
            user="AIBATCH01",
            password="AI@123",
            database="ai_prasanth"
        )
        return con
    
    def insertvalues(self,Name,age,Tamil,English,Maths,Science,Social_Science):
        student_name=Name
        student_age=age
        st_mk_tam=Tamil
        st_mk_eng=English
        st_mk_math=Maths
        st_mk_sci=Science
        st_mk_s_sci=Social_Science
        data=self.mydbconnection()
        result=data.cursor()

        stmts="insert into Student_Mark_List(Name,age,Tamil,English,Maths,Science,Social_Science)  values(" +'"'+ student_name + '"' +","+ str(student_age) + "," + str(st_mk_tam) + ","+str(st_mk_eng) +"," + str(st_mk_math) + "," + str(st_mk_sci) + "," + str(st_mk_s_sci) + ");"
        result.execute(stmts)
        print(stmts)

        data.commit()

        return(str(result.rowcount)+"row Inserted")
    
    def upadtevalues(self,sno,Name,age,Tamil,English,Maths,Science,Social_Science):
        student_S_no=sno
        student_name=Name
        student_age=age
        st_mk_tam=Tamil
        st_mk_eng=English
        st_mk_math=Maths
        st_mk_sci=Science
        st_mk_s_sci=Social_Science

        data=self.mydbconnection()
        result=data.cursor()
        
        stmts1="upadte Student_Mark_List set name=(%s) where sno=(%s)"
        valuepass=(student_name,student_S_no)
        result.execute(stmts1,valuepass)
        print(stmts1)
        data.commit()
        return(str(result.rowcount)+"row updated")
        # stmts="UPDATE student_mark_list SET (Name,Age,Tamil,English,Maths,Science,Social_Science) (" + str(student_S_no=(%s) + ","str(Name =(%s)),Age` = <{Age: }>,Tamil` = <{Tamil: }>,`English` = <{English: }>,Maths` = <{Maths: }>,Science` = <{Science: }>,Social_Science` = <{Social_Science: }WHERE `S_no` = <{expr}>");"
