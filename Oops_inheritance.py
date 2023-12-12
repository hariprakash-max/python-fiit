#inheritance
class animal:
    def eat(self):
        print("eating...")
class dog(animal):
    def bark(self):
        print("barking...")
d = dog()
d.eat()
d.bark()

# multilevel
class animal:
    def eat(self):
        print("eating...")
class dog(animal):
    def bark(self):
        print("barking...")
class babydog(dog):
    def weep(self):
        print("weeping...")
d=babydog()
d.eat()
d.bark()

# multiple inheritance
class first(object):
    def __init__(self):
        super(first,self).__init__()
        print("first")

class second(object):
    def __init__(self):
        super(second,self).__init__()
        print("second")
class third(second,first):
    def __init__(self):
        super(third,self).__init__()
        print("third")
third();

class student:
    def student_database(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
print("name",self.name,"age",self.age,"rollno",self.rollno)
class mark(student):
    def marklist(self,tamil,english,maths):
        self.tamil=tamil
        self.english=english
        self.maths=maths
print("tamil:",self.tamil,"english:",self.english,"maths:",self.maths)
obj=student()
obj.student_database("ramesh",'25','280')
obj.mark('23','45','280')