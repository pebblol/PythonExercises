# ex 6

# Asks user for string and prints out whether string is palindrome or not

userStr = input("Enter word: ")

userStrReversed = userStr[::-1]

if (userStr == userStrReversed):
    print(userStr + " is a palindrome.")
else:
    print(userStr + " is not a palindrome.")
