# ex 7

# Takes a list and makes a new list containing only the even elements of the original list

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# list comprehension
b = [num for num in a if (num % 2 == 0)]

print("Original list: \n" + str(a))
print ("New list containing only even elements from original list: \n" + str(b))
