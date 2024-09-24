#list in python stores the group  of value and that can be of different data type
marks=[100,89,78,65,40,56,90,37]
print(marks)

#to print value of any index
print(marks[0])
print(marks[3])

# in python if we want to print a value from backward position we can use -1,-2 so no. this start with -1 
print(marks[-1])

#we can make sublist from the list it take two index.1st is starting index and 2nd one last index.the value of last index is not included in sublist
print(marks[2:5])

#for loop in list
print("for loop on list")
for num in marks:
    print(num)
    
# we can perform operation in list using for loop
print("for loop on list with operations")
for num in marks:
    print(num+2)
    
 # operation on list
 # append(value) add the given value on last index in list in the existing list
marks.append(99)
print("append",marks)   

#insert(index,value) --it will add the value at given index 
marks.insert(5,88)
print("insert",marks)

#in check if the given value is present or not return true and false in answer
print("in",100 in marks)

#len(list name) -- give us the length of list
print("length is ",len(marks))

#while loop in list -- for this we can use len function
i=0
while i<len(marks):
    print(marks[i])
    i += 1