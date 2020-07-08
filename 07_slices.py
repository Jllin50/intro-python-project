"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# print the second element: 4:
# Your code here
print(a[1])

# print the second-to-last element: 9
# Your code here
print(a[-2:-1])


# print the last three elements in the array: [7, 9, 6]
# Your code here
print(a[-3:])

# Your code here


# print every element except the first one: [4, 1, 7, 9, 6]
# Your code here
print(a[1:])


# print every element except the last one: [2, 4, 1, 7, 9]
# Your code here'
print(a[:-1])



# For string s...

s = "Hello, world!"


# print just the 8th-12th characters: "world"
# Your code here


print(s[7:12])
