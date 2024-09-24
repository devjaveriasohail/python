"""if ,elif,else are keyword used for if- else statments
here block of code that need to be execute when any condition is true is presented 
by the indentation. in dentation is 4 spaces together. so it is important to write code with proper indentation
 """
age = int(input("enter your age "))  # int () to convert input to integer datatype
if age >= 18:
    print("Your are an adult")
elif age<18 and age>3:
    print("Your are an child")
else :
    print("Your are an kid")
    
    
    