string = str(input("enter a string:"))
vowels = 0
for i in string:
    if(i=='a'or i=='e'or i=='i'or i=='o'or i=='u'):
        vowels = vowels+1
    print("No of vowels are:",vowels)

# to convert the string to upperletter
my_string = "hello"
print(my_string.upper())

# to find the ascii values
x = ord("A")
print(x)
y = chr(97)
print(y)