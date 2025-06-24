# Example 1: Simple if statement
age = 18
if age >= 18:
    print("You are an adult.")
    print("You can vote.")

print("This always prints regardless of the age condition.")

# Example 2: Another simple if statement
# temperature = 75
# if temperature > 70:
#     print("It's hot outside.")

# Example 3: Simple if statement with comparison
# score = 95
# if score >= 90:
#     print("You got an A+!")

# Example 4: String comparison in if statement
# name = "Alice"
# if name == "Alice":
#     print("Hello, Alice!")

# Example 5: if-else statement
# new_age = 16
# if new_age < 18:
#     print("You are a minor.")
# else:
#     print("You are an adult.")

# Example 6: if-elif-else statement for grading
score = 49
if score >= 90:
    print("You got an A+!")
elif score >= 80:
    print("You got an A!")
elif score >= 70:
    print("You got a B!")
elif score >= 60:
    print("You got a C!")
elif score >= 50:
    print("You got a D!")
else:
    print("You failed.")


age = 20
has_license = True
if age >= 18 and has_license:
    print("You can drive a car.")

day = "Monday"
is_holiday = False
if day == "Saturday" or day == "Sunday" or is_holiday:
    print("It's a day off!")

is_raining = False
if not is_raining:
    print("You can go for a walk.")

weather = "sunny"
temperature = 75

if weather == "sunny":
    print("It's a beautiful day!")
    if temperature > 70:
        print("It's warm outside.")
    else:
        print("It's a bit chilly.")
else:
    print("Not a sunny day.")

user_input = "yes"
if user_input == "yes" or user_input == "y" or user_input == "YES":
    print("You agreed!")

if user_input.lower() == "yes" or user_input == "y":
    print("You agreed with a case-insensitive check!")

age_range = 25

if age_range >= 13 and age_range <= 19:
    print("You are a teenager.")

if 13 <= age_range <= 19:
    print ("You are a teenager.")

email = "user@example.com"
if "@" in email and "." in email:
    print("This is a valid email address.")
else:
    print("This is not a valid email address.")