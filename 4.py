# Task 4: Reverse a string without using [::-1] or built-in methods
#My thought process:
# - I wanted to reverse a word without using shortcuts like [::-1].
# - I'll build a new string by putting each character at the front.

text = "PyCharm"
reversed_word = ''

for letter in text:
    reversed_word = letter + reversed_word  # Add each letter at the beginning

print("Reversed word:", reversed_word)

