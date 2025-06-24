first_name = "Tom"
last_name = "Ford"
full_names = first_name + " " + last_name
print(full_names)

# Add to existing strings
message = "Hello"
message += " World!"
message += " How are you?"
# print(message)

# Repeating strings
laugh = "Ha" * 3
# print(laugh)

line = "-" * 20
# print(line)

# Useful string methods

text = "Hello, World!"
# print(text.upper())  # Convert to uppercase
# print(text.lower())  # Convert to lowercase
# print(text.split(","))  # Split into a list
# print(text.capitalize())  # Capitalize the first letter
# print(text.title())  # Capitalize the first letter of each word

# Remove extra spaces
messy_text = "          Hello, World!             "
# print(messy_text.strip())  # Remove leading and trailing spaces

# Finding text in a string
sentence = "Python is a great programming language."
# print(sentence.strip()) # Remove extra spaces

# print(sentence.find("great"))  # Find the position of "great"
# print(sentence.find("Java"))  # Find the position of "Java"
# print(sentence.count("o"))  # Count occurrences of "o"

# Checking what's in text
text = "Hello123"
# print(text.startswith("Hello"))  # Check if the text starts with "Hello"
# print(text.endswith("123"))  # Check if the text ends with "123"
# print(text.isalnum())  # Check if the text is alphanumeric
# print("Python" in sentence)  # Check if "Python" is in the sentence
# print("Java" in sentence)  # Check if "Java" is not in the sentence

# Replacing text in a string
message = "I love Python programming!"
new_message = message.replace("Python", "Java")
# print(new_message)  # Replace "Python" with "Java"

# Splitting text
sentence = "apple,banana,cherry"
fruits = sentence.split(",")  # Split into a list
# print(fruits)  # Split into a list

words = "Hello World Python".split()  # Split by spaces
# print(words)  # Split by spaces


words_lists = ",".join(words)  # Join the list into a string
# print(words_lists)  # Join the list into a string

letters = ['a', 'b', 'c', 'd']
new_word ="".join(letters)  # Join the list into a string
# print(new_word)

# String slicing (Getting parts of a string)
text = "Python Programming"
print(text[0:6])  # Get "Python"
print(text[7:18])  # Get "Programming"
print(text[:6])  # Get "Python"
print(text[7:])  # Get "Programming"