# Create a list from 0 to 100 using a for loop
my_list = list(range(101))
print("Original List:", my_list)

# Slice the list from index 0 to 50
sliced_list = my_list[:50]

# Print the sliced list
print("Sliced List (0 to 49):", sliced_list)

# Append numbers from 50 to 60 to the sliced list
sliced_list.extend(range(50, 61))

# Print the updated list
print("Updated List (Appended 50 to 60):", sliced_list)

# Remove the element at index 49
if len(sliced_list) > 49:
    removed_element = sliced_list.pop(49)
    print(f"Removed element at index 49: {removed_element}")
else:
    print("List length is less than 50, cannot remove element at index 49")

# Print the final list
print("Final List:", sliced_list)


# list using for_loop(0,100)
# for x in range(0,100):
#     print(x)
#     print(x[0:50])
#     print(x.append('60'))

