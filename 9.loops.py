"""loops has 4 main things
1 - iterater --- here i is iterater 
2- condition on which loop checks. until it become false the loop will continue to execute --- here while i<10
3- incrementer- statement that increment the iterater --- here i +=1 is incrementer
4- code - that execute in each loop --- here print(i)
same as if-else case the indentation is important"""

#While loop
i=1
while i<10:
    print(i)
    i +=1
    
#printing patterns
i=1
while i<=10:
    print(i*"*")
    i +=1 
    
# printing same pattern but in reverse
print("reverse pattern")
i=10
while i>=1:
    print(i*"*")
    i -=1    
    
# for loop --here range is built function that print number till the given number
# i is iterater for each number in range for loop will print the value of i
for i in range(5):
     print(i)   

#range start from 0 if we want to start with 1 
for item in range(20):
    print(item+1)     
