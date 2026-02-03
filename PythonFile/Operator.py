''' Python  Operator'''

''' In Python programming, Operators in general are used to perform operations on values and variables.

- Operators: Special symbols like -, + , * , /, etc.
- Operands: Value on which the operator is applied.
'''


# Types of Operators in Python

''' Arithmetic Operators'''

'''
a  = 10
b  = 15 

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)
'''

# Comparison Operators
'''
x = 2
y = 5

print(x>y)  # greater than
print(x<y)  # less than 
#print(x=y)  # equal to 
print(x>=y) # greater than equal to 
print(x<=y) # less than equal  to 
print(x!=y) #  not equal to 
print(x==y) # double equal to 

'''

# Logical Operators
"""
a = True
b = False

print(a and b) # F
print(a or b)  # T
print(not b)  # T
print(not a)  # F
"""

 # Bitwise Operators 
'''
1. Bitwise NOT
2. Bitwise Shift
3. Bitwise AND
4. Bitwise XOR
5. Bitwise OR
'''
'''
a = 2
b = 6
print(a & b)
print(a | b)
print(a ^ b)
print(a >> b)
print(a <<b)
print(~a)
print(~b)
print(a<<2)
print(b<<2)
print(a>>2)
print(b>>2)
'''

# Assignment Operators
'''
a = 10
b = a
print(b)

b += a
print(b)

b -= a
print(b)

b *= a
print(b)

b <<= a
print(b)
'''

# Identity Operators
'''
is          True if the operands are identical 
is not      True if the operands are not identical 
'''

a = 10 
b = 20 
c = a

print(a is c)
print(a is not b)
print(a is b)

''''
if a is  c:
    print("True")
else:
    print(" False")
 '''

 # Membership Operators

'''
in            True if value is found in the sequence
not in        True if value is not found in the sequence
'''
x = [ 20, 10, 23, 29]

num = 26
if num  in x:
    print("yes")
else:
    print("NO")



x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")


# Ternary Operator

a, b = 10, 20
min = a if a<b else b

print(min)


 #Precedence and Associativity of Operators

 # Operator Precedence

expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")


# Operator Associativity
print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)