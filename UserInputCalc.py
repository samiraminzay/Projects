# This asks what the user wants to do.
userinput = input("What would you like to do?  ")

# If statement for calculating (a*b mod c)
if userinput == 'a*b mod c' or userinput == 'q1':
    a = int(input("what is a? "))
    b = int(input("what is b? "))
    c = int(input("What is c? "))
    y = ((a % c))
    h = y * (b % c)
    n = h % c
    print("This funtion calculates (a*b mod c) "
          "The answer is, ", n)
if userinput == 'a^n * 6^n mod x' or userinput == 'q2' or userinput == "q3":
    a = int(input("what is a? "))
    b = int(input("what is n in (a^n)? "))
    c = int(input("What is b? "))
    d = int(input("What is n in (b^n)? "))
    e = int(input("What is the mod? "))
    calculations = ((a**b)*(c**d))%e
    print("This function calculates (a^n * b^n mod x)"
          "The answer is, ", calculations)


if userinput == 'a mod x' or userinput == 'q4':
    a = int(input("what is a in (a mod x)? "))
    b = int(input("what is x in (a mod x)? "))
    calculations = (a%b)
    print("This function calculates (a mod x)"
          "The answer is, ", calculations)
