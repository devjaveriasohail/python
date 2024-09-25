# dictionary store data in key value pair. left side data are key e.g english and right side data are value . we can access our values using key
marks={"english":98,
       "math":100,
       "physics":99,
       "chemistry":78}
print(marks["physics"])

# adding new key value pair
marks["biology"]=89
print(marks)

# we can also modify the existing value
marks["chemistry"]=55
print(marks)