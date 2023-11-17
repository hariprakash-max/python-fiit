# # converting list into tuple and find datatype manual database(names) print 10 names in for_loop
#
# # Convert a list into a tuple
# # my_list = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry", "Ivy", "Jack"]
# # my_tuple = tuple(my_list)
#
# # Print the original list and the converted tuple
# # print("Original List:", my_list)
# # print("Converted Tuple:", my_tuple)
#
# # Manual Database: Names and Data Types
# # names_database = {}
#
# # Populate the database with names and their data types
# # for name in my_tuple[:10]:  # Print 10 names
# #    data_type = type(name).__name__
# #    names_database[name] = data_type
#
# # Print the names and their data types
# # print("\nDatabase of Names and Data Types:")
# # for name, data_type in names_database.items():
# #   print(f"{name}: {data_type}")

a = ["alice,bob,charlie,david,emily,frank,grace,hank,ivy,jack"]
print(list(a))
a.append('john')
print(a)
print(tuple(a))
print(type(a))
for i in range(0,10):
    print(a)
