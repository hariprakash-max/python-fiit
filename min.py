# find the minimum and maximum numbers
numbers=[1,2,3,4,5,6,7,8,9,10]
min=numbers[0]
max=numbers[0]
for i in range(len(numbers)):
    if numbers[i]>max:
        max=numbers[i]
        print("min:", min)
    elif numbers[i]<min:
        print("max:",max)
