'''
    Age category

    Ask the user's age and display:
    - Below 13 → Child
    - 13–19 → Teenager
    - 20–59 → Adult
    - 60 and above → Senior citizen
'''
age=int(input("Enter your age: "))
if age<13 :
    print("Child")
elif age<=19:
    print("Teenager")
elif age<=59:
    print("Adult")
else:
    print("Senior citizen")
'''
    Number checker

    Ask the user for a number and check whether it is:
    - Positive
    - Negative
    - Zero
'''
num=int(input("Enter a number: "))
if num==0:
    print("Zero")
elif num>0:
    print("Positive number")
else:
    print("Negative number")

'''
    Task: Ask the user for:
        - Name
        - Age
        - Python mark
        - SQL mark
    Then calculate and display total and average.
    Average >= 90  → Excellent
    Average >= 75  → Very Good
    Average >= 50  → Pass
    Otherwise      → Fail
'''
name=input("Enter your name: ")
age=int(input("Enter your age: "))
python_mark=int(input("Enter your Python mark: "))
sql_mark=int(input("Enter your SQL mark: "))
total=python_mark+sql_mark
average=total/2

print("Name: ",name)
print("Age: ",age)
print("Python Mark: ",python_mark)
print("SQL Mark: ",sql_mark)
print("Total: ",total)
print("Average: ",average)
if python_mark>=50 and sql_mark>=50:
    if average>=90:
        s="Excellent"
    elif average>=75:
        s="Very Good"
    elif average>=50:
        s="Pass"
    else:
        s="Fail"   
else:
    s="Fail"
print("Status: ",s)    