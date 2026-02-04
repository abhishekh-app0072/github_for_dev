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

'''
user =(input("enter your user  name: "))
psw = (input("Enter Your pass word  : "))

if user == "abhishek" :
    if psw == "12345":
        print("correct password , welcome to window he ll o  Abhishek  welcome back t o ypur PC")
    else: 
        print("wrong password pls check, again enter your correct username or password ")

 '''

# Problem 2: Check exam pass and scholarship eligibility  

'''
marks = int(input("enter your marks : "))

if marks >= 50 :
    if marks >= 80:
        print("eligible for scholarship")
    else:
        print("Not eligible for sch")
else:
    print("failed")
    '''


 # Ternary Statement

  # Problem 1: Check if number is even
'''
num = int(input("enter your num: "))
if num % 2  == 0 : print("even") 
else : print("odd")

# num = int(input("Enter a number: "))
# print("Even" if num % 2 == 0 else "Odd")

'''

# Problem 2: Compare two numbers

'''
 int(input("enter your number " ))
b = int(input("enter your number " ))

print( "a is greater than b "  if a>b else " b is greater than a")
'''

# Problem 3: Temperature check
'''
temp =  float(input("enter your temp value "))
print("hot" if temp >= 30 else "cool")
'''

# Match- case Statement 

#Problem 1: Assign grade

# grade = input("Enter your grade (A/B/C): ").upper()

# match grade:
#     case "A":
#         print("Excellent")
#     case "B":
#         print("Good")
#     case "C":
#         print("Average")
#     case _:
#         print("Fail")

#Problem 2: Activity Suggestion based on weather condition

# weather = input("Enter the weather (sunny/rainy/cloudy/snowy): ").lower()

# match weather:
#     case "sunny":
#         print("Great day for a picnic!")
#     case "rainy":
#         print("Stay indoors and read a book.")
#     case "cloudy":
#         print("Perfect time for a walk.")
#     case "snowy":
#         print("Build a snowman or go skiing!")
#     case _:
#         print("Unknown weather condition.")


# Problem 3: Mobile notification settings based on user profile mode
mode = input("Enter phone mode (silent/vibrate/loud/do not disturb): ").lower()

match mode:
    case "silent":
        print("Notifications are muted.")
    case "vibrate":
        print("Phone will vibrate for notifications.")
    case "loud":
        print("All notifications will play sound.")
    case "do not disturb":
        print("No calls or notifications will come through.")
    case _:
        print("Invalid mode selected.")