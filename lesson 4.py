#  Integer
age = 25
count = 0
temperature = 30.5

# Floaters (numbers with decimal points)
price = 19.99
height = 5.9
new_temperature = 98.6

# Addition
# print(5 + 3)  # Output: 8
# Subtraction
# print(10 - 2)  # Output: 8
# Multiplication
# print(4 * 2)  # Output: 8
# Division
# print(16 / 2)  # Output: 8.0
# Integer Division (gives a whole number)
# print(16 // 3)  # Output: 5
# Remainder (modulus)
# print(16 % 3)  # Output: 1
# Power (exponentiation)
# print(2 ** 3)  # Output: 8
# PEDMAS/BODMAS (Parentheses, Exponents, Division/Multiplication, Addition/Subtraction)
result = 5 + 3 * 4
# print(result)  # Output: 17 (3 * 4 = 12, then 5 + 12 = 17)

result = (5 + 3) * 4
# print(result)  # Output: 32 ((5 + 3) = 8, then 8 * 4 = 32)

x = 10

# # x = x + 5  # Increment x by 5

# # x = x + 5
# x += 5  # Increment x by 5 using shorthand
# print(x)  # Output: 15
# # x = x - 3
# x -= 3  # Decrement x by 3 using shorthand
# print(x) 
# # x = x * 2
# x *= 2  # Multiply x by 2 using shorthand
# print(x) 
# # x = x / 4
# x /= 4  # Divide x by 4 using shorthand
# print(x) 
# # x = x ** 2  # Square x
# x **= 2  # Square x using shorthand
# print(x) 

# #  Converting between types 
# age_text = "22"
# age_number = int(age_text)  # Convert string to integer
# print(age_number + 5)  # Output: 27

# price_text = "19.99"
# price_number = float(price_text)  # Convert string to float
# print(price_number * 2)  # Output: 39.98

# score = 98
# score_text = str(score)  # Convert integer to string
# print("Your score is: " + score_text)  # Output: Your score is: 98

# Absolute value (removes negative sign)
print(abs(-10))  # Output: 10
print(abs(5))  # Output: 5

# Rounding numbers
print(round(3.7))  # Output: 4 (rounds to nearest integer)
print(round(3.14159, 3))  # Output: 3.14 (rounds to 3 decimal places)

numbers = [5, 2, 9, 1, 8, 7]
print(max(numbers))  # Output: 9
print(min(numbers))  # Output: 1
print(sum(numbers))  # Output: 32 (sum of all numbers in the list)  

# Wont work with strings
# user_age = input("Enter your age: ")  # User input as a string
# next_year = user_age + 1

# This Work's
age_text = input("Enter your age: ")  # User input as a string
age = int(age_text)  # Convert string to integer
next_year = age + 1  # Add 1 to the age
print("Next year, you will be " + str(next_year) + " years old.")  # Output: Next year, you will be X years old.

# Check if number are odd or even

number = 7
remainder = number % 2  # Get the remainder when divided by 2

if (remainder == 0):
    print(str(number) + " is even.")
else:
    print(str(number) + " is odd.")
number = 8