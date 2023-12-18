# write a class with two private class variables and print the sum using a method
class sample:
    def __init__(self,n1,n2):
        self.__n1 = n1
        self.__n2 = n2
    def display(self):
        print("class variable 1:",self.__n1)
        print("class variable 2:",self.__n2)
        print("sum:",self.__n1+self.__n2)
s=sample(10,20)
s.display()

