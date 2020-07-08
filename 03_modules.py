"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html
import sys
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
import os


# Using the sys module, print out the command line arguments
# in sys.argv, one per line:
# Your code here

print(sys.argv[0])


# Using the sys module, print out the OS platform you're using:
# Your code here
print(sys.platform)

# Using the sys module, print out the version of Python you're using:
# Your code here
print(sys.version)




# Using the os module, print the current process ID
# Your code here
print(os.getpid())


# Using the os module, print the current working directory (cwd):
# Your code here
print(os.getcwd())


# Using the os module, print out your machine's login name
# Your code here
print(os.getlogin())
