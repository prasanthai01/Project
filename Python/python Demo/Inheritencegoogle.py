class google:
    def __init__(self,fname,lname,flname,):
        self.firstname = fname 
        self.lastname = lname
        self.fullname = flname

    def printname(self):
        print(self.fname,self.lname,self.flname)

y = google
y.printname("Veera ", "Raghavan", "Veera Raghavan")
print(y)



        