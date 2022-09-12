# ex 5

# Returns a list that contains only the elements that are common between the lists (w/o duplicates)
# Lists can be different sizes

import random

# 10 random numbers between 1 and 50
x = random.sample(range(1, 50), 10)
y = random.sample(range(1, 50), 15)
z = []

for num in x:
    if num in y:
        z.append(num)

print("List 1: \n" + str(x))
print("List 2: \n" + str(y))
print("List sharing elements from 1 and 2: \n" + str(z))
