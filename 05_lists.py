# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# Your code here
x.append(4)
print(x)
# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# Your code here
for z in y:
    x.append(z)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# Your code here
x.pop(4)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# Your code here
x.insert(5, 99)
print(x)


# Print the length of list x
# Your code here
print(len(x))


# Print all the values in x multiplied by 1000
# Your code here

for num in x:
    print(num * 1000)
