line=input("Enter a string ")
print(line)

"""below are some bulit in method that we can directly perform on string
  these method return the new string with the change the original string remain same
 we can directly print it or either store it new variable"""
# upper method - return string will all upper case
print(line.upper())  

#lower method -return string with all lower case
lower=line.lower()
print(lower)

# find- find any letter/characher and return its first occurance postion/index and if not found return -1
# it is case sensitive mean hello and Hello are different words
print(line.find("a"))
print (line.find("hello")) 

#replace - it will find the given word and replace it with your given word 
# 1 argument take finding word and 2 argument take the word to replace it
print(line.replace("hello","hi"))
print(line.replace("a","z"))

# in- it find a character or word and return true or false base on result 
print("b"in line)