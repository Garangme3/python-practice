# Task 5: Factorial (Recursive)
#My thought process:
#Normally recursion uses a function, but since I can't define one,
# - I'll simulate it manually for a specific number.

n = 4

# Simulating recursion manually for understanding
if n == 0 or n == 1:
    recursive_factorial = 1
else:
    recursive_factorial = n * (n - 1) * (n - 2) * (n - 3)  # Only works up to 4 manually

print(f"Recursive factorial of {n} is {recursive_factorial}")


