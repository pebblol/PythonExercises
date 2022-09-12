# ex 4

# Asks user for a number, printing out a list of all its divisors.

userNum = int(input("Enter a number: "))

x = range(1, userNum+1)
y = []

for n in x:
    if (userNum % n == 0):
        y.append(n)

print("List of divisors for " + str(userNum) + ": " + str(y))
