class emp:
    def __init__(self,n,s):
        self.n=n
        self.s=s
    def inc(self,p):
        self.s=self.s+(self.s*p/100)
    def pr(self):
        print("emp:",self.n,"salary:",self.s) 
e1=emp("kavya",1000)
e1.inc(10)
e1.pr()
e2=emp("deeksha",2000)
e2.inc(20)
e2.pr()
e3=emp("laxmi",3000)
e3.inc(30)
e3.pr()
