"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""
# Each of the following list comprehensions should be written in
# the form:
# y = [list comprehension here]
# print(y)

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]
# Your code here
x = [i for i in range(5)]
print(x)


# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
# Your code here
x = [i**3 for i in range(10)]
print(x)


# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".
a = ["foo", "bar", "baz"]
# Your code here
x = [i.upper() for i in a]
print(x)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.
x = input("Enter comma-separated numbers: ").split(',')
# Your code here
only_even = [num.strip() for num in x if int(num) % 2 == 0] 
print(only_even)


