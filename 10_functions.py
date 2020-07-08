# Write a function is_even that will return true if the passed-in number is even.


# Your code here

def is_even(anumber):
    if anumber % 2 == 0:
        return True
    else:
        return False


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
# Your code here

def callouts(lean):
    if lean == True:
        print("Even!")
    else:
        print("Odd")

callouts(is_even(num))

