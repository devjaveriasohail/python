#to take input from user we use input () keyword and store it value in the variable

name= input("what is your name? ") # storing the input value in variable name
#  printing the inputed data
print("Hi ", name)

age=input("Enter your age ")
print("your age is ",age)

"""" all the inputed store in the string data type 
 to chnage this we use casting- where we change its data type using 
int( ) convert to integer datatype
float() convert to float datatype
bool()  convert to bool datatype
str()  convert to str datatype
"""
print(type(name))
print(type(age))

# casting the age variable datatype to int
new_age=int(age)
print("after casting the data type of age variable is ", type(new_age))