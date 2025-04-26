#Task 6: Sum of digits of a number
#My thought process:
# - I want to sum each digit of the number.
# - I'll keep getting the last digit using %10 and removing it using //10.

digit_sum = 9876
total = 0

while digit_sum != 0:
    last_digit = digit_sum % 10
    total += last_digit
    digit_sum //= 10

print("Sum of the digits is:", total)



