 
"""  Comments starts with a #, and Python will ignore them:
# this  used for single line comments 
three double quotes at the start and end used for multi line comments

"""
# variables
name="javeria"
age=20

# printing variables
print(name)
print(age )

# we can change/modify the value od variables after declaring it
name="ayesha"
print("the value in variable name after modifying it ",name)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
unique="agv"  # this variable of string type
print("before modfiying ",type(unique))
unique= 45598  # this variable of int type
print("after modfiying ",type(unique))
# to check the type of any variable we use bulit in function type

# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3' data type  is string
y = int(3)    # y will be 3   data type  is integer
z = float(3)  # z will be 3.0  data type  is float

print(x, "and it type is ",type(x))
print(y, "and it type is ",type(y))
print(z, "and it type is ",type(z))

# Variable names are case-sensitive.
# single or double quotes both work the same
a="abc" 
A='Monday'


# a and A both are different variables
print(a)
print(A)

# Python allows you to assign values to multiple variables in one line:
l, m, n = "Orange", "Banana", "Cherry"
print(l)
print(m)
print(n)

# you can assign the same value to multiple variables in one line:
rollno=serialNo = 0
print(rollno)
print(serialNo)
