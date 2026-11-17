'''
    Personal information

    Ask the user to enter:
    - Name
    - Age
    - Qualification
    - Current profession
    Display all the details using f-strings.
'''
name=input("Enter your name: ")
age=int(input("Enter your age: "))
qualification=input("Enter your qualification: ")
current_profession=input("Enter your current profession: ")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Qualification: {qualification}")
print(f"Current profession: {current_profession}")

'''
    Basic calculator

    Ask the user to enter two numbers. Display:
    - Addition
    - Subtraction
    - Multiplication
    - Division
'''
a,b=input("Enter two numbers: ").split()
a=int(a)
b=int(b)
print(f"Addition: {a+b}")
print(f"Subtraction: {a-b}")
print(f"Multiplication: {a*b}")
print(f"Division: {a/b}")
'''
    Age calculator

    Ask the user to enter their birth year. Calculate and display their approximate age.
'''
year=int(input("Enter your birth year: "))
age=2026-year
print(f"Age: {age}")

