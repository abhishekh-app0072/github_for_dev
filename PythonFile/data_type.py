a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for":2, "Geeks":3}


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))


# Type of variable 

n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
bool = True

print(type(n))   
print(type(f)) 
print(type(s))   
print(type(li))     
print(type(d))     
print(type(bool))


# concept of object Reference 
'''
x = 5
y = x  #  x = 5 now y = 5
# x-> 5 <-Y
x = apple
y = mango  # y change the the old value to new value 
5 = garbage value 

# Deleting a Varible 
x = 10
del x
print(x)'''

# python data type # 

x =  10  # int 
y = 12.90  # float 
z = "hello" # string 
a = [1,2,3,"abc", "abhishek","age", 12.0]  # list 
b = (1,2,3,4,5, "abc ", "for", "abc")  # tuple
c = {"key" : "value" }  # dicst or set 


# Numeric Data Types

x = 123
print(type(x))

y =  12.89
print(type(y))

z =  2+4j
print(type(z))

# Numeric Data Types
    # String Data Type

s =  "welcome to python 30 days"

print(s)
print(type(s))
print(s[1])
print(s[6])
print(s[-1])


# List  

a = []
print(a)

b = [1,2,3,4,5,]
print(b)

c = [1,2,3,4, "hello","world", 2.90]
print(c)


# Access List Items

a = ["Geeks", "For", "Geeks"]
print("Accessing element from the list")
print(a[0])
print(a[2])

print("Accessing element using negative indexing")
print(a[-1])
print(a[-3])


# Tuple Data Type
tup1 =  ()

tup2 = " welcome to day 3  of python"

print("\nTuple with the use of String: ", tup2)


# Access Tuple Items

t1 = ()
t2 = (1,2,3,4,5,0.3)
t3 = ( "apple" , "banana",  "mango", 1,2,3 , 2.30)

print(t2[5])
print(t3[3])



# 3. Boolean Data Type 

print(type(True))
print(type(False))
#print(type(true)) true is wrong way to write here case sensetive

# Truthy and Falsy Values

if 1:
    print("1 is truthy")

if not 0:
    print("0 is falsy")


# 4. Set Data Type

s1 = set()
print(s1)

s2 = set ("abhishekprasad")
print(s2)

s3 =  set(["abc" ,"123", "apple"])
print(s3)

