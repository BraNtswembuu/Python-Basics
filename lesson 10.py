for i in range(1, 11):
    print("Hello "+ str(i))

# Count  from 1 to 10
for i in range(6):
    print(i)

# Steps
for i in range(0, 10, 5):
    print(i)

# Countdown from 10 to 0
for i in range(10, 0, -1):
    print(i)
print("Blast off!")

# Print loop numbers in one line
for i in range(5):
    print(i, end=" ")

print("\n")
word = "Python"
for letter in word:
    print(letter)

# Loop through a list of fruits
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like " + fruit)

count = 1
while count <= 5:
    print("Count:", str(count))
    count += 1

password = ""
while password != "secret":
    password = input("Enter the password: ")
    if password == "secret":
        print("Access granted!")
    else:
        print("Incorrect password, try again.")
        
print("You have successfully logged in!")