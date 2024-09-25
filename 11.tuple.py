# tuple is same as list but it is immutable --mean you cannot change it value
marks=(100,89,76,34,100,89,100)
 #marks[0]=99 this will give us error
 
 # count function -- it give us the count of given number in tuple
print(marks.count(100))

#index -- give the index of given number
print(marks.index(76))

# set -- set is same tuple but it only store unique value and it has curl brackets
number={100,78,90,69,90,50,90}
print(number) #only unique numbers are printed

#for loop
for item in number:
    print(item)