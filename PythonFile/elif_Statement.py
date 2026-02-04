# elif Statement

'''
Level = int(input("enter your level  based on your level select the tools: "))
if Level <= 10:
    print("learn : Linux , git , netwoking ")
elif Level <= 30:
    print(" Cloud service (AWs, GCP,  Azure)")
elif Level <= 50:
    print("Docker K8s, CI/Cd")
else :
    print("Complete Revions ")

'''

# Nested if..else Conditional Statement

'''
age = 70
is_member = True

if age >= 70:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")
'''


 # Ternary Conditional Statement

age  = 2
s = "adult" if age >= 18 else "minor"
print(s)


# Ternary Conditional Statement

number = 5

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")