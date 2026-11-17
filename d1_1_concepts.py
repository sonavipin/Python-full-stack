
                # Variables,datatypes,operators,i/p and o/p,conditional statements
                #*****************************************************************

'''
Variables

    A variable is a named location used to store data in a program. 
    You create one by assigning with =.Python figures out the type on its own.

    student_name = "Asha"
    age = 21

    Naming rules:
        A variable name must start with a letter or underscore.
        It cannot start with a number.
        It cannot contain spaces.
        Variable names are case-sensitive.
        Python keywords cannot be used as variable names.

    Multiple variable assignment

        a, b, c = 10, 20, 30
        print(a)
        print(b)
        print(c)
    You can also assign the same value to multiple variables:
        x = y = z = 100
'''


'''
Data types

    Type	   Meaning	       Example
    ----------------------------------
    int	       whole numbers	78
    float	   decimal numbers	78.5
    str	       text	            "Maths"
    bool	   True/False	    True
    list	                    numbers = [10, 20, 30]
    tuple	                    numbers = (10, 20, 30)
    set	                        numbers = {10, 20, 30}
    dict	                    student = {"name": "Sona"}

    Check a type with type():

        print(type(78))        # <class 'int'>
        print(type(78.5))      # <class 'float'>
        print(type("hi"))      # <class 'str'>

    Type conversion
        Type conversion means changing one data type into another.
        Type conversion is important because input() always gives you a string 
        (you’ll need it in the next block):

        x = int("45")      # 45 (int)
        y = float("3.5")   # 3.5 (float)
        z = str(100)       # "100" (str)
        
'''

'''
Operators
    Operators are symbols used to perform operations on values and variables.

    Arithmetic

            a, b = 17, 5
            a + b    # 22  addition
            a - b    # 12  subtraction
            a * b    # 85  multiplication
            a / b    # 3.4 division (always returns float)
            a // b   # 3   floor division (drops the decimal part)
            a % b    # 2   remainder (modulus)
            a ** 2   # 289 power/Exponentiation

            Important: Understand the difference between /, // and %.
                - / returns the division result.
                - // returns the floor of the division result.
                - % returns the remainder.
            

    Comparison (result is always True or False)
            These operators compare two values and return True or False.
            Operator	Meaning
                ==	    Equal to
                !=	    Not equal to
                >	    Greater than
                <	    Less than
                >=	    Greater than or equal
                <=	    Less than or equal

    Logical (combine conditions)

            There are three logical operators:
            - and – Both conditions must be True.
            - or – At least one condition must be True.
            - not – Reverses the Boolean result.

            marks = 65
            print(marks >= 35 and marks <= 100)   # True
            print(marks < 35 or marks > 90)       # False
            print(not marks > 50)                 # False

    Assignment operators
            Operator	Example	    Equivalent
                =	     x = 10	    Assign 10
                +=	    x += 5	    x = x + 5
                -=	    x -= 5	    x = x - 5
                *=	    x *= 2	    x = x * 2
                /=	    x /= 2	    x = x / 2
                
                total = 0
                total += 10    # same as total = total + 10
'''

'''
Input and Output
    Output – print()
    We use print() to display information.
        
        name = "Sona"
        age = 36
        print(name)
        print(age)
        print("Welcome to Python")
Input – input()
    We use input() to get information from the user.
        name = input("Enter your name: ")
        print("Welcome", name)

        Important: input() always returns a string, even when the user enters a number.
'''

'''
Conditional statements (if, elif, else)
    Conditional statements allow a program to make decisions.
'''