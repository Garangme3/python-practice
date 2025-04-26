#Task 1: Sum all elements in a list
#My thought process:
# - I want to add all the numbers in a list manually.
# - I could have used sum(), but I decided to practice using a for loop.
# - I'll start with 0 and keep adding each number one by one.

numbers = [3, 6, 9, 12]
addition = 0

for number in numbers:
    addition += number  # Adding each number to my total

print("The total sum is:", addition)
