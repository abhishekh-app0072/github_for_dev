# Practical Solved Problems of Conditional Statements

## if Statement##


# Problem 1: Check if user is eligible to vote# 
''' 
age = int(input("Enter  your age : "))

if age  >= 18 :
    print("Yes, u are Eligible for vote")
else:
    print("Not")
'''

# Problem 2: Check if a number is positive 
'''
num =  int(input("Enter your number psl..: "))

if num % 2 == 0 :
    print("Postive")
else:
    print("negative")
    '''


# if-else Statement

# Problem 1: Check if a student is pass/fail in exam.# 

'''marks  = int(input("enter  your  number : "))

if marks >= 40 :
    print("pass")
else :
    print("fail")
'''

 # Problem 2: Check if a user has balance to buy an item

'''

balance =  int(input("Enter your balance : "))
price = float(input(" Enter your product price : "))

if balance >= price:
    print("buy")
else:
    print("Not Buy") 

'''

# if-elif-else Statement 
# Problem 1: Suggest a mode of transport based on distance

'''

distance =  float(input("Enter your traveling distance in (Km) :"))

if distance <= 10 :
    print("Auto")
elif  distance <= 30:
    print( " Local Bus")
elif distance <= 100:
    print("Expres bus")
else:
    print("Train")
    
'''

#  Problem 2: Battery status

'''
battery = int(input("Enter your percentage of battery : "))

if battery <= 20 :
    print("low charging ")
elif battery <= 50 :
    print("mid level charge ")
elif battery <= 80 :
    print( " 80%  charging ")
elif battery <= 95:
    print(" almost charge done ")
else:
    print("fullcharge ")
'''
# 
''' b =  int( input ( " enter your b  % "))

if b >= 80 :
    print( " battery full")
elif  b >= 50 :
    print("half charge ")
else :
    print("low  battery ")

 '''

# Nested if-else Statement 

  # Problem 1: Login with username and password

user =(input("enter your user  name: "))
psw = (input("Enter Your pass word  : "))

if user == "abhishek" :
    if psw == "12345":
        print("correct password , welcome to window he ll o  Abhishek  welcome back t o ypur PC")
    else: 
        print("wrong password pls check, again enter your correct username or password ")

 
# Problem 2: Check exam pass and scholarship eligibility  

