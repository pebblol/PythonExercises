# ex 3

# Print elements of the list that are less than the number the user inputted.

list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

list2 = []

print("Current list: " + str(list1))

n = int(input("Enter a number: "))

for num in list1:
    if num < n:
        list2.append(num)

print("New list with only elements less than " + str(n) + ": " + str(list2))
