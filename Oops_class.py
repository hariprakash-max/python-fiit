class student:
    def __init__(a,rollno,name,address):
     a.rollno = rollno
     a.name = name
     a.address = address
    def displaystudent(a):
     print("rollno:",a.rollno,"name:",a.name,"address:",a.address)
emp1=student(121,"ajeet","chennai")
emp2=student(122,"sonu", "avadi")
emp1.displaystudent()
emp2.displaystudent()


class manf:
     def __init__(self,chairheight,chairweight):
        self.chairheight=chairheight
        self.chairweight=chairweight
     def manf(self):
        print("chairheight",self.chairheight,"chairweight",self.chairweight)
chair=manf(12,13)
chair.manf()

