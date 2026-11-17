# Even or Odd
num=int(input("Enter a number: "))
if num%2==0:
    print("Even number")
else:
    print("Odd number")

# Find the Largest of Three Numbers
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if num1>num2 and num1>num3:
    print("Greatest no: ",num1)
elif num2>num3:
    print("Greatest no: ",num2)
else:
    print("Greatest no: ",num3)

                    # Python fundamentals

# 1	Personal Details	Accept name, age, city and display them.
# --------------------------------------------------------------
# name=input("Enter your name: ")
# age=int(input("Enter your age: "))
# city=input("Enter your city: ")
# print("\nPersonal Details\n--------------------")
# print("Name: ",name)
# print("Age: ",age)
# print("City: ",city)

# 2	Simple Calculator	Accept two numbers and perform +, -, *, /.
# ----------------------------------------------------------------
# a,b=input("Enter two numbers: ").split()
# a=float(a)
# b=float(b)
# add=a+b
# diff=a-b
# prod=a*b
# print(f"Sum: {add}")
# print(f"Difference: {diff}")
# print(f"Product: {prod}")
# if b==0:
#     print("Cannot divide by zero")
# else:
#     quot=a/b
#     print(f"Quotient: {quot}")

# 3	Temperature Converter	Convert Celsius to Fahrenheit.(F = (C X 9/5)+32)
# --------------------------------------------------------
# c=float(input("Enter temperature in Celsius: "))
# f=(c*9/5)+32
# print(f"Temperature in Fahrenheit: {f}")

# 4	Rectangle Calculator	Calculate area and perimeter.[Area = Length * Width, Perimeter = 2 * (Length + Width)]
# ----------------------------------------------------------------------------------------------------------------
# length=float(input("Enter length: "))
# width=float(input("Enter width: "))
# area=length*width
# perimeter=2*(length+width)
# print(f"Area: {area}")
# print(f"Perimeter: {perimeter}")

# 5	Average Calculator	Accept marks for five subjects and calculate total and average.
# ------------------------------------------------------------------------------------
# name=input("Enter your name: ")
# m1=int(input("Subject1 Mark: "))
# m2=int(input("Subject2 Mark: "))
# m3=int(input("Subject3 Mark: "))
# m4=int(input("Subject4 Mark: "))
# m5=int(input("Subject5 Mark: "))
# # total=m1+m2+m3+m4+m5
# total=sum([m1,m2,m3,m4,m5])
# average=total/5
# print(f"Name :{name}")
# print(f"Marks: {m1},{m2},{m3},{m4},{m5}")
# print(f"Total: {total}")
# print(f"Average: {average}")

            # Conditional statements

# 6   Largest of Four	Find the largest among four numbers.
# ----------------------------------------------------------
# a,b,c,d=input("Enter 4 numbers: ").split()
# a=int(a)
# b=int(b)
# c=int(c)
# d=int(d)
# if(a>=b and a>=c and a>=d):
#     print(f"Greatest Number is: {a}")
# elif(b>=c and b>=d):
#     print(f"Greatest Number is: {b}")
# elif(c>=d):
#     print(f"Greatest Number is: {c}")
# else:
#     print(f"Greatest Number is: {d}")

# 7	Grade Calculator	Assign grades based on average marks.
# -----------------------------------------------------------
# name=input("Enter your name: ")
# m1=int(input("Subject1 Mark: "))
# m2=int(input("Subject2 Mark: "))
# m3=int(input("Subject3 Mark: "))
# m4=int(input("Subject4 Mark: "))
# m5=int(input("Subject5 Mark: "))
# total=sum([m1,m2,m3,m4,m5])
# average=total/5
# if m1>=50 and m2>=50 and m3>=50 and m4>=50 and m5>=50:
#   if average>=90:
#     print("Excellent")
#   elif average>=75:
#     print("Very Good")
#   elif average>=50:
#     print("Pass")
#   else:
#     print("Fail")
# else:
#   print("Fail")
# 8	Leap Year	Check whether a year is a leap year.
      # It is divisible by 400, OR
      # It is divisible by 4 but NOT divisible by 100.
# ------------------------------------------------
# y=int(input("Enter a year: "))
# if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
#     print("Leap year")
# else:
#     print("Not leap year")
# 9	Electricity Bill	Calculate bill based on unit consumption and given slabs.
# ----------------------------------------------------------------------------

# 10	Login Validation	Check username and password against predefined values.
# -------------------------------------------------------------
# 11	Age Eligibility	Check eligibility for voting based on age.
# -------------------------------------------------------------
# 12	Triangle Validator	Check whether three sides can form a triangle.
# -------------------------------------------------------------
# Problem-solving challenges
# 13	Even Numbers	Check whether a number is even or odd and print the result.
# -------------------------------------------------------------
# 14	Number Reversal	Reverse a three-digit integer using arithmetic operators.
# -------------------------------------------------------------
# 15	Palindrome Number	Check whether a number reads the same backward.
# -------------------------------------------------------------
# 16	Armstrong Number	Check whether a three-digit number is an Armstrong number.
# -------------------------------------------------------------
# 17	Multiplication Table	Print the multiplication table of a given number from 1 to 10.
# -------------------------------------------------------------
# 18	Factorial	Calculate the factorial of a positive integer.
# -------------------------------------------------------------