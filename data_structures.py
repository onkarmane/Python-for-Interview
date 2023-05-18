# Different data stuctures can be handled in differnt way
# 1 . Data Structures
# names = ['John123', 'Smith3', 'is', 'the']

# output = {}
# for item in names:
#     if item in output:
#         output[item] += 1
#     else:
#         output[item] = 1
# print(output)


# 2. is and ==
# Example 1: List with same values but different objects
# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# print(list1 == list2)  # True
# print(list1 is list2)  # False - list1 and list2 are different objects in memory

# 3. A list is a mutable sequence of values, while a tuple is an immutable sequence of values.
# The tricky part is that because tuples are immutable, they can be used as keys in dictionaries
# or as elements in sets, while lists cannot.

# 4. String
string = 'HelloWorld'
print(string[::-len(string)])
