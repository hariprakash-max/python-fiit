class complexnumber:
    def __init__(self,r=0,i=0):
        self.real=r
        self.img=i
    def getData(self):
        print("{0}+{1}j".format(self.real,self.img))
c1=complexnumber(10,9)
c1.getData()