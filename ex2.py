# ex 2

# Asks the user for a number and tell whether it is even or odd.

num = int(input("Enter a number: "))

if (num % 2 == 0):
    print(str(num) + " is an even number.")
elif (num % 2 == 1):
    print(str(num) + " is an odd number.")
elif (num % 4 == 0):
    print(str(num) + " is a multiple of 4.")

# Asks for two numbers if they divide evenly into the first number.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if (num2 % num1 == 0):
    print(str(num2) + " divides evenly into " + str(num1) + ".")
else:
    print(str(num2) + " does not divide evenly into " + str(num1) + ".")
