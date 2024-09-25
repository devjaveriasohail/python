""" functions are of three types
    1. inbuilt functions like int(),bool()
    2. modulue function -- which are import from different library like from math import *
       here * show all function like sqrt -- sqrt give us the sqrt of number
    3. user define function-- function that are define by us.syntax of them is
     def  functionName (parameters):
        // code in function
        """
def addition(a,b):
    return a+b

print(addition(6,7))

#function to  calculate are of triangle
def triangleArea(base,height):
    return 0.5*base*height

#function to calculate area of circle
def circleArea(radius):
    return 3.14*radius*radius

# calling function and taking input from user
base=int(input("Enter the value of base to calulate area of triangle: "))
height=int(input("Enter the value of height to calulate area of triangle: "))
print("The area of triangle is ",triangleArea(base,height))  #calling function and printing answer

radius=int(input("Enter the value of radius to calulate area of circle: "))
print("The area of circle is ",circleArea(radius))  #calling function and printing answer


       