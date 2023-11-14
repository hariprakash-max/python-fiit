# area of circle
r=float(input("enter radius of circle:"))
area=2*3.14*r*r
print("area of circle is",area)

# area of triangle

b=float(input("enter height:"))
h=float(input("enter base:"))
area=0.5*b*h
print("area of triangle",area)

# area of rectangle
length=float(input("enter the length:"))
breadth=float(input("enter the breadth:"))
area=length*breadth
print("area of rectangle is",area)

# perimeter of circle
r=int(input("enter the radius:"))
perimeter=2*3.14*r
print("perimeter of circle is",perimeter)

# find the minimum and maximum numbers
numbers=[1,2,3,4,5,6,7,8,9,10]
min=numbers[0]
max=numbers[0]
for i in range(len(numbers)):
    if numbers[i]>max:
        max=numbers[i]
    elif numbers[i]<min:
        print("min:",min)
        print("max:",max)

