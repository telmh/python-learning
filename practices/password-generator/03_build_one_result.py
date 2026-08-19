# Practice 3
# Ask: How many fruits do you want?
# Loop that many times. Each time, pick a random fruit.
# After the loop, print ONE result that contains every fruit you picked.
# Do not print inside the loop.

import random

fruits = ["apple", "banana", "mango", "kiwi", "pear"]

# Your code here
how_many = int(input("How many fruits do you want? "))

picked_fruits = []

for i in range(how_many):
    fruit = random.choice(fruits)
    picked_fruits.append(fruit)

print(picked_fruits) 


