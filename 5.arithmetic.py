# addition
print("add",5+10)

# subtraction 
#we can also store this answer in any variable
ans=10-5
print("sub",ans)

#multiplication
print("multiply",8*9)

# division 
print("division",12/2)  
# division return the answer in decimal from. if we want to remove the digit after the decmical we can use // (double divison mark)
print("division without decimal",12//2)

# modulus/ remainder operator % this sign return the remainder after the division
print("Remainder",13/2)

# power double sterik ** give the power of the digit
print("power",2**8)

i=5
i= i+2  
# we can write the above statement in the more optimize way as both will work same 
i +=2 
# same as case of addition here we can do this for any Arithmetic operator

"""Operater Precedence
operator precedence determines the order in which operations are evaluated in an expression. Operators with higher precedence are evaluated before operators with lower precedence. If two operators have the same precedence, they are evaluated according to their associativity (either left-to-right or right-to-left).
* and / operator are evaluated first than the addition or subtraction
if we want to change the precedance we can use brackets"""

print(2+5*5) #multiplication solved first
print((2+5)*5) # here addition solved first


