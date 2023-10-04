#This is a demonstration on how to create stacks from a module
#The module being used is called deque
#The module also holds the methods used to get information about a stack

#Imports
from collections import deque

mystack = deque()

#Append function
mystack.append(8)
mystack.append(10)
mystack.append(4)
mystack.append(7)
mystack.append(6)
mystack.append(67)

# print(mystack.empty())

print(mystack.getSize)