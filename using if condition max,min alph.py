# alphabet = ["apple,banana,orange,kiwi,grape"]
# min = alphabet['apple']
# max = alphabet['grape']
# for i in range(len(alphabet)):
#     if alphabet[i] < max:
#         max = alphabet[i]
#         print("min:", min)
#     elif alphabet[i] < max:
#         print("max:", max)

def find_max_min_alphabet(input_list):
    if not input_list:
        print("The list is empty.")
        return

    # Find maximum and minimum elements based on alphabetical order
    max_alphabet = max(input_list, key=lambda x: x.lower())
    min_alphabet = min(input_list, key=lambda x: x.lower())

    print(f"The maximum alphabet: {max_alphabet}")
    print(f"The minimum alphabet: {min_alphabet}")

# Example usage:
my_list = ["apple", "Orange", "banana", "Grapes", "kiwi"]
find_max_min_alphabet(my_list)

