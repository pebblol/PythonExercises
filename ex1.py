# ex 1

# Asks the user to enter their name and age.
# Prints out a message that tells them in what year they turn 100 years old.

name = input("Enter your name: ")
age = int(input("Enter your age: "))

year = 100 - age

msg = name + ", it will be " + str(year) + " years until you turn 100 years old.\n"

print(msg)

# Prints out copies of the message
num = int(input("Enter a number: "))

print(num * msg)
