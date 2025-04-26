#Task 3: Compute factorial using a loop
#My thought process:
# - I want to calculate the factorial by multiplying numbers from 1 up to n.
# - A for loop makes sense because I know exactly how many times I need to multiply.

x = 6
factorial = 1

for j in range(1, x + 1):
    factorial = factorial * j  # Multiply and update the factorial each time

print(f"Factorial of {x} is {factorial}")

