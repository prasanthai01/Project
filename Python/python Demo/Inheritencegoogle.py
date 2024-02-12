class google:
    def __init__(self,stab,ntab):
        self.searchtab = stab
        self.newtab = ntab

    def printname(self):
        print(self.stab,self.ntab)

y = google()
y.printname("chrome", "opentab")



        